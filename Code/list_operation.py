fruits = input('Enter the name of fruits you like : ')
flist = fruits.split(' ')
masterlist = ['apple', 'banana']
while (len(flist) != 0):
    fpoped = flist.pop()
    masterlist.append(fpoped)
    print ('Fruit poped from basket is ', fpoped)
print('All fruits popped from the basket ' + '\n' + 'Fruits in the master list : ' , masterlist)
print('masterlist[0] : ', masterlist[0])
print('popped from master : ', masterlist.pop())

