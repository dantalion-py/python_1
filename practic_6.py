"""Write a python program to get number from user to find square of that number"""


class Square:
    def __init__(self,squ):
        self._squ = squ
        
    def cua(self):
        cuadrado = self._squ**2
        print(f"= {cuadrado}")
    
    
num1 = int(input("Enter the number:\t"))
ojt = Square(num1)
ojt.cua()