import numpy as np            
from scipy.spatial import distance
from scipy.spatial import distance_matrix
from scipy.spatial.distance import euclidean
from scipy.spatial import distance

data = np.load('data/digit2.npy')
sample_size = data.shape[0]
image_size = data.shape[1]

data = data.reshape(sample_size,image_size*image_size)
print(data.shape)
print(data[0].shape)

def Euclidean_distance(x,y,p=2):
    x = x.reshape(1,-1)
    y = y.reshape(1,-1)
    return distance_matrix(x,y,p=p)

import time

start = time.time()
distance_matrix = distance.cdist(data,data,metric='euclidean')
print(distance_matrix)
end = time.time()
print(end-start)


np.save('distance_matrix.npy',distance_matrix)


