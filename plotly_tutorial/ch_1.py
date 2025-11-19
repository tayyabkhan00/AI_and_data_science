import plotly.express as px

# df = px.data.iris()  # built-in dataset
#fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
#fig.show()

# fig = px.pie(df, names="species")
# fig.show()


import pandas as pd

# Sample sales data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Revenue": [12000, 15000, 17000, 16000, 18000]
}

df = pd.DataFrame(data)

# fig = px.bar(df, x="Month", y="Revenue", title="Monthly Revenue")
# fig.show()

# fig.update_layout(
    # title="Monthly Revenue",
    # xaxis_title="Month",
    # yaxis_title="Revenue ($)",
    # template="plotly_dark"
# )
# fig.show()


from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Bar(x=df["Month"], y=df["Revenue"]), row=1, col=1)
fig.add_trace(
    go.Scatter(x=df["Month"], y=df["Revenue"],mode='lines'),
    row=1, col=2
    )

fig.show()
