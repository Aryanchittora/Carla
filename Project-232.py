import numpy as np
from keras.models import Sequential
from keras.layers import Dense

data = np.loadtxt('pokemon.csv', delimiter=',')
x = data[:, 1:7]
y = data[:, 7]

model = Sequential()
model.add(Dense(12, input_dim=6, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=250, batch_size=100)
predictions = model.predict(x)

for i in range(5):
    print(f'{x[i].tolist()} => {predictions[i]} expected {y[i]}')