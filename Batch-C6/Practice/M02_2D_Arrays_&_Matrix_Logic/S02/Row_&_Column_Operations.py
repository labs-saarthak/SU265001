from typing import List
def countNegatives(grid: List[List[int]]) -> int:
        '''
        count = 0
        for row in grid:
            for ele in row:
                if ele < 0:
                    count += 1
        return count
        '''
        count = 0
        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    count += (cols - c)
                    break
        return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))

#832 – Flipping an Image
def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for row in image:
        row.reverse()
        for i in range(len(row)):
            '''
            if row[i] == 0:
                row[i] = 1
            else:
                row[i] = 0
            '''
            #row[i] = 1 if row[i] == 0 else 0
            row[i] = 1 - row[i]
    return image
image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))