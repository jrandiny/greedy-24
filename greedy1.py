import utils

def getName():
    return "Josh Greedy"

def calculate(param):
    input = list(param)

    input.sort(reverse=True)
    
    # result = input[0]
    tempExpr = str(input[0]) 
    maxExpr = tempExpr

    for i in range(1,4):
        tempMax = "empty"
        for opr in ['+','-','*','/']:
            tempExpr = maxExpr
            tempExpr = tempExpr+opr
            tempExpr = tempExpr+str(input[i])
            tempScore = utils.countScore(tempExpr)

            if(tempMax == "empty"):
                tempMax = tempExpr

            if(tempScore>=utils.countScore(tempMax)):
                tempMax = tempExpr
        maxExpr = tempMax

    return [utils.countScore(maxExpr),maxExpr]