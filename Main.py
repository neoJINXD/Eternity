import numpy as np


def calculateExplonent(x, y):
    newValue = x
    theExponent = y * -1
    if isinstance(y, int):
        secondCalculation = calculateExplonentIntOnly(x, y)
    else:
        firstCalculation = calculateRoot(x)
        print("TESTING")
        print(firstCalculation)
        numerator = int(y * 100)
        secondCalculation = calculateExplonentIntOnly(firstCalculation, numerator)
    return secondCalculation


#This is a helper function that calculates x^y when y is an integer
def calculateExplonentIntOnly(x,y):
    newValue = x
    if isExponentNegative(y):
        y = y * -1
        for value in range(1, y):
            newValue = newValue * x
    else:
        for value in range(1, y):
            newValue = newValue * x

    return newValue

def isExponentNegative(x):
    if x >= 0:
        return False
    return True

#This function takes the inverse
def takeInverse(x):
    return 1/x

#This is a helper function that is used to calculate the approximate value of a number that is root 100
def calculateRoot(b):
    a = calculateApproxSquare()
    theNumber = 0
    toContinue = True
    while toContinue:
        index = 0
        for values in a:
            theValue = a.get(values)
            temp = calculateExplonentIntOnly(values, 100)
            if temp < b:
                continue
                index = index + 1
            if temp > b:
                toContinue = False
                theNumber = values
                break
    print(theNumber)
    return theNumber

#This is a helper function to obtain a dictionary with a number and the corresponding
# result of that number power of 100
def calculateApproxSquare():
    a = np.arange(1,1.44,0.000001) #Not sure if numpy can be used
    dictionary = {}
    newlist = []
    for items in a:
        newlist.append(calculateExplonentIntOnly(items, 100))
    value = 0
    for i in a:
        dictionary[i] = newlist[value]
        value = value + 1
    print(dictionary)
    return dictionary


# Main method
theValue = calculateExplonent(2,-6)
print(theValue)
x = 2**-6
print(x)

# x = 2**5.5
# print(x)