import dash
from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc


dash.register_page(__name__)


layout = dbc.Container(
    [
        html.Div(
            children=[
                html.H2("Snakemake report integration", style={"margin-top": 5}, className="display-4"),
                html.Hr(),
                html.H2("Sample selection:", className="card-title"),
                dcc.Dropdown(
                    # sorted(df_datatable["sample"].unique().tolist()),
                    value=["GM19384x02"],
                    options=[
                        "GM19384x02",
                        "HG2554x02",
                        "HG03452x01",
                        "BoM47Nx02",
                        "ckAML02x03",
                        "BoM66Gx02",
                        "GM19129x02",
                        "ckADOs42hx01",
                        "HG02953x01",
                        "GM21487x01",
                        "HG02554x01",
                        "GM21487x02",
                        "GM19347x01",
                        "HGSVCpool1xulOPxmanual",
                        "HGSVCpool1xulOPxEcho",
                        "KM1096",
                    ],
                    id="sample-dropdown-smk",
                    style={"fontSize": 18, "font-family": "sans-serif"},
                    # multi=True,
                ),
                html.Br(),
                html.Iframe(
                    src=dash.get_asset_url("HGSVC2/report.html"),
                    style={"height": "1067px", "width": "100%"},
                ),
            ]
        )
    ]
)


# @dash.callback(Output("sample-dropdown-smk", "value"), Input("sample-dropdown-smk", "options"))
# def set_sample_value(value):
#     # print(value)
#     # print(df_datatable.loc[df_datatable["sample"].isin(value)].sort_values(["run", "sample"])["sample"].unique().tolist())
#     return value
