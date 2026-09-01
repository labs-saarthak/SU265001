def diagonalSort(mat):
   pass
if __name__ == '__main__':
   m, n = map(int, input().split())
   mat = []
   for i in range(m):
      mat.append(list(map(int, input().split())))
   print(diagonalSort(mat))
