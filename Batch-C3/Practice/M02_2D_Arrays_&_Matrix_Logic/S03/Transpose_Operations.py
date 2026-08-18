'''
867. Transpose Matrix
566. Reshape the Matrix
'''
from typing import List
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    '''
    rows,cols = len(matrix),len(matrix[0])
    res = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            res[j][i] = matrix[i][j]
    return res
    '''
    return [list(row) for row in zip(*matrix)]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))