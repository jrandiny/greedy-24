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

    tempExpr = [str(input[0])]
    maxExpr = tempExpr

    for i in range(1,4):
        tempMax = []
        for opr in ['+','-','*','/']:
            index = 0
            panjang = len(maxExpr) -1
            while(index<=panjang):
                tempExpr = maxExpr.copy()
                tempExpr.insert(index,opr)
                tempExpr.insert(index,str(input[i]))
                index = index + 2
                tempScore = utils.countScore(toText(tempExpr))

                if(tempMax == []):
                    tempMax = tempExpr

                if(tempScore>=utils.countScore(toText(tempMax))):
                    tempMax = tempExpr
                    
            index = 1
            panjang = len(maxExpr)
            while(index<=panjang):
                tempExpr = maxExpr.copy()
                tempExpr.insert(index,str(input[i]))
                tempExpr.insert(index,opr)

                index = index + 2
                tempScore = utils.countScore(toText(tempExpr))

                if(tempMax == []):
                    tempMax = tempExpr
                
                if(tempScore>=utils.countScore(toText(tempMax))):
                    tempMax = tempExpr
                
        maxExpr = tempMax.copy()

        if(i==3):
            tempMax = maxExpr.copy()
            for enclosing in [1,2,3]:
                tempExpr = maxExpr.copy()
                if(enclosing==1):
                    tempExpr = ['((']+tempExpr.copy()
                    tempExpr.insert(4,')')
                    tempExpr.insert(7,')')
                elif(enclosing ==2):
                    tempExpr = ['('] + tempExpr.copy()
                    tempExpr.insert(4,')')
                    tempExpr.insert(6,'(')
                    tempExpr = tempExpr.copy() + [')']
                elif(enclosing ==3):
                    tempExpr.insert(2,'((')
                    tempExpr.insert(6,')')
                    tempExpr = tempExpr.copy() + [')']

                if(utils.countScore(toText(tempExpr))>=utils.countScore(toText(tempMax))):
                    tempMax = tempExpr.copy()
            maxExpr = tempMax.copy()



    return [utils.countScore(toText(maxExpr)),toText(maxExpr)]