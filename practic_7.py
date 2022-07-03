"""write a python program to get 10 name of the students from the user in list, display that students name in descending order"""

try:
    list_names = []
    for i in range(10):
        names = input("enter a name:\t")
        list_names.append(names)
        
    print("list names:")
    for j in list_names:
    
        print(j)
        
        
    list_names.reverse()
    print("list names in descending order:")
    for k in list_names:
        
        print(k)
except Exception as e:
    print(f"Exception {e}")