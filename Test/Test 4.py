import pandas as pd

a = {'Cars': ['BMW', 'Tesla']}
b = {'New_Cars': ['Porche', 'Lamborghini', 'Bugati']}

df_a = pd.DataFrame(a)
df_b = pd.DataFrame(b)

new_df = df_a.append(df_b)

print(df_a)
print(df_b)
print(f'\n{new_df}')