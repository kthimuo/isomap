from keras.datasets import mnist
import numpy as np

(x_train,y_train),(x_test,y_test) = mnist.load_data()
labels2_indexs = [i for i,label in enumerate(y_train) if label==2]
data = x_train[labels2_indexs]

np.save('data/digit2.npy',data)




