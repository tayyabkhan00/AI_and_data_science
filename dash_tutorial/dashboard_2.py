import dash
from dash import html, dcc
import plotly.express as px

df = px.data.iris()

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(df.columns[:4], id="feature", value="sepal_length"),
    dcc.Graph(id="graph")
])

@app.callback(
    dash.dependencies.Output("graph", "figure"),
    [dash.dependencies.Input("feature", "value")]
)
def update_graph(feature):
    return px.histogram(df, x=feature, color="species")

app.run(debug=True)
if __name__ == "__main__":
    app.run_server(debug=True)