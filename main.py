import os
import time

clear = 'cls'

def write(name, x, val):
    os.remove(os.getcwd() + "/database.txt")
    test = open(name, x)
    print(val, file=test)
    test.close()

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
    write('database.txt', 'a', encrypt(bal))
# create database.txt when not avaliable
while True:
    write('database.txt', 'a', encrypt(bal))
    print(bal)
    inp = input()
    if inp == '':
        bal += 1
    elif inp == 'reset':
        inpr = input('Are you sure you want to reset? [y/n]: ')
        if inpr == 'y':
            write('database.txt', 'a', 'f', 'b')
            bal = 0
            print('Succesfully resetted stats!\nPress enter to continue')
            input()
    os.system(clear)