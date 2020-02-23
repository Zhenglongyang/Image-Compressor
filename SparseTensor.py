class SparseTensor:
    def __init__(self, fromiter, shape):
        n, m , o = shape
        self.n = n
        self.m = m
        self.o = o          #3rd coordinate for the Tensor
        self.nnz = 0        # TODO: nombre de valeurs non-nulles
        self.rowptr = []    # liste de taille n + 1 des intervalles des colonnes
        self.colind = []    # liste de taille nnz des indices des valeurs non-nulles
        self.data = []      # liste de taille nnz des valeurs non-nulles

        self.rowtensptr = []  # liste de la taille n des intervalles des colones pour une matrice k


        #Creating sized array for RowPtr
        for i in range(0, n + 1):
            self.rowtensptr.append(0)
        for i in range(0,o):                        #creates entry of tuples for each matrix pages
            self.rowptr.append(self.rowtensptr.copy())
        for i in fromiter:
            self.nnz += 1  # increment the non zero value
            if i[3] != 0:  # check if the value is zero or not
                self.data.append(i[3])  # append the value to the data array
                self.colind.append(i[1])  # append the j column value to the colind array

            if i[0] != n:
                self.rowptr[i[2]][i[0] + 1] += 1  # increment the correct value in rowptr for each row

            else:
                self.rowptr[i[2]][i[0]] += 1  # increment if we're at the end of array

        # summin up each value by previous row
        for i in range(0, len(self.rowptr)):
            for j in range(1,len(self.rowptr[i])):
                self.rowptr[i][j] += self.rowptr[i][j - 1]  # add up the value of the previous index.

        previousElement=self.rowptr[0][n]
        for i in range(1,len(self.rowptr)):
            self.rowptr[i][0]= previousElement
            for j in range(1,len(self.rowptr[i])):
                self.rowptr[i][j] += self.rowptr[i][0]
                previousElement = self.rowptr[i][self.n]


    def printArrays(self):
        print("RowTensPtr: ", self.rowtensptr)
        print("Rowptr: ",  self.rowptr)
        print("Colind: ",  self.colind)
        print("Data: ",  self.data)

    def __getitem__(self, i):
        i, j ,k =  i        # TODO: retourner la valeur correspondant à l'indice (i, j, k)
        # Get row values
        row_start = self.rowptr[k][i]
        row_end = self.rowptr[k][i + 1]
        row_values = self.data[row_start:row_end]

        # Get column indices of occupied values
        index_start = self.rowptr[k][i]
        index_end = self.rowptr[k][i + 1]

        # contains indices of occupied cells at a specific row
        row_indices = list(self.colind[index_start:index_end])

        try:
            # Find a positional index for a specific column index
            value_index = row_indices.index(j)

            if value_index >= 0:
                return row_values[value_index]
            else:
                # non-zero value is not found
                return 0

        except:  # if the item doesn't exist => its a zero
            return 0

    #ADAPTED version for the sparse Tensor.
    def todense(self):      # TODO: encoder la matrice en format dense
        denseRow = [0] * self.n  # Set the numbers of rows
        denseMatrix = [denseRow] * self.m  # Set the number of column
        denseTensor = [denseMatrix] * self.o #Set the number of Matrix

        voidMatrix = [denseRow] * self.m

        rowReduced = self.rowptr.copy()


        previousMatrixIndex=0
        for index in range(0, len(self.rowptr)):
            # Create array of elements per row
            rowElements = self.rowptr[index].copy()
            i = 0
            while i < len(rowElements):
                t = self.rowptr[index].copy()
                t.append(0)
                rowElements[i] = t[i+1]- rowElements[i]
                i += 1
            del rowElements[-1]
            rowReduced[index] = rowElements.copy()

        previousDataIndex = 0
        for k in range(0, len(rowReduced)):
            tMat=voidMatrix.copy()
            for i in range(0, len(rowReduced[k])):
                temp = denseRow.copy()
                for j in range(0, rowReduced[k][i]):
                    col = self.colind[previousDataIndex]  # indicates the column
                    temp[col] = self.data[previousDataIndex]  # temporary value to hold in the data
                    tMat[i] = temp  # add the vector into the Matrix
                    previousDataIndex += 1  # increment counter

            denseTensor[k] = tMat.copy()
        return denseTensor


#mat = SparseTensor(fromiter= [(0,0,0,1),(0,2,0,2),(1,2,0,3),(0,2,1,1),(1,0,1,1),(2,1,1,3),(0,0,2,3),(0,1,2,2),(1,2,2,4)],shape= (3,3,3))
#print(mat.printArrays())
#print(mat.todense())