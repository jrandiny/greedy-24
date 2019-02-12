import utils

def getName():
    return "Josh double () reverse Greedy"

def calculate(param):
    input = list(param)

    input.sort(reverse = True)
    
    # result = input[0]
    tempExpr = str(input[0]) 
    maxExpr = tempExpr

    for i in range(1,4):
        tempMax = "empty"
        for enclosed in [0,1]:
            for pos in[0,1]:
                for opr in ['+','-','*','/']:
                    tempExpr = maxExpr
                    if(enclosed==1):
                        tempExpr = "(" + tempExpr + ")"
                    
                    if(pos==0):
                        tempExpr = tempExpr+opr
                        tempExpr = tempExpr+str(input[i])
                    else:
                        tempExpr = opr+tempExpr
                        tempExpr = str(input[i])+tempExpr
                    tempScore = utils.countScore(tempExpr)

                    if(tempMax == "empty"):
                        tempMax = tempExpr

                    if(tempScore>=utils.countScore(tempMax)):
                        tempMax = tempExpr
        maxExpr = tempMax

    return [utils.countScore(maxExpr),maxExpr]