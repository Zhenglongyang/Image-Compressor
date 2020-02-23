class SparseMatrix:
    def __init__(self, fromiter, shape):
        n, m = shape
        self.n = n
        self.m = m
        self.nnz = 0 # TODO: nombre de valeurs non-nulles
        self.rowptr = [] # liste de taille n + 1 des intervalles des colonnes
        self.colind = [] # liste de taille nnz des indices des valeurs non-nulles
        self.data = [] # liste de taille nnz des valeurs non-nulles

        #init the data[0] by 0
        # self.data.append(0)

        #create an entry for each row
        for i in range(0, n+1):
            self.rowptr.append(0)

        for i in fromiter:
            self.nnz += 1 #increment the non zero value
            if i[2] != 0: #check if the value is zero
                self.data.append(i[2]) #append the value to the data array
                self.colind.append(i[1]) #append the j column value to the colind array

            if i[0] != n:
                self.rowptr[i[0]+1] += 1 #increment the correct value in rowptr for each row

            else:
                self.rowptr[i[0]] += 1#increment if we're at the end of array

        #summin up each value by previous row
        for i in range(1, len(self.rowptr)):
            self.rowptr[i] += self.rowptr[i-1] #add up the value of the previous index.

    def printArrays(self):
        print("Rowptr: ",  self.rowptr)
        print("Colind: ",  self.colind)
        print("Data: ",  self.data)

    def __getitem__(self, k):
        i, j = k    # TODO: retourner la valeur correspondant à l'indice (i, j)


        # Get row values
        row_start = self.rowptr[i]
        row_end = self.rowptr[i + 1]
        row_values = self.data[row_start:row_end]

        # Get column indices of occupied values
        index_start = self.rowptr[i]
        index_end = self.rowptr[i + 1]

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

        except: #if the item doesn't exist => its a zero
            return 0

    def todense(self):     # TODO: encoder la matrice en format dense
        denseRow = [0] * self.n      #Set the numbers of rows
        denseMatrix = [denseRow] * self. m  #Set the number of column

        #Create array of elements per row
        rowElements = self.rowptr.copy()
        rowElements.pop(0)
        i=0
        while i < len(rowElements):
            rowElements[i] = rowElements[i]- self.rowptr[i]
            i+=1

        #Operations to create the dense Matrix
        previousDataIndex = 0
        for i in range(0, len(rowElements)):
            temp = denseRow.copy()
            for j in range(0, rowElements[i]):
                col = self.colind[previousDataIndex] #indicates the column
                temp[col]=self.data[previousDataIndex]  #temporary value to hold in the data
                denseMatrix[i]=temp                     #add the vector into the Matrix
                previousDataIndex+=1                    #increment counter

        return denseMatrix


#
# fromiter = [(0, 1, 1), (1, 0, 2), (2, 1, 4), (2, 2, 3)]
# shape = (3, 3)
#mat = SparseMatrix(fromiter, shape)
#mat = SparseMatrix(fromiter= [(0, 1, 1), (1, 0, 2), (2, 1, 4), (2, 2, 3)],shape= (3,3))
#mat.printArrays()
#
#
# print(mat.todense())


