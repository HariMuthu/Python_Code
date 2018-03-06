def collatz(inp):
    if inp % 2 == 0 :
        out = inp // 2
    else:
        out = 3 * inp + 1
    return int(out)


print('Input should be Number. Press 2 to exit')
while True:
    p = int(input('Enter the value : '))
    o = collatz(p)
    print('Collatz Series : ', o)
    if o == 1 :
        print('You pressed 2.So I am quitting')
        break
    
    
    
    
