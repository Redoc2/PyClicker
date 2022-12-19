import os
import time
def remove():
    try:
        os.remove(os.getcwd() + "/database.txt")
        return 'Success'
    except:
        return 'Failed'
def write(name, x, x2, val):
    with open(name, x) as x2:
        print(val, file=x2)

def encrypt(value):
    enc = ['b','d','K','O','Z','p','j','u','T','a']
    ret = ''
    list = [item for item in str(value)]
    for lett in list:
        ret += f'{enc[int(lett)]}'
    return ret

def decrypt(value):
    enc = ['b','d','K','O','Z','p','j','u','T','a']
    ret = ''
    list = [item for item in value]
    for item in list:
        val = 0
        while enc[val] != item:
            val +=1
        ret += str(val)
        val = 0
    return ret
    
try:
    l = open('database.txt', 'r')
    bal = int(decrypt(l.read()))
    l.close()
except:
    bal = 0
    with open('database.txt', 'a') as f:
        print(encrypt(bal), file=f)
# create database.txt when not avaliable
while True:
    print(remove())
    write('database.txt', 'a', 'f', encrypt(bal))
    print(bal)
    inp = input()
    if inp == '':
        bal += 1
    elif inp == 'reset':
        inpr = input('Are you sure you want to reset? [y/n]: ')
        if inpr == 'y':
            remove()
            write('database.txt', 'a', 'f', 0)
            bal = 0
            print('Succesfully resetted stats!\nPress enter to continue')
            input()
    elif inp == 'test':
        os.remove(os.getcwd() + "/database.txt")
    os.system('cls')