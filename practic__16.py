"""Write a python program that lists the following prices, 50, 75, 46, 22, 80, 65, 8, and displays the lowest and highest prices on the screen."""


prices = [ 50, 75, 46, 22, 80, 65, 8]

def minMax(n1):
    #[min] is a comparative function that returns the minimum value in the list
    minN = min(n1)
    #[max] is a comparative function that returns the max value in the list
    maxN = max(n1)
    print(f"""
          max number:{maxN}
          min number:{minN}""") 
        
        
minMax(prices)