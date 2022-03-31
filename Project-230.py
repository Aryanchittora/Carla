import pandas as pd

# Dataset
data = pd.read_csv(r'country_vaccinations.csv')

# Printing The Data
print('Shape of Data -',data.shape)
print('Number of Columns -', len(data.columns))
print('Number of NaN Values -', data.loc[:, data.isna().any()])