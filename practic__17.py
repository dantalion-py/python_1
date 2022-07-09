"""Write a program that stores vectors (1,2,3) and (-1,0,2) in two lists and displays your scalar product on the screen"""


numbers1 = [1,2,3]
numbers2 = [-1,0,2]
sumT = 0
#len is a function that returns the length of the list
for i in range(len(numbers1)):
    total = numbers1[i]*numbers2[i]
    sumT+=total
    
print(f"the result is:{sumT}")
