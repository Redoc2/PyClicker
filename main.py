import os
import time
from funcs import *
from vars import *
    
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