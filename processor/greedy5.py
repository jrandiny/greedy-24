import utils

def getName():
    return "Josh () akhir Greedy"

def toText(arr):
    teks = ""
    for entry in arr:
        teks = teks + entry
    return teks

def calculate(param):
    input = list(param)

    input.sort(reverse = True)
    
    # result = input[0]
    tempExpr = [str(input[0])]
    maxExpr = tempExpr

    for i in range(1,4):
        tempMax = "empty"
        for pos in[0,1]:
            for opr in ['+','-','*','/']:
                tempExpr = maxExpr
                
                if(pos==0):
                    tempExpr = tempExpr+[opr]
                    tempExpr = tempExpr+[str(input[i])]
                else:
                    tempExpr = [opr]+tempExpr
                    tempExpr = [str(input[i])]+tempExpr
                tempScore = utils.countScore(toText(tempExpr))

                if(tempMax == "empty"):
                    tempMax = tempExpr

                if(tempScore>=utils.countScore(toText(tempMax))):
                    tempMax = tempExpr
        maxExpr = tempMax
        if(i==3):
            for enclosing in [1,2]:
                tempExpr = maxExpr
                if(enclosing==1):
                    tempExpr = ['((']+tempExpr
                    tempExpr.insert(4,')')
                    tempExpr.insert(7,')')
                elif(enclosing ==2):
                    pass
                if(utils.countScore(tempExpr)>=utils.countScore(toText(maxExpr))):
                    maxExpr = tempExpr



    return [utils.countScore(maxExpr),maxExpr]