#Task
from typing import List
def setZeroes(matrix: List[List[int]]) -> List[List[int]]:
   pass 

if __name__ == '__main__':
   matrix = []
   while True:
      line = input()
      if not line.strip():  
         break
      row = list(map(int, line.split()))
      matrix.append(row)
   print(setZeroes(matrix))
