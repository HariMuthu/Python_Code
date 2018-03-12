import numpy as np

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

r = len(grid)
c = len(grid[0])

inv_grid = [ [ 0 for i in range(c) ] for j in range(r) ]
inv_grid.clear()
for i in range(0,len(grid[0])):
   for j in range(0,r):
       inv_grid.append(grid[j][i])

l = len(inv_grid)
grid_arr = np.array(inv_grid).reshape(c,r)

for i in range(0,r):
 print(grid[i][:])

print('Below is the transpose')

print(grid_arr)
