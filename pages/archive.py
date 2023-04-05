import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = dbc.Container(
    [
        html.Div(
            children=[
                html.H1(children="This is our Archive page"),
                html.Div(
                    children="""
        This is our Archive page content.
    """
                ),
            ]
        )
    ],
    fluid=False,
)
