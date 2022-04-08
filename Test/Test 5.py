import pandas as pd

a = [1, 5, 5, 5, 2, 3, 4, 4, 2, 7, 8, 9, 0]
df = pd.DataFrame(a)

print(df)
print(f'\n Duplicate Data - {df.duplicated()}')