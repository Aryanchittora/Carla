import pandas as pd
from sklearn.neural_network import MLPClassifier

dataset = pd.read_csv('radar_data_modified.csv')

x = dataset.iloc[:, [2, 4]].values # input
y = dataset.iloc[:, 5].values # output

model = MLPClassifier(
    hidden_layer_sizes = (40),
    random_state=5, 
    activation='relu', 
    batch_size = 500, 
    learning_rate_init = 0.1
) 

model.fit(x, y)

#prediction
predictions = model.predict(x)
print("Predicated data:",predictions)
