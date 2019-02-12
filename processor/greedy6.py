import utils

def getName():
    return "Josh group reedy"

def calculate(param):
    inputNum = list(param)

    inputNum.sort(reverse = True)

    input = []

    for num in inputNum:
        input.append(str(num))

    pairs = [[8,3,'*'],[6,4,'*'],[12,2,'*'],[25,1,'-'],[24,0,'+'],[23,1,'+'],[26,2,'-'],[27,3,'-'],[22,2,'+'],[21,3,'+']]

    posiblePick= [[[1,2],[3,4]],[[1,3],[2,4]],[[1,4],[2,2]]]

    lowestDelta = 99
    lowestConfLeft  = ""
    lowestConfRight = ""
    lowestConfCenter = ""

    print(input)

    for pair in pairs:
        for pick in posiblePick:
            for swap in [True,False]:
                if(swap):
                    pick.reverse()
                for internalSwap in [True,False]:
                    if(internalSwap):
                        pick[0].reverse()
                        pick[1].reverse()
                    for opr in ['+','-','*','/']:
                        for opr2 in ['+','-','*','/']:
                            deltaLeft = abs(eval(input[pick[0][0]-1] + opr + input[pick[0][1]-1])-pair[0])
                            deltaRight = abs(eval(input[pick[1][0]-1] + opr2 + input[pick[1][1]-1])-pair[1])
                            if((deltaLeft+deltaRight)<lowestDelta):
                                lowestConfLeft = "("+input[pick[0][0]-1] + opr + input[pick[0][1]-1]+")"
                                lowestConfRight = "("+input[pick[1][0]-1] + opr2 + input[pick[1][1]-1]+")"
                                lowestConfCenter = pair[2]
                                lowestDelta = deltaLeft+deltaRight

    maxExpr = lowestConfLeft+lowestConfCenter+lowestConfRight

    return [utils.countScore(maxExpr),maxExpr]