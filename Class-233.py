import pandas as pd

data = pd.read_csv('radar_data.csv')

data.loc[data['distance'] <= 17, 'action'] = 1
data.loc[data['distance'] > 17, 'action'] = 2
data.loc[data['steer'] < 0, 'action'] = 0

data.to_csv('radar_data_modified.csv', index=False)

print(data)