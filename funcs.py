import pickle
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