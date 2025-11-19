import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

df=px.data.wind()
# ct = pd.crosstab(df["direction"],df["strength"])
# px.imshow(ct).show()

# px.histogram(df, x="direction", color="strength", barnorm="percent").show()

# px.bar(df,x="direction",y="frequency").show()

fig=make_subplots(rows=1,cols=2,subplot_titles=("Histogram","Bar Chart"))
fig.add_trace(go.Histogram(x=df["strength"],marker_color='indianred',name="Histogram"),row=1,col=1)
fig.add_trace(go.Bar(x=df["direction"],y=df["frequency"],marker_color='lightseagreen'),row=1,col=2)
fig.update_layout(title_text="Wind Direction Analysis",showlegend=False)
fig.show()