from dash import Dash, html, dcc, Input, Output, dash_table
from pathlib import Path
import datetime
import os, sys
import pandas as pd
import plotly.express as px
import scipy
import dash_bootstrap_components as dbc
import dash


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX])
# app = Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])
# app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])


parent_directory = "/scratch/tweber/DATA/MC_DATA/GENECORE_REPROCESSING_2021_2022/"

l = list()
for run in os.listdir(parent_directory):
    for sample in os.listdir(parent_directory + run):
        if sample not in ["config", "log"]:
            file_path = parent_directory + run + "/" + sample + "/cell_selection/labels.tsv"
            if os.path.isfile(file_path):
                # print(parent_directory, run, sample)
                tmp_df = pd.read_csv(file_path, sep="\t")

                # print("Owner: %s" % Path(file_path).owner())
                # print("Group: %s" % Path(file_path).group())

                # file modification timestamp of a file
                m_time = os.path.getmtime(file_path)
                # convert timestamp into DateTime object
                dt_m = datetime.datetime.fromtimestamp(m_time).date()
                # print("Modified on:", dt_m)

                # file creation timestamp in float
                c_time = os.path.getctime(file_path)
                # convert creation timestamp into DateTime object
                dt_c = datetime.datetime.fromtimestamp(c_time).date()
                # print("Created on:", dt_c)
                tmp_df["run"] = run
                tmp_df["sample"] = sample
                tmp_df["run-sample"] = "{run}<br>{sample}".format(run=run, sample=sample)
                tmp_df["owner"] = Path(file_path).owner()
                tmp_df["group"] = Path(file_path).group()
                tmp_df["datetime_modified"] = dt_m
                tmp_df["datetime_creation"] = dt_c
                l.append(tmp_df)

labels_df = pd.concat(l).reset_index(drop=True)
labels_df["cell"] = labels_df["cell"].str.replace(".sort.mdup.bam", "")

l = list()
for run in os.listdir(parent_directory):
    for sample in os.listdir(parent_directory + run):
        if sample not in ["config", "log"]:
            if os.path.isfile(parent_directory + run + "/" + sample + "/counts/{sample}.info_raw".format(sample=sample)):
                # print(parent_directory, run, sample)
                tmp_df = pd.read_csv(
                    parent_directory + run + "/" + sample + "/counts/{sample}.info_raw".format(sample=sample), sep="\t", skiprows=13
                )
                tmp_df["Sample"] = sample
                l.append(tmp_df)
info_df = pd.concat(l)
info_df["cell"] = info_df["cell"].str.replace(".sort.mdup.bam", "")

final_df = pd.merge(labels_df, info_df, on=["sample", "cell"])
final_df.loc[(final_df["prediction"] == 1) & (final_df["pass1"] == 1), "prediction_status"] = "ashleys + mosaic"
final_df.loc[(final_df["prediction"] == 1) & (final_df["pass1"] == 0), "prediction_status"] = "ashleys"
final_df.loc[(final_df["prediction"] == 0) & (final_df["pass1"] == 1), "prediction_status"] = "mosaic"
final_df.loc[(final_df["prediction"] == 0) & (final_df["pass1"] == 0), "prediction_status"] = "None"
final_df["%dupl"] = 100 * (final_df["dupl"] / final_df["mapped"])
final_df["%dupl"] = final_df["%dupl"].round(2)
final_df["datetime_creation"] = pd.to_datetime(final_df["datetime_creation"])
# return final_df


df_datatable = final_df[
    [
        "owner",
        "datetime_creation",
        "run",
        "sample",
        "cell",
        "probability",
        "prediction",
        "pass1",
        "prediction_status",
        "mapped",
        "good",
        "%dupl",
    ]
]

barplot_df_mosaic = final_df.groupby(["run-sample", "run", "sample"])["prediction_status"].value_counts().rename("count").reset_index()


# Multiple components can update everytime interval gets fired.
# @app.callback(Output('example-graph', 'figure'),
#               Input('interval-component', 'n_intervals')
#               )
# Text field
def drawText():
    return html.Div(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                html.H2("Text"),
                            ],
                            style={"textAlign": "center"},
                        )
                    ]
                )
            ),
        ]
    )


print([html.Div(dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])) for page in dash.page_registry.values()])

app.layout = html.Div(
    children=[
        html.Img(src="https://upload.wikimedia.org/wikipedia/en/thumb/b/b1/EMBL_logo.svg/1200px-EMBL_logo.svg.png", width="200"),
        html.Div(
            id="description-card",
            children=[
                html.H5("ashleys-qc-pipeline dashboard"),
                html.Div(
                    id="intro",
                    children="Explore clinic patient volume by time of day, waiting time, and care score. Click on the heatmap to visualize patient experience at different time points.",
                ),
                dcc.Dropdown(
                    sorted(df_datatable["run"].unique().tolist()),
                    sorted(df_datatable["run"].unique().tolist()),
                    id="run-dropdown",
                    style={"fontSize": 12, "font-family": "sans-serif"},
                    multi=True,
                ),
                dcc.Dropdown(
                    # sorted(df_datatable["sample"].unique().tolist()),
                    value=sorted(df_datatable["sample"].unique().tolist()),
                    id="sample-dropdown",
                    style={"fontSize": 12, "font-family": "sans-serif"},
                    multi=True,
                ),
                html.Div(id="dd-output-container"),
            ],
        ),
        html.Div(
            [html.Div(dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])) for page in dash.page_registry.values()]
        ),
        html.Div(dcc.Link("Grafana", href="http://localhost:3000", refresh=True)),
        dash.page_container,
        dash_table.DataTable(
            id="table-data",
            columns=[{"name": i, "id": i} for i in df_datatable.columns],
            page_size=96,
            fixed_rows={"headers": True},
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            # row_selectable="multi",
            style_table={"overflowX": "auto"},
            style_cell={
                "fontSize": 12,
                "font-family": "sans-serif",
                # all three widths are needed
                "width": "{}%".format(len(df_datatable.columns)),
                "textOverflow": "ellipsis",
                "overflow": "hidden",
            },
        ),
        dcc.Graph(id="graph-bar"),
        # dcc.Graph(id="graph-violin-good-overtime"),
        dcc.Graph(id="graph-violin-good"),
        dcc.Graph(id="graph-violin-dupl"),
    ]
)


@app.callback(Output("sample-dropdown", "options"), Input("run-dropdown", "value"))
def set_sample_options(value):
    return df_datatable.loc[df_datatable["run"].isin(value)].sort_values(["run", "sample"])["sample"].unique().tolist()


@app.callback(Output("sample-dropdown", "value"), Input("sample-dropdown", "options"))
def set_sample_value(value):
    # print(value)
    # print(df_datatable.loc[df_datatable["sample"].isin(value)].sort_values(["run", "sample"])["sample"].unique().tolist())
    return df_datatable.loc[df_datatable["sample"].isin(value)].sort_values(["run", "sample"])["sample"].unique().tolist()


@app.callback(Output("dd-output-container", "children"), Input("sample-dropdown", "value"), Input("run-dropdown", "value"))
def update_output(sample, run):
    # print(sample)
    return f"You have selected {sample} from {run}"


@app.callback(Output("graph-bar", "figure"), Input("sample-dropdown", "value"))
def update_bar(value):
    # print(barplot_df_mosaic["run-sample"].values.tolist())
    return px.bar(
        barplot_df_mosaic.loc[barplot_df_mosaic["sample"].isin(value)].sort_values(by=["run-sample"]),
        x="run-sample",
        y="count",
        color="prediction_status",
        barmode="stack",
        color_discrete_map={"ashleys + mosaic": "green", "mosaic": "lightgreen", "None": "red"},
        template="none",
    )


@app.callback(Output("graph-violin-good", "figure"), Input("sample-dropdown", "value"))
def update_bar(value):
    return px.violin(
        final_df.loc[(final_df["prediction"] == 1) & (final_df["sample"].isin(value))].sort_values(by=["run-sample"]),
        x="sample",
        y="good",
        points="all",
        color="run",
        hover_data=["cell"],
        box=True,
        template="none",
    )


@app.callback(Output("graph-violin-dupl", "figure"), Input("sample-dropdown", "value"))
def update_bar(value):
    return px.violin(
        final_df.loc[(final_df["prediction"] == 1) & (final_df["sample"].isin(value))].sort_values(by=["run-sample"]),
        x="sample",
        y="%dupl",
        points="all",
        color="run",
        hover_data=["cell"],
        box=True,
        template="none",
    )


# @app.callback(Output("graph-violin-good-overtime", "figure"), Input("sample-dropdown", "value"))
# def update_bar(value):
#     print(value)
#     return px.violin(
#         final_df.loc[(final_df["prediction"] == 1) & (final_df["sample"].isin(value))].sort_values(["datetime_creation", "sample", "cell"]),
#         x="datetime_creation",
#         y="good",
#         color="sample",
#         box=True,
#         points="all",
#         hover_data=["cell"],
#         template="none",
#     )


@app.callback(Output("table-data", "data"), Input("sample-dropdown", "value"))
def create_dataframe(value):
    return df_datatable.loc[df_datatable["sample"].isin(value)].sort_values(by=["run", "sample"]).to_dict("records")


if __name__ == "__main__":
    app.run(
        debug=True,
        host="seneca.embl.de",
        port=5500,
    )
