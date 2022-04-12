import pandas as pd

data = pd.read_csv('student_data.csv')

data['Total_marks_obtained'] = data.iloc[:, [2, 3, 4]].sum(axis=1)
data.loc[data['Total_marks_obtained'] > 250, 'Grade'] = 'A'
data.loc[data['Total_marks_obtained'] < 250, 'Grade'] = 'B'
data['Percentage'] = data['Total_marks_obtained'] / data['Overall_Total'] * 100

print(data)