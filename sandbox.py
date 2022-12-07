from dash import Dash, Input, Output, State, dcc, html

# Added
import flask
import os
from flask import Flask

# Added
server = Flask(__name__)
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=external_stylesheets, server=server)

app.scripts.config.serve_locally = True

app.layout = html.Div(
    [
        # html.A("Navigate to google.com", href="http://google.com", target="_blank"),
        # html.Br(),
        # html.Img(src="/static/chromosome.png")
        html.A("Test", href="/static/HJ_MIXTURE_LITE/report.html")
    ]
)

# Added
@app.server.route("/static/<resource>")
def serve_static(resource):
    return flask.send_from_directory(STATIC_PATH, resource)


# STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# server = Flask(__name__)
# app = dash.Dash(name = __name__, server = server)

# app.layout = html.Div(
#    html.Img(src='/static/your_img.jpeg')
# )

# @app.server.route('/static/<resource>')
# def serve_static(resource):
#     return flask.send_from_directory(STATIC_PATH, resource)

if __name__ == "__main__":
    app.run_server(debug=True, host="seneca.embl.de", port=5500)
