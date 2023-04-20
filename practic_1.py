#is new change
class Dev1:
    level = 23
    def __init__(self,name=None,level=None):
        self._name = name
        self._level =  level
    def __str__(self):
        return f"your name is  {self._name} and your lvl is {self._level}"
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name
        
    
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self,level):
        self._level = level
        
if __name__ == "__main__":    
    name=input("enter your name:\t")    
    level=int(input("enter your level:\t"))    
    obj1 = Dev1(name,level)
    print(obj1)
    
