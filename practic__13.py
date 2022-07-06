"""write a python program to get a angle from the user and find its sin and cos vaue in radian"""
import numpy as np
class SenCos:
    def __init__(self,num1):
        self.num1 = num1
            
        
    def calc(self):
        #(np.cos) is a function to calculate the sine of the expected angle
        radianCos = np.cos(self.num1)
        radianSen = np.sin(self.num1)
        print(f"the cosen is {radianCos}")
        print(f"the sen is {radianSen}")
            
            


degree = float(input("enter a degrees:\t"))
data=SenCos(degree)
data.calc()

