print('Transferring file to file')
sname = input('Enter the file name to be copied :')
stext = open(sname)
sdata = stext.read()
tname1 = input('Enter the target file')
tfile = open(tname1,'w')
tfile.truncate()
str = input('Enter the string to be appended : ')
sdata = sdata + '\n' + str
tfile.write(sdata)
stext.close()
tfile.close()