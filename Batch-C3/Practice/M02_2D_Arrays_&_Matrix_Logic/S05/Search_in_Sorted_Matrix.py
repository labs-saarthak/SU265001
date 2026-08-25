'''
Sorted Matrix Problems
74 - Search a 2D Matrix
240 - Search a 2D Matrix II
378 - Kth Smallest Element in a Sorted Matrix
'''
from typing import List
#Flatten 2D matrix
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
arr = []
for row in matrix:
    arr += row
print(arr)
#74 - Search a 2D Matrix
# Traditional Approach
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    arr = []
    for row in matrix:
        arr += row
    left,right = 0,len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
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

#Optimal approach
def searchMatrix( matrix: List[List[int]], target: int) -> bool:
    m,n = len(matrix),len(matrix[0])
    left,right = 0,m*n- 1
    while left <= right:
        mid = (left + right) // 2
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