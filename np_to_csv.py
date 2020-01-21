
# saving numpy array as csv
import numpy as np  

data = np.asarray([[0,1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1,0]])
np.savetxt('output/data.csv', data, delimiter=',')

data = np.loadtxt('output/data.csv', delimiter=',')
print(data)

# saving numpy array as native binary format for efficient storage
np.save('output/data.npy', data)
data_from_npy = np.load('output/data.npy')
print(data_from_npy)

# saving large numpy array as compressed native numpy file
np.savez_compressed('output/data.npz', data)
data_from_npz = np.load('output/data.npz')
print(data_from_npz)
