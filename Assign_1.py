
#                   PROGRAMING TASK FOR REFRESHING
# Question 1
def rectangleArea(length,breath):
    print(length*breath)
rectangleArea(3,5)

# Question 2
def isEven(num):
    if num%2==0:
        print(f"{num} is an Even Number")
    else:
        print(f"{num} is not an Even Number")
isEven(7)

# Question 3
def reverseString(string):
    reversed=string[::-1]
    print(reversed)

reverseString("Hello")

# Question 4
def factorial(num):
    if num==0:
        print(f"Factorial of {num} is equal to {1}")
    elif num>0:
        factorial=1
        for i in range(1,num+1):
            factorial*=i
    print(f"Factorial of {num} is equal to {factorial}")

factorial(5)

# Question 5
def isPalindrome(string):
    string = string.lower().replace(' ', '')
    if string == string[::-1]:
        print(f"Yes,{string} is an palindrome")

isPalindrome("radar")

# Question 6
def fibonacciSeries(Tn):
    fibonacci = [0,1]
    for i in range(2,Tn):
        newTerm = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(newTerm)
    print(fibonacci)

fibonacciSeries(6)

# Question 7
def largestNumber(num1,num2,num3):
    if num1>num2 and num1>num3:
            print(f"{num1} is larger")
    elif num2>num1 and num2>num3:
            print(f"{num2} is larger")
    else:
            print(f"{num3} is larger")

largestNumber(10,25,5)

# Question 8
def simpleIntrest(principleAmount,intrestRate,time):
     intrest=(principleAmount*intrestRate*time)/100
     print(intrest)

simpleIntrest(1000,5,2)

# Question 9
def TctoTf(Tc):
     Tf=(Tc*9/5)+32
     print(f"{Tc} in Celsius is equal to {Tf} in Fahrenheit")

TctoTf(37)

# Question 10
import calendar
def isLeapYear(year):
    if calendar.isleap(year):
          print(f"{year} is a leap year")
    else:
         print(f"{year} is not a leap year")

isLeapYear(2020)


#                         PROGRAMING CHALLENGES

# Question 1
def findMedian(list):
     newList=sorted(list)
     if len(newList)%2==0:
          T1=newList[len(newList)//2-1]
          T2=newList[len(newList)//2]
          median=(T1+T2)/2
          print(f"Median of {list} is {median}")

     else:
          median=newList[len(newList)//2]
          print(f"Median of {list} is {median}")
          
     
findMedian([10,5,20])

# Question 2
def countWord(txt):
     word=txt.count(" ")
     print(f"number of words in '{txt}' is {word}")

countWord("The quick brown fox jumps over the lazy dog.")

# Question 3
def sumOfDigit(num):
     sum=0
     num=str(num)
     for i in range(1,len(num)):
          sum=sum+int(num[i])
     print(f"Sum of the given number digits is : {sum}")

sumOfDigit(12345)

# Question 4
def commonLongestPrefix(list):
    prefix = list[0]

    for string in list[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix) - 1]
        if not prefix:
            break
    print(prefix)

commonLongestPrefix(["flow", "flower", "float"])


# Question 5
from sympy import isprime #you shuld install sympy library by this "pip install symspy"

def isPrime(num):
    if isprime(num):
        print(f"Yes, {num} is a Prime Number")
    else:
        print(f"No, {num} is not a Prime Number")

isPrime(29)


#                                BONOUS QUESTION

def longestCommonSequence(list):
    newList = sorted(list)
    sequence = [newList[0]]
    for i in range(len(newList) - 1):
        if newList[i] == (newList[i + 1] - 1):
            sequence.append(newList[i + 1])
    print(sequence)
    
longestCommonSequence([100,4,200,1,3,2])


