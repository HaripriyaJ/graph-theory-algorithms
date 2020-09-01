import numpy as np
from numpy import *

matrix =list()
n = int(input("Enter the number of vertices: "))

# Creating a nxn Adjancency Matrix
for i in range(n):
	row=list()
	for j in range(n):
		print("Insert 1 if you want an edge btw",(i+1,j+1),"and 0 if no ")
		item=int(input())
		row.append(item)
	matrix.append(row) 
print ("Adjacency matrix of the Graph is :\n")
arr=reshape(matrix,(n,n))
print (arr)

i=0

# Perform fusion for n-1 vertices
while i < n-1:
        c = len(matrix)
        j = 0
        while j < n and c > 1:
                if matrix[i][j] > 0 :
			
                        for k in range(n):
                                matrix[i][k] = matrix[i][k] or matrix[j][k]   # rows are logical or-ed
				
                        for k in range(n):
                                matrix[k][i] = matrix[k][i] or matrix[k][j]  # columns are logical or-ed
				
                        # delete column and row of vertices fused
                        matrix = np.delete(matrix, (j), axis=0)  # axis = 0 implies row deletion 
                        matrix = np.delete(matrix, (j), axis=1)  # axis=1 implies column deletion 
                        print("\nAfter Fusion:\n", matrix);
                        n = n-1
                else :
                        print("\nNO EDGE!")
                        print("\n", matrix)
                        j = j+1
        i += 1
c = len(matrix);
print("\nNumber of components: ", c);
