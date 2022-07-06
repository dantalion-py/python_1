"""write a python program to generate 1 to n numbers with their square and cube and also display their addition(square + cube)"""
import numpy as np
import pandas as pd
numbers = int(input("enter the limit number to generate:\t"))

listNumbers = []
listSquare = []
listCube = []
listSum = []
for i in range(1,numbers+1):
    Num = i
    listNumbers.append(Num)
    
    squareNum = np.square(i)
    listSquare.append(squareNum)
    
    cubeNum = i**3
    listCube.append(cubeNum)
    
    
    sumNum = squareNum+cubeNum
    listSum.append(sumNum)
    
#method to generate a dataframe with the pandas bookstore
df_1 = pd.DataFrame(listNumbers,columns=["Numbers"])
df_1["Square"] = listSquare
df_1["Cube"] = listCube
df_1["SumSquareCube"] = listSum
print(df_1)