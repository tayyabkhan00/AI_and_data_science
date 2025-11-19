import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

url = "https://raw.githubusercontent.com/plotly/datasets/master/superstore.csv"

df = pd.read_csv(url, encoding="latin1", parse_dates=["Order Date"])

app = dash.Dash()

app.layout = html.Div([
    html.H1("Superstore Sales Dashboard"),
    
    dcc.Dropdown(
        id="region",
        options=[{"label": r, "value": r} for r in df["Region"].unique()],
        value="West"
    ),

    dcc.Graph(id="sales_trend"),
    dcc.Graph(id="profit_category"),
])

@app.callback(
    [
        dash.dependencies.Output("sales_trend", "figure"),
        dash.dependencies.Output("profit_category", "figure")
    ],
    [dash.dependencies.Input("region", "value")]
)
def update(region):
    dff = df[df["Region"] == region]

    fig1 = px.line(dff, x="Order Date", y="Sales", title="Monthly Sales Trend")
    fig2 = px.bar(dff, x="Category", y="Profit", title="Profit by Category")

    return fig1, fig2

app.run(debug=True)
if __name__ == "__main__":
    app.run_server(debug=True)