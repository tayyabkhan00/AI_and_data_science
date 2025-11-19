from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = px.data.gapminder()
app = Dash(__name__)

app.layout = html.Div(style={"padding": "20px"}, children=[
    html.H1("Gapminder Dashboard"),

    dcc.Dropdown(
        id="year",
        value=2007,
        options=[{"label": y, "value": y} for y in df["year"].unique()]
    ),

    dcc.Graph(id="graph")
])


@app.callback(
    Output("graph", "figure"),
    Input("year", "value")
)
def update(year):
    dff = df[df["year"] == year]
    fig = px.scatter(
        dff, 
        x="gdpPercap", 
        y="lifeExp",
        size="pop", 
        color="continent",
        log_x=True
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
