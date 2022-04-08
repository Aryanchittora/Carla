import pandas as pd

data = pd.read_csv('E:\\WindowsNoEditor\\PythonAPI\\examples\\Test\\expenses.csv')
sum = data.sum()

print(data)
print(f'Sum {sum}')