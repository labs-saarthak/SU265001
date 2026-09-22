from typing import List
def diagonalBoundarySum(arr):
    pass

if __name__ == '__main__':
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    print(diagonalBoundarySum(mat))