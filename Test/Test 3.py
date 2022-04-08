import pandas as pd

a = {'Products': [1, 7, 5]}
b = {'Calories': [43, 566, 123]}

a_df = pd.DataFrame(a)
b_df = pd.DataFrame(b)

data = pd.concat([a_df, b_df], join='inner', axis=1)

print(a_df)
print(b_df)
print(f'\n {data}')