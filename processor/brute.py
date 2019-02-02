import itertools
import time
import utils

def getName():
    return "Brute"

def getSymbol(sign):
    if sign == 1:
        return '+'
    elif sign == 2:
        return '-'
    elif sign == 3:
        return '*'
    else:
        return '/'

def calculate(param):
    num = list(param)

    number_permut = list(itertools.permutations(num))
    sign_permut = list(itertools.product([1,2,3,4],repeat=3)) # + - * /
    listskor = []
    listexpr = []

    for num in number_permut:
        for sign in sign_permut:
            expr = "{:.0f}{}{:.0f}{}{:.0f}{}{:.0f}".format(num[0],getSymbol(sign[0]),num[1],getSymbol(sign[1]),num[2],getSymbol(sign[2]),num[3])
            listexpr.append(expr)
            listskor.append(utils.countScore(expr))
            
    maxidx = 0
    for i in range (len(listskor)):
      if (listskor[i]>listskor[maxidx]):
        maxidx = i

    return [listskor[maxidx],listexpr[maxidx]]
