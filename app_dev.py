from dash import Dash, html, dcc, Input, Output, dash_table
from pathlib import Path
import datetime
import os, sys
import pandas as pd
import plotly.express as px
import scipy
import dash_bootstrap_components as dbc
import dash


# Start the app, use_pages allows to retrieve what's present in the pages/ folder in order
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], use_pages=True)
server = app.server


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.P("Navigation", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Dash home page", href="/", active="exact"),
                # dbc.NavLink("Grafana home page", href="http://localhost:3000", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        # html.Hr(),
        # html.P("Bio-related components", className="lead"),
        # dbc.Nav(
        #     [
        #         dbc.NavLink("Dash-Jbrowse2", href="/jbrowse-example", active="exact"),
        #         dbc.NavLink("Dash-ideogram", href="https://dash.gallery/dash-ideogram/", active="exact"),
        #         dbc.NavLink("Dash-Circos", href="https://dash.gallery/dash-circos/", active="exact"),
        #     ],
        #     vertical=True,
        #     pills=True,
        # ),
        # html.Hr(),
        # html.P("HTML reports integration", className="lead"),
        # dbc.Nav(
        #     [
        #         # dbc.NavLink("Grafana", href="https://play.grafana.org/d/000000012/grafana-play-home?orgId=1", active="exact"),
        #         dbc.NavLink("Snakemake report", href="/snakemake-report", active="exact"),
        #         dbc.NavLink("MultiQC report", href="/multiqc-report", active="exact"),
        #     ],
        #     vertical=True,
        #     pills=True,
        # ),
        # html.Hr(),
        # html.P("Preconfigured Jup NB", className="lead"),
        # dbc.Nav(
        #     [
        #         dbc.NavLink("Jupyter-Notebook", href="http://localhost:5500", active="exact"),
        #     ],
        #     vertical=True,
        #     pills=True,
        # ),
    ],
    style=SIDEBAR_STYLE,
)

print([dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"]) for page in dash.page_registry.values()])
content = html.Div(id="page-content", style=CONTENT_STYLE)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div()
    elif pathname == "/jbrowse-example":
        return html.Div()
    elif pathname == "/grafana":
        return html.Div()
    elif pathname == "/snakemake-report":
        return html.Div()
    elif pathname == "/multiqc-report":
        return html.Div()
    elif pathname == "/datavzrd":
        return html.Div()
    elif pathname == "/jupyter-notebook":
        return html.Div()
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


app.layout = html.Div(
    [
        html.Div([dcc.Location(id="url"), sidebar, content]),
        dash.page_container,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, host="seneca.embl.de", port=5100)
