from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

dataset = loadtxt('diabetes_dataset.csv', delimiter=',')
x = dataset[:,0:8]
y = dataset[:,8]

print('The Value Of X -', x)
print('The Value Of Y -', y)