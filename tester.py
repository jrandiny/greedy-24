import processor.greedy1 as greedy1
import processor.greedy2 as greedy2
import processor.brute as brute
import itertools
import sys
import random

candidates = [brute,greedy1, greedy2]
loop = 10000

def get4Number():
    return list(itertools.combinations_with_replacement([1,2,3,4,5,6,7,8,9,10,11,12,13],4))
# [random.randint(0,17159)]
if __name__ == "__main__":
    if len(sys.argv)>1:
        if sys.argv[1].isnumeric():
            loop = int(sys.argv[1])

    tempScore = [0] * len(candidates)
    for _ in range(loop):
        numIn = get4Number()
        print(numIn)
        
        for i in range(len(candidates)):
            candidate = candidates[i]
            tempOutput = candidate.calculate(numIn)
            if(candidate.getName()=="Brute"):
                bruteScore = tempOutput[0]
            tempScore[i] = tempScore[i] + tempOutput[0]
            print(candidate.getName()," sol = ",tempOutput[1])
            print(candidate.getName()," scr = ",tempOutput[0])
            if(candidate.getName()!="Brute"):
                print("Selisih = ",float(tempOutput[0])-float(bruteScore))
        print()

    for i in range(len(candidates)):
        print("Score ",candidates[i].getName()," = ",float(tempScore[i])/float(loop))