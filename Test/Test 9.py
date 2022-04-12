import pandas as pd

df = pd.read_csv('E:\\WindowsNoEditor\\PythonAPI\\examples\\Test\\expenses.csv')

print(f'Data on 1st Index - {df.loc[1]}')