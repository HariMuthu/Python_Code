import NumPy as np

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

##inv_grid = [[0] * r] * c
#inv_grid.clear()

#print (inv_grid[1][:], len(inv_grid), len(inv_grid[0]))

inv_grid = [ [ 0 for i in range(c) ] for j in range(r) ]
inv_grid.clear()
for i in range(0,r):
   for j in range(0,len(grid[i])):
       #inv_grid[j][i] = grid[i][j]
      inv_grid.append(grid[i][j])
   #print(inv_grid[j][i], '  ', grid[i][j],' | ', end = ' ')
 #  print('')
  # print(inv_grid[:][:])

##print(inv_grid[:][:])
l = len(inv_grid)
grid_arr = array(inv_grid)

#print(inv_grid[3][1])
##for a in range(0,l):
##   for b in range(0,len(inv_grid[a])):
##        print(inv_grid[a][b],end = ' ')
##   print('')
print(inv_grid[8])
