import os
import time
try:
    l = open('database.txt', 'r')
    bal = int(l.read())
    l.close()
except:
    bal = 0
    with open('database.txt', 'a') as f:
        print(bal, file=f)
# create database.txt when not avaliable
while True:
    os.remove(os.getcwd() + "/database.txt")
    with open('database.txt', 'a') as f:
        print(bal, file=f)
    print(bal)
    inp = input()
    if inp == '':
        bal += 1
    os.system('cls')
    print(bal)