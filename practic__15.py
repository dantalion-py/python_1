"""write a python program to get starting number and ending number from the user to display that number with proper sequence
as, user input 5 as starting number and 10 as ending number, then it should display
5,6,7,8,9,10"""

number1 = int(input("enter the first number:\t")) 
number2 = int(input("enter the final number:\t")) 
num2 = number2+1


for i in range(number1,num2):
    print(i)