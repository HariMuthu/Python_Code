#Finding the biggest number in the list
a = [int(a) for a in input('Enter the list of number : ').split()]
print(a)
l = len(a)
#print('L : ', l)
for i in range(0,l):
  #print('\n' , a[i])
  for j in range(i+1,l):
 #     print( 'j : ', j , '\n a[j] : ', a[j])
 #     b = j
      if a[i] < a[j]:
         break
      else:
         continue
  else:
    if i < (l-1):
       print(a[i], 'is big')
       break
    else:  
      print(a[i], 'is big')

print('Finding the biggest number in different way')
b = [int(b) for b in input('Enter another set of numbers : ').split()]
max=0
for i in b:
   if i > max:
     max = i
print(max, ' is a maximum number')
