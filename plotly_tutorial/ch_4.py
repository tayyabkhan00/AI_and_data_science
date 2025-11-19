import plotly.express as px
import pandas as pd
import statsmodels.api as sm

df = px.data.iris()
df.head(1)

# px.scatter(df, x="sepal_length", y="petal_length", color="species", facet_col="species").show()

# px.scatter(
    # df, x="sepal_length", y="petal_length", color="species",
    # trendline="ols"
# ).show()

# px.scatter_polar(df, r="sepal_length", theta="species", color="species").show()

# df_long = pd.melt(df, id_vars=["species"], value_vars=["sepal_length", "sepal_width", "petal_length", "petal_width"])
# px.box(df_long, x="variable", y="value", color="species").show()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
nums = scaler.fit_transform(df[['sepal_length','petal_length','petal_width']])
df[["A","B","C"]] = nums

px.scatter_ternary(df, a="A", b="B", c="C", color="species").show()
