import pprint
print('The Layout with grid position. Players should only use the below grid position while playing','\n')
print(' TL ','|',' TM ','|',' TR ')
print('----','|','----','|','----')
print(' ML ','|',' MM ','|',' MR ')
print('----','|','----','|','----')
print(' DL ','|',' DM ','|',' DR ')

tic_tac = {'TL':' ','TM':' ','TR':' ','ML':' ','MM':' ','MR':' ','DL':' ','DM':' ','DR':' '}

print('Players should enter grid position they want to lock','\n')
print('Player 1\'s character is 0')
print('Player 2\'s character is X', '\n')
##pprint.pprint(tic_tac['TL'])
for i in range(1,10):
  if i % 2 != 0:
    print('Player 1\'s turn')
    grid = input('Enter the grid position : ')
    #print(grid)
    #print(tic_tac.get(grid, 2))
    if str(tic_tac.get(grid, 2)) == '2' or tic_tac[grid] != ' ':
        print('You have entered the invalid grid position')
        while True:
            grid = input('Enter the correct grid position : ')
            if str(tic_tac.get(grid, 2)) != '2' :
                if tic_tac[grid] == ' ':
                   break
                
    tic_tac[grid] = '0'
  else: 
    print('\n','Player 2\'s turn',sep='')
    grid = input('Enter the grid position : ')
    if str(tic_tac.get(grid, 2)) == '2' or tic_tac[grid] != ' ':
        print('You have entered the invalid grid position')
        while True:
            grid = input('Enter the correct grid position : ')
            if str(tic_tac.get(grid, 2)) != '2':
                if tic_tac[grid] == ' ':
                   break
                
    tic_tac[grid] = 'X'
  print('\n','Now the board is ','\n',sep='') 
  print(tic_tac['TL'],'|',tic_tac['TM'],'|',tic_tac['TR'])
  print('--','|','---','|','--',sep='')
  print(tic_tac['ML'],'|',tic_tac['MM'],'|',tic_tac['MR'])
  print('--','|','---','|','--',sep='')
  print(tic_tac['DL'],'|',tic_tac['DM'],'|',tic_tac['DR'])
  if (tic_tac['TL'] == tic_tac['TM'] == tic_tac['TR'] == '0') or (tic_tac['ML'] == tic_tac['MM'] == tic_tac['MR'] == '0') or (tic_tac['DL'] == tic_tac['DM'] == tic_tac['DR'] == '0') or (tic_tac['TL'] == tic_tac['DL'] == tic_tac['ML'] == '0') or (tic_tac['TM'] == tic_tac['MM'] == tic_tac['DM'] == '0') or (tic_tac['TR'] == tic_tac['MR'] == tic_tac['DR'] == '0') or (tic_tac['TL'] == tic_tac['MM'] == tic_tac['DR'] == '0') or (tic_tac['TR'] == tic_tac['MM'] == tic_tac['DL'] == '0'):
     print('Player 1 Wins')
     break
  if (tic_tac['TL'] == tic_tac['TM'] == tic_tac['TR'] == 'X') or (tic_tac['ML'] == tic_tac['MM'] == tic_tac['MR'] == 'X') or (tic_tac['DL'] == tic_tac['DM'] == tic_tac['DR'] == 'X') or (tic_tac['TL'] == tic_tac['DL'] == tic_tac['ML'] == 'X') or (tic_tac['TM'] == tic_tac['MM'] == tic_tac['DM'] == 'X') or (tic_tac['TR'] == tic_tac['MR'] == tic_tac['DR'] == 'X') or (tic_tac['TL'] == tic_tac['MM'] == tic_tac['DR'] == 'X') or (tic_tac['TR'] == tic_tac['MM'] == tic_tac['DL'] == 'X'):
     print('Player 2 Wins')
     break
    
    
    

