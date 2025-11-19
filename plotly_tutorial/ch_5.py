import plotly.express as px
import pandas as pd

df = px.data.iris()

# Scatter Plot
fig1 = px.scatter(df, x="sepal_length", y="petal_length", color="species",
                  title="Sepal vs Petal Length")
fig1.show()

# Box Plot
fig2 = px.box(df, x="species", y="petal_length", title="Petal Length by Species")
fig2.show()

# Histogram
fig3 = px.histogram(df, x="sepal_width", color="species", nbins=20,
                    title="Distribution of Sepal Width")
fig3.show()

# Scatter Matrix
fig4 = px.scatter_matrix(df, dimensions=df.columns[:4], color="species",
                         title="Pair Plot of All Iris Features")
fig4.show()
