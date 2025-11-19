import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

df = px.data.iris()

app = dash.Dash()

app.layout = html.Div([
    html.H1("Iris Dashboard"),

    dcc.Dropdown(
        id="feature",
        options=[{"label": col, "value": col} for col in df.columns[:4]],
        value="sepal_length"
    ),

    dcc.Graph(id="graph")
])

@app.callback(
    dash.dependencies.Output("graph", "figure"),
    [dash.dependencies.Input("feature", "value")]
)
def update_graph(feature):
    fig = px.histogram(df, x=feature, color="species")
    return fig

app.run(debug=True)
