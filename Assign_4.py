from functools import reduce

#       Question 1    

myList : list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
outputList : list = list(filter(lambda new:len(new)>5,myList))
print(outputList)

#       Question 2

myNumbers : list = [2, 4, 6, 8, 10]
doubleNumbers : list = list(map(lambda num: num * 2, myNumbers))
print(doubleNumbers)

outputNumbers : list = reduce(lambda num1, num2: num1 * num2, doubleNumbers)
print(outputNumbers)



