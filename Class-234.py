import pandas as pd
from sklearn.neural_network import MLPClassifier

df = pd.read_csv('radar_data_modified.csv')

x = df.iloc[: ,[2, 4]].values
y = df.iloc[:, 5].values

model = MLPClassifier(
    hidden_layer_sizes = (20),
    batch_size = 200,
    activation = 'relu',
    random_state = 5,
    learning_rate_init = 0.03,
)

model.fit(x, y)
predictions = model.predict(x)

print(f'Predicted Data - {predictions}')