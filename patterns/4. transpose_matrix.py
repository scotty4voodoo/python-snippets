def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("\n".join(",".join(map(str,row)) for row in transpose_matrix(matrix)))