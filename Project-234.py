import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_csv('E:\\WindowsNoEditor\\PythonAPI\\examples\\premier_league.csv')

goal = data['Goals']
club_sorted = goal.groupby(data['Club'])
goal_sum = club_sorted.sum()
goal_sorted = goal_sum.sort_values(ascending=False)

top_scorer = data.sort_values(ascending=False, by=['Goals'])
top10 = top_scorer[:10]

print(goal_sorted)
print(top10)

fig = px.bar(top10, x='Name', y='Goals', color='Goals', hover_data=['Club', 'Age'], text='Goals') 
fig.show()