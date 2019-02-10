import random

def countScore(expressionStr):
    try:
        skor = (-10)*abs(24 - (eval(expressionStr)))
        for i in range (len(expressionStr)):
            if (expressionStr[i]=='+'):
                skor = skor + 5
            if (expressionStr[i]=='-'):
                skor = skor + 4
            if (expressionStr[i]=='*'):
                skor = skor + 3
            if (expressionStr[i]=='/'):
                skor = skor + 2
            if (expressionStr[i]=='(' or expressionStr[i] == ')'):
                skor = skor - 0.5
        return skor
    except:
        return -999

def pick4card(deck):
    cards = []
    for _ in range(4):
        index = random.randint(0,len(deck)-1)
        newDeck = deck[0:index]
        cards.append(deck[index:index+1][0])
        newDeck = newDeck + deck[index+1:len(deck)]
        deck = newDeck
    
    return [cards,deck]


def getNewDeck():
    return [1,2,3,4,5,6,7,8,9,10,11,12,13]*4

if __name__ == '__main__':
    deck = getNewDeck()

    while(len(deck)>0):
        out = pick4card(deck)
        deck = out[1]
        print(out[0])
