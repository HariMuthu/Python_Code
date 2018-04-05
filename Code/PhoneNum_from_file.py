#To get the phone number from a file

#function to find the phone number from the file
def getphonenum(filetext):
 num_pattern = re.compile(r'XX\D{4}.*?\s\W\s\d{3}-\d{3}-\d{3}')
 phone_num = num_pattern.findall(filetext)
 dictn = { k[2:]:v for k,v in(x.split(':') for x in phone_num)} 
 #return phone_num
 return dictn
 
##Main program

import re
filename = input(r'Enter the phone directory location :')
phonefile = open(filename ,'r')
a = phonefile.read()
print(a)
out_num = getphonenum(a)
print('Phone numbers in the file', out_num)
phonefile.close()

