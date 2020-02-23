# Image-Compressor
An Image Compressor Algorithm for parsing large list of images


This is A typical multi-dimensional array requires Θ(𝑑) of space where 𝑑 is the number of dimensions. For many
applications such as graph encoding or word embedding, the number of used entries is very small with respect
to the allocated space.
To address this issue, there exist a variety of sparse coding. In this assignment, we will explore the columnsparse-row encoding also known as Yale’s encoding.
For example, the following matrix:

[[0, 1, 0],
[2, 0, 0],
[0, 4, 3]]

is encoded as follow:
n = 3
m = 3
nnz = 4
rowptr = [0, 1, 2, 4]
colind = [1, 0, 1, 2]
data = [1, 2, 4, 3]
n, m et nnz respectively correspond to the number of lines, columns and non-zero entries of the matrix.

Within this repository you will find the the implementation of the encoding.