import processor.greedy1 as greedy1
import processor.greedy2 as greedy2
import processor.brute as brute
import processor.greedy3 as greedy3
import itertools
import sys

candidates = [brute,greedy1,greedy3]

def getAllPermut():
    return list(itertools.combinations_with_replacement([1,2,3,4,5,6,7,8,9,10,11,12,13],4))

if __name__ == "__main__":
    same = [0]*len(candidates)
    lose = [0]*len(candidates)
    tempScore = [0] * len(candidates)
    allPermut = getAllPermut()
    for numIn in allPermut:
        for i in range(len(candidates)):
            candidate = candidates[i]
            tempOutput = candidate.calculate(numIn)
            if(candidate.getName()=="Brute"):
                try:
                    bruteResult = eval(tempOutput[1])
                except:
                    bruteResult = 0
                bruteScore = tempOutput[0]
            tempScore[i] = tempScore[i] + tempOutput[0]
            print(candidate.getName()," sol = ",tempOutput[1])
            print(candidate.getName()," scr = ",tempOutput[0])
            if(candidate.getName()!="Brute"):
                try:
                    canResult = eval(tempOutput[1])
                except:
                    canResult = 0
                if(abs(24-bruteResult) < abs(24-canResult)):
                    lose[i] = lose[i]+1
                    print("Kalah")
                elif(abs(24-bruteResult) == abs(24-canResult)):
                    same[i] = same[i]+1
                    print("Selisih same= ",float(tempOutput[0])-float(bruteScore))
                else:
                    print("WOWWW")

                
        print()

    for i in range(len(candidates)):
        print("Score ",candidates[i].getName()," = ",float(tempScore[i])/float(1820))
        print("Same ",candidates[i].getName()," = ",float(same[i]))
        print("Lose ",candidates[i].getName()," = ",float(lose[i]))
        print()