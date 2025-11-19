from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = px.data.iris()
app = Dash(__name__)

app.layout = html.Div([
    html.H2("Iris Dashboard"),

    dcc.Dropdown(
        id="x-axis",
        options=[{"label": col, "value": col} for col in df.columns],
        value="sepal_length"
    ),

    dcc.Graph(id="graph")
])


@app.callback(
    Output("graph", "figure"),
    Input("x-axis", "value")
)
def update_graph(x):
    return px.scatter(df, x=x, y="petal_width", color="species")


if __name__ == "__main__":
    app.run(debug=True)
