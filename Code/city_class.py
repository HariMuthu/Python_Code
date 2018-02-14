class city_abbr:
    def __init__(self, cabbr, cname):
       self.ca = [cabbr for cabbr in cabbr.split(' ')]
       self.cn = [cname for cname in cname.split(' ')] 
	
    def city_print(self):
         inp_name = input('Enter the city abbr you need : ')
         i = self.ca.index(inp_name)
         print('City name is ', self.cn[i])	