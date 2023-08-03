import dash
from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
from pathlib import Path
import datetime
import os, sys
import pandas as pd
import plotly.express as px


# TO REGISTER THE PAGE INTO THE MAIN APP.PY
# app = dash.Dash(__name__)
dash.register_page(__name__, path="/")


# HEADER PART
def Header(title, subtitle):
    title = html.H2(title, style={"margin-top": 5}, className="display-4")
    subtitle = html.H4(subtitle, style={"margin-top": 5})
    # logo = html.Img(src=app.get_asset_url("dash-logo.png"), style={"float": "right", "height": 50})
    logo_embl = html.Img(src="https://upload.wikimedia.org/wikipedia/en/thumb/b/b1/EMBL_logo.svg/1200px-EMBL_logo.svg.png", width="200")
    logo_snakemake = html.Img(src=dash.get_asset_url("snake.png"), width="200")
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Row([dbc.Col(title, md=9), dbc.Col(logo_embl, md=3)]),
                html.Hr(),
                dbc.Row([dbc.Col(subtitle, md=9), dbc.Col(logo_snakemake, md=3)]),
            ]
        )
    )


########

# THIS PART IS WHERE YOU WILL PROCESS YOUR DATA

## NEED TO BE CHANGED AND ADAPTED

parent_directory = "/scratch/tweber/DATA/MC_DATA/GENECORE_REPROCESSING_2021_2022/"

# FIRST ITERATION ON THE LABELS FILES
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
                tmp_df["run-sample"] = "{run}-{sample}".format(run=run, sample=sample)
                tmp_df["owner"] = Path(file_path).owner()
                tmp_df["group"] = Path(file_path).group()
                tmp_df["datetime_modified"] = dt_m
                tmp_df["datetime_creation"] = dt_c
                if sample == "LanexBuesraKM1080":
                    print("LanexBuesraKM1080")
                    print(tmp_df)
                l.append(tmp_df)

# CONCAT LABELS INTO A SINGLE DF
labels_df = pd.concat(l).reset_index(drop=True)
labels_df["cell"] = labels_df["cell"].str.replace(".sort.mdup.bam", "")


# SECOND ITERATION ON THE COUNTS FILE (need to be optimised into a single for loop)
l = list()
for run in os.listdir(parent_directory):
    for sample in os.listdir(parent_directory + run):
        if sample not in ["config", "log"]:
            if os.path.isfile(parent_directory + run + "/" + sample + "/counts/{sample}.info_raw".format(sample=sample)):
                # print(parent_directory, run, sample)
                tmp_df = pd.read_csv(
                    parent_directory + run + "/" + sample + "/counts/{sample}.info_raw".format(sample=sample), sep="\t", skiprows=13
                )
                tmp_df["run"] = run
                tmp_df["sample"] = sample
                l.append(tmp_df)

# CONCAT LABELS INTO A SINGLE DF
info_df = pd.concat(l)
info_df["cell"] = info_df["cell"].str.replace(".sort.mdup.bam", "")

# FINAL MERGE & POSTPROCESSING
final_df = pd.merge(labels_df, info_df, on=["run", "sample", "cell"])
final_df.loc[(final_df["prediction"] == 1) & (final_df["pass1"] == 1), "prediction_status"] = "ashleys + mosaic"
final_df.loc[(final_df["prediction"] == 1) & (final_df["pass1"] == 0), "prediction_status"] = "ashleys"
final_df.loc[(final_df["prediction"] == 0) & (final_df["pass1"] == 1), "prediction_status"] = "mosaic"
final_df.loc[(final_df["prediction"] == 0) & (final_df["pass1"] == 0), "prediction_status"] = "None"
final_df["%dupl"] = 100 * (final_df["dupl"] / final_df["mapped"])
final_df["%dupl"] = final_df["%dupl"].round(2)
final_df["datetime_creation"] = pd.to_datetime(final_df["datetime_creation"])
final_df["year"] = final_df["run"].apply(lambda r: r.split("-")[0])
# return final_df
# final_df.to_csv("data_wf.tsv", index=False)

# FINAL DF TO BE DISPLAYED ON THE DASHBOARD
df_datatable = final_df[
    [
        "owner",
        "year",
        # "datetime_creation",
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

# DF TO BE USED IN BARPLOT
barplot_df_mosaic = final_df.groupby(["run-sample", "run", "sample"])["prediction_status"].value_counts().rename("count").reset_index()
# print(df_datatable)


# Card components
cards = [
    dbc.Card(
        [
            html.H2("{value}".format(value=df_datatable.run.nunique()), className="card-title"),
            html.P("Runs number", className="card-text"),
        ],
        body=True,
        color="light",
    ),
    dbc.Card(
        [
            html.H2(
                "{value_sample} / {value_cell:,}".format(
                    value_sample=df_datatable["sample"].nunique(), value_cell=df_datatable.cell.nunique()
                ),
                className="card-title",
            ),
            html.P("Samples / Cells processed", className="card-text"),
        ],
        body=True,
        color="dark",
        inverse=True,
    ),
    dbc.Card(
        [
            html.H2("{value:,}".format(value=int(df_datatable.good.mean())), className="card-title"),
            html.P("Average number of reads / cell", className="card-text"),
        ],
        body=True,
        color="primary",
        inverse=True,
    ),
    dbc.Card(
        [
            html.H2("{value}%".format(value=int(df_datatable["%dupl"].mean())), className="card-title"),
            html.P("Average rate of duplicates / cell", className="card-text"),
        ],
        body=True,
        color="green",
        inverse=True,
    ),
]

######################
# MAIN LAYOUT OF THE DASH APP
layout = dbc.Container(
    [
        # HEADER
        Header("Workflow results dashboard", "snakemake/ashleys-qc-pipeline v1.4.1"),
        html.Hr(),
        # CARDS ROW
        dbc.Row([dbc.Col(card) for card in cards]),
        html.Br(),
        # FIRST DROPDOWN ROW
        dbc.Row(
            [
                html.Div(
                    [
                        html.H2("Year selection:", className="card-title"),
                        dcc.Dropdown(
                            sorted(df_datatable["year"].unique().tolist()),
                            sorted(df_datatable["year"].unique().tolist())[-1:],
                            id="year-dropdown",
                            style={"fontSize": 12, "font-family": "sans-serif"},
                            multi=True,
                        ),
                    ]
                )
            ]
        ),
        html.Br(),
        # SECOND DROPDOWN ROW
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H2("Run selection:", className="card-title"),
                            dcc.Dropdown(
                                sorted(df_datatable["run"].unique().tolist()),
                                sorted(df_datatable.loc[df_datatable["year"] == 2023]["run"].unique().tolist()),
                                id="run-dropdown",
                                style={"fontSize": 12, "font-family": "sans-serif"},
                                multi=True,
                            ),
                        ]
                    )
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.H2("Sample selection:", className="card-title"),
                            dcc.Dropdown(
                                # sorted(df_datatable["sample"].unique().tolist()),
                                value=sorted(df_datatable.loc[df_datatable["year"] == 2023]["sample"].unique().tolist()),
                                id="sample-dropdown",
                                style={"fontSize": 12, "font-family": "sans-serif"},
                                multi=True,
                            ),
                        ]
                    )
                ),
            ]
        ),
        html.Hr(),
        html.H2("Choose your grouping method", className="card-title"),
        html.Div(
            [
                dbc.RadioItems(
                    options=[
                        {"label": "Run", "value": "run"},
                        {"label": "Sample", "value": "sample"},
                    ],
                    id="radioitems-inline-input",
                    value="run",
                    inline=True,
                ),
            ]
        ),
        html.Hr(),
        html.Br(),
        html.Br(),
        html.Br(),
        # FIRST PLOT
        html.H2("Cell quality predictions", className="card-title"),
        html.Hr(),
        dcc.Graph(id="graph-bar"),
        html.Br(),
        # SECOND PLOT
        html.H2("Binned reads distribution", className="card-title"),
        html.Hr(),
        dcc.Graph(id="graph-violin-good"),
        html.Br(),
        # THIRD PLOT
        html.H2("% duplicates distribution", className="card-title"),
        html.Hr(),
        dcc.Graph(id="graph-violin-dupl"),
        html.Br(),
        # DATATABLE
        html.H2("Datatable exploration", className="card-title"),
        html.Hr(),
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
            export_format="xlsx",
        ),
        # dbc.Row([dbc.Col(graph) for graph in graphs]),
        # dash.page_container,
    ],
    fluid=False,
)


# THIS PART IS TO ORCHESTRATES THE NESTED DROPDOWNS TO INTERACT WITHIN EACH OTHERS
######
# YEAR DROPDOWN VALUE TO RUN DROPDOWN OPTIONS
@dash.callback(Output("run-dropdown", "options"), Input("year-dropdown", "value"))
def set_year_options(value):
    return df_datatable.loc[df_datatable["year"].isin(value)].sort_values(["run", "sample"])["run"].unique().tolist()


# RUN DROPDOWN OPTIONS TO RUN DROPDOWN VALUE
@dash.callback(Output("run-dropdown", "value"), Input("run-dropdown", "options"))
def set_run_options(value):
    # print(value)
    return value


# RUN DROPDOWN VALUE TO SAMPLE DROPDOWN OPTIONS
@dash.callback(Output("sample-dropdown", "options"), Input("run-dropdown", "value"))
def set_sample_options(value):
    # print(value)
    return df_datatable.loc[df_datatable["run"].isin(value)].sort_values(["run", "sample"])["sample"].unique().tolist()


# SAMPLE DROPDOWN OPTIONS TO SAMPLE DROPDOWN VALUE
@dash.callback(Output("sample-dropdown", "value"), Input("sample-dropdown", "options"))
def set_sample_value(value):
    return df_datatable.loc[df_datatable["sample"].isin(value)].sort_values(["run", "sample"])["sample"].unique().tolist()


########


# Datatable callback
@dash.callback(Output("table-data", "data"), Input("sample-dropdown", "value"))
def create_dataframe(value):
    return df_datatable.loc[df_datatable["sample"].isin(value)].sort_values(by=["run", "sample"]).to_dict("records")


# Barplot callback
@dash.callback(Output("graph-bar", "figure"), Input("sample-dropdown", "value"))
def update_plot(value):
    fig = px.bar(
        barplot_df_mosaic.loc[barplot_df_mosaic["sample"].isin(value)].sort_values(by=["run-sample"]),
        x="run-sample",
        y="count",
        color="prediction_status",
        barmode="stack",
        color_discrete_map={"ashleys + mosaic": "green", "mosaic": "lightgreen", "None": "red"},
        template="none",
        height=500,
    )
    fig.update_xaxes(tickangle=45, tickfont=dict(size=6), ticksuffix="                ", title_text="")
    # fig.update_layout(yaxis_range=[0, 96])
    # print(barplot_df_mosaic.loc[barplot_df_mosaic["sample"].isin(value)].groupby("sample").value_counts().reset_index().groupby("sample")["count"].sum())
    fig.update_layout(
        yaxis_range=[
            0,
            barplot_df_mosaic.loc[barplot_df_mosaic["sample"].isin(value)]
            .groupby("sample")
            .value_counts()
            .reset_index()
            .groupby("sample")["count"]
            .sum(),
        ]
    )
    return fig


# Reads violin
@dash.callback(Output("graph-violin-good", "figure"), Input("sample-dropdown", "value"), Input("radioitems-inline-input", "value"))
def update_plot(value, group):
    final_df_tmp = final_df.loc[(final_df["prediction"] == 1) & (final_df["sample"].isin(value)) & (final_df["good"] < 2e6)].sort_values(
        by=["run-sample"]
    )
    fig = px.violin(
        final_df_tmp,
        x="sample",
        y="good",
        points="all",
        color=group,
        hover_data=["cell"],
        box=True,
        template="none",
    )
    fig.update_xaxes(tickangle=90, tickfont=dict(size=6), ticksuffix="                ", title_text="")
    fig.update_layout(yaxis_range=[0, 1500000])

    return fig


# Duplicates violin
@dash.callback(Output("graph-violin-dupl", "figure"), Input("sample-dropdown", "value"), Input("radioitems-inline-input", "value"))
def update_plot(value, group):
    # final_df_tmp = final_df.loc[~final_df.loc["sample"].isin(samples_to_remove)]
    fig = px.violin(
        final_df.loc[(final_df["prediction"] == 1) & (final_df["sample"].isin(value))].sort_values(by=["run-sample"]),
        x="sample",
        y="%dupl",
        points="all",
        color=group,
        hover_data=["cell"],
        box=True,
        template="none",
    )
    fig.update_xaxes(tickangle=90, tickfont=dict(size=6), ticksuffix="                ", title_text="")
    fig.update_layout(yaxis_range=[0, 100])

    return fig
