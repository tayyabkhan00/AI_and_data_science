from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H1("My First Dash App"),

    dcc.Graph(
        id="basic-graph",
        figure=px.scatter(px.data.iris(), x="sepal_width", y="petal_length")
    )
])

if __name__ == "__main__":
    app.run(debug=True)

