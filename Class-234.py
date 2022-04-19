import pandas as pd
import pickle
from keras.models import model_from_json
from sklearn.neural_network import MLPClassifier

df = pd.read_csv('new_radar_distance_data.csv')

x = df.iloc[:, [2, 4]].values
y = df.iloc[:, 5].values

model = MLPClassifier(
    hidden_layer_sizes = (20),
    random_state = 5,
    activation = 'relu',
    batch_size = 200,
    learning_rate_init = 0.03,
)

model.fit(x, y)
predictions = model.predict(x)

with open("model.pkl", 'wb') as file:
    pickle.dump(model, file)

with open('model.pkl', 'rb') as file:
    saved_model = pickle.load(file)

car_data = {
    'throttle':[5.5534],
    'steer':[-0.68],
    'distance':[22.2192192]
}
data = pd.DataFrame(car_data, columns=['throttle', 'distance'])

data_predict = saved_model.predict(data)

print('Car Data Predictions', data_predict)