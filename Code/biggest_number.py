##This program finds the biggest number

print(' To find the biggest number ')
a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))
c = int(input('Enter the third number : '))
if a > b :
  if a > c :
     print ( '%d is the biggest number' % a)
  else:
     print ( '%d is the biggest number' % c)
elif b > c :
     print ( '%d is the biggest number' % b)
else:
  print ( '%d is the biggest number' % c)	 
