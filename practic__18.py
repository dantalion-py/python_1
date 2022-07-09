"""write a python program to get large number as starting and lower number as ending number, 
display that number from large to lower.
as user input 10 large number and 5 as lower number, then it should display as: 10,9,7,6,5 """



listValues =  []
def convert(n1,n2):
    
    for i in range(n1,n2-1,-1):
        listValues.append(i)
    print(listValues)    
    return listValues
   
numberB = int(input("enter a big number:\t"))
numberS = int(input("enter a small number:\t"))

convert(numberB,numberS)
