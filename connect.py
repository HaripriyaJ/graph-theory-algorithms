import numpy as np
from numpy import *
matrix =list()
n=int(input("Enter the number of vertices: "))
#creating a nxn matrix
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
while i<n:
        c=len(matrix);
        j=0
        while j<n and c>1:
                if matrix[i][j]>0 :
                        for k in range(n):
                        #rows are logical or-ed
                                matrix[i][k]= matrix[i][k] or matrix[j][k]
                        for k in range(n):
                        #columns are logical or-ed
                                matrix[k][i]=matrix[k][i] or matrix[k][j]
                        #delete column and row of vertices fused
                        #axis=0 implies row deletion and axis=1 column deletion
                        matrix=np.delete(matrix,(j),axis=0) 
                        matrix=np.delete(matrix,(j),axis=1) 
                        print("\nAfter Fusion:\n");
                        print (matrix)
                        n=n-1
                else :
                        print("\nNO EDGE!")
                        print("\n",matrix)
                        j=j+1
        i=i+1
c=len(matrix);
print("\nNumber of components: ",c);
