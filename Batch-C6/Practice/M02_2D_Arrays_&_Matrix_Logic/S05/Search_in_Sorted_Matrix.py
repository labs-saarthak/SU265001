'''
Sorted Matrix Problems
74 - Search a 2D Matrix
240 - Search a 2D Matrix II
378 - Kth Smallest Element in a Sorted Matrix
'''
from typing import List
#Flatten a matrix
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
arr = []
for row in matrix:
    arr += row
print(arr)

#74 - Search a 2D Matrix
#Traditional approach
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    #Flatten matrix
    arr = []
    for row in matrix:
        arr += row
    #Binary search
    left,right = 0,len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(searchMatrix(matrix,target))
# Optimal solution
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m,n = len(matrix),len(matrix[0])
    left,right = 0,m*n-1
    while left <= right:
        mid = (left + right)//2
        row,col = mid // n,mid % n
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            right = mid - 1
        else:
            left = mid + 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))

#240 - Search a 2D Matrix II
def searchMatrixII(matrix: List[List[int]], target: int) -> bool:
    m,n = len(matrix),len(matrix[0])
    r,c = 0,n-1
    while r < m and c >= 0:
        if target == matrix[r][c]:
            return True
        elif target < matrix[r][c]:
            c -= 1
        else:
            r += 1
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrixII(matrix,target))