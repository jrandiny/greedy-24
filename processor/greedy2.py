import math
import utils

def getName():
    return "Willy Greedy"

def calculate(param):
    input = list(param)
    listoperations = []     #list kombinasi operasi
    listnumbers = input
    num = []
    
    listnumbers.sort(reverse=True)      #integer urutan angka

    for i in range(4):
        num.append(str(listnumbers[i]))
    
    i=0
    target = 24
    cek = True
    while (i<3):
        m = listnumbers[i]
        n = listnumbers[i+1]
        if (target>=0):
            if(m <= ((math.sqrt(target))) and n!=1):           
                if (n!=1):
                    listoperations.append('*')
                    listnumbers[i+1] = (m*n)
                else:
                    listoperations.append('+')
                    if(cek==True):                                                                
                        target = target -m-n
                    else:
                        target = target -n
                    cek = False
            else:
                listoperations.append('+')
                if(cek==True):                                                                
                    target = target -m-n
                else:
                    target = target -n
                cek = False
        else:
            listoperations.append('-')
            if(cek==True):                                                                
                target = target -m+n
            else:
                target = target +n
            cek = False
        i = i+1

    listoperations.append('')
    data = list(zip(num,listoperations))
    for k in range(len(data)):
        data[k] = ''.join(data[k])
    data = ''.join(data)

    return [utils.countScore(data),data]