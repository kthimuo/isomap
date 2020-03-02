import numpy as np

distance_matrix = np.load('distance_matrix.npy')
print(distance_matrix.shape)

epsilon = 4.2
N = 1000
K = 6


distance_sort_matrix = np.argsort(distance_matrix,axis=1)

#print(distance_sort_matrix)
k_nearest_mask = np.where(distance_sort_matrix < 7,True,False)
epsilon_mask = np.where((distance_matrix < epsilon) & (distance_matrix !=0),True,False)
D_X = np.where(k_nearest_mask + epsilon_mask > 0,distance_matrix,np.inf)

from tqdm import tqdm
D_G = D_X[:200,:200].copy()
for n in tqdm(range(N)):
    for i in range(D_G.shape[0]):
        for j in range(D_G.shape[0]):
            for k in range(D_G.shape[0]):
                D_G[i,j] = min(D_G[i,j],D_G[i,k] + D_G[k,j])












