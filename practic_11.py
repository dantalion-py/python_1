"""write a python  program to get 5 numbers in the list, pass that list in the funcion to multiply and add that numbers and display total result"""

def operation(list_numbers):
    sum_list = 0
    print("list the numbers")
    for n in list_numbers:
        print(n)
    for i in list_numbers:
        sum_list +=  i
    print(f"ther result of the sum: {sum_list}")
    mul_list = 1
    for j in list_numbers:
        mul_list = mul_list * j
        
    print(f"ther result of the mul: {mul_list}")

number = []
for i in range(5):
    numbe = int(input("enter a number:\t"))
    number.append(numbe)
operation(number)
