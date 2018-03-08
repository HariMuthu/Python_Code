grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

#inv_grid = list(9,6)
print (grid[1][:], len(grid), len(grid[0]))
r = len(grid)
c = len(grid[0])

inv_grid = [[0] * r] * c

print (inv_grid[1][:], len(inv_grid), len(inv_grid[0]))


for i in range(0,r):
   for j in range(0,len(grid[i])):
       inv_grid[i][j] = grid[j][i]

l = len(inv_grid)

for i in range(0,l):
   for j in range(0,len(inv_grid[i])):
        print(inv_grid[i][j],end = ' ')
   print('')
