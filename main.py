import os
import pickle
import time

clear = 'cls'

def writePickle(filename, data):
     with open(filename, 'wb') as f:
         pickle.dump(data, f)

def readPickle(filename): 
    with open(filename, 'rb') as f:
            return pickle.load(f)

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
    bal = int(decrypt(readPickle('database.txt')))
except:
    bal = 0
    writePickle('database.txt', encrypt(bal))
# create database.txt when not avaliable
while True:
    writePickle('database.txt', encrypt(bal))
    print(bal)
    inp = input()
    if inp == '':
        bal += 1
    elif inp == 'reset':
        inpr = input('Are you sure you want to reset? [y/n]: ')
        if inpr == 'y':
            writePickle('database.txt', 'b')
            bal = 0
            print('Succesfully resetted stats!\nPress enter to continue')
            input()
    os.system(clear)