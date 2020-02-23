import numpy as np
import matplotlib.pyplot as plt
import SparseMatrix
import SparseTensor
import sys

mnist_dataset =np.memmap('train-images-idx3-ubyte', offset=16, shape=(60000,28,28))
first_image = mnist_dataset[0].tolist()

#Converts Bitmaps into Arrays of vectors under the form of coordinates (Ignore 0s)
def ConvertBitmapToCoordinate(bitmap=None):
    coordinate=[]
    for i in range(0, len(bitmap)):
        for j in range(0, len(bitmap[i])):
            if bitmap[i][j] > 0:
                vector = (i,j,bitmap[i][j])
                coordinate.append(vector)

    return coordinate
#Converts the dataset into a string of coordinates
def convertBitmapToCoordinateTensor(dataset=None):
    coordinate=[]
    for k in range(0, len(mnist_dataset)):
        image = mnist_dataset[k].tolist()
        for i in range(0, len(image)):
            for j in range(0, len(image[i])):
                if image[i][j] > 0:
                    vector = (i,j,k,image[i][j])
                    coordinate.append(vector)
    return coordinate


# # #Tests          Uncomment for testing
# for i in range(0,len(mnist_dataset)):
#      image = mnist_dataset[i].tolist()
#      matrix = SparseMatrix.SparseMatrix(fromiter= ConvertBitmapToCoordinate(image), shape= (28,28))
#      assert matrix.todense() == image
#      print(True)



# matTest = SparseTensor.SparseTensor(fromiter=convertBitmapToCoordinateTensor(mnist_dataset), shape=(28, 28, 60000))
# print("SparseTensorLoaded")
# f=matTest.todense()
# print("to dense converted")
# for i in range(len(f)):
#     assert f[i] == f[i+1]
#     print("tested ",i )



#test for Tensor    Uncomment for testing
# mat = SparseTensor.SparseTensor(fromiter=convertBitmapToCoordinateTensor(mnist_dataset), shape=(28, 28, 60000))
# print("SparseTensorLoaded")
# f=mat.todense()
# for i in range(0,len(mnist_dataset)):
#      assert f[i] == mnist_dataset[i].tolist()
#      print("Assert Succcess # ",i)