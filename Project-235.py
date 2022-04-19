import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_csv('premier_league.csv')

clubs = data['Club'].value_counts().head(20)
print(clubs)

fig = go.Figure(data=[go.Pie(labels=clubs.index, values=clubs.values)])
fig.show()