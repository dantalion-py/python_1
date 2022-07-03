"""write a python program to check a year, whether it is a leap year or not"""
# To determine if a leap year is a leap year, follow these steps:

#1     If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
#2     If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
#3     If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
#4     The year is a leap year (it has 366 days).
#5     The year is not a leap year (it has 365 days).
def leap(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                print("The leap year is not a leap year")
            else:
                print("The leap year is not a leap year")
        else:
            print("The leap year is a leap year")
    else:
        print("the year is not a leap year")
year = int(input("enter the year:\t"))

leap(year)