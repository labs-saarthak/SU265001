from typing import List
def matrixBlockSum(mat: List[List[int]], k: int) -> List[List[int]]:
    m,n = len(mat),len(mat[0])
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r_start = max(0,i-k)
            c_start = max(0,j-k)
            r_end = min(i+k,m-1)
            c_end = min(j+k,n-1)
            for r in range(r_start,r_end+1):
                for c in range(c_start,c_end+1):
                    res[i][j] += mat[r][c]
    return res
mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(matrixBlockSum(mat,k))

