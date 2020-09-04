import numpy as np
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Algorithm: Connectedness and Components'.upper())
print('----------------------------------------')

n = int(input("Enter the number of vertices: "))
vertices = list(alphabets[:n])
print('Vertices in the graph:', vertices, "\n")

# Creating a nxn Adjancency Matrix
adj_matrix = np.zeros((n,n))

# Get input of lower triangular and fill the upper
for i in range(n):
    for j in range(n):
        if i > j:  
            print('Edge between (', vertices[i], ',', vertices[j], ') ? (1-Yes, 0-No): ')
            adj_matrix[i][j] = int(input())
            adj_matrix[j][i] = adj_matrix[i][j]
            
print('\nAdjacency Matrix:\n', adj_matrix)


n_components = []

# Perform fusion for n-1 vertices
i = 0
while i < n-1:
    
    component_vertices = set()
    component_vertices.add(vertices[i])
    
    c = len(adj_matrix)
    j = 0
    
    while j < n and c > 1:

        # Edge exists
        if adj_matrix[i][j] > 0 :  
            
            component_vertices.add(vertices[j])  
            vertices.remove(vertices[j])  # Remove added vertex
            
            for k in range(n):
                adj_matrix[i][k] = adj_matrix[i][k] or adj_matrix[j][k]   # rows are logical or-ed

            for k in range(n):
                adj_matrix[k][i] = adj_matrix[k][i] or adj_matrix[k][j]  # columns are logical or-ed

            # delete column and row of vertices fused
            adj_matrix = np.delete(adj_matrix, (j), axis=0)  # axis = 0 implies row deletion 
            adj_matrix = np.delete(adj_matrix, (j), axis=1)  # axis=1 implies column deletion 
        
            print("\nMatrix After Fusion:\n", adj_matrix)
            n = n-1  
            
        else:
            j = j+1
 
    i += 1
    n_components.append(component_vertices)
    

c = len(adj_matrix)
print("\nNumber of components: ", c)

# Add disconnected points to component list
for disjoint_pt in vertices[len(n_components):]:
    n_components.append(set(disjoint_pt))

print('\nThe Following are the Components:'.upper())
for index in range(len(n_components)):
    print('Component:', index, ' ', n_components[index])
