import os
import random
import string

def randomString(stringLength=2):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

l = ['o','k','ñ','.','l']
s = ['w','a','s','d','x']

r = ['4','e','r','t','f']
m = ['j','n','m',',']

comandos = ['ls','rm']
while True:
    comando = input(">>>")
    #print(repr(comando))
    if comando == '':
        pass
    elif(comando == 'file'):
        os.system("type NUL > " + randomString()+".txt")
    elif(comando == "ex" or comando == "exit"):
        print("Adios :D")
        break
    else:
        if comando[:2] in comandos:
            if((comando[0] in l or comando[0] in s) and (comando[1] in l or comando[1] in s)):
                os.system("dir")
            elif((comando[0] in r or comando[0] in m) and (comando[1] in r or comando[1] in m)):
                #print("del")
                print(os.system("del"+comando[2::]))
        else:
            if((comando[0] in l or comando[0] in s) and (comando[1] in l or comando[1] in s)):
                res = input("Did you mean ls ? (Y/N)")
                if(res == 'Y' or res == 'y'):
                    comandos.append(comando)                    
                    os.system("dir")
                