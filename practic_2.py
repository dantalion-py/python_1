"""Write a python program to get two numbers and operator from the user to perform arithmetic operations """
try:
    def suma(n1,n2):
        s = n1+n2
        print(f"={s}")
    def subtract(n1,n2):
        s = n1-n2
        print(f"={s}")
    def multiplication(n1,n2):
        s = n1*n2
        print(f"={s}")
    def divicion(n1,n2):
        s = n1/n2
        print(f"={s}")
    def cudrad(n1,n2):
        s = n1**n2
        print(f"={s}")
    def div(n1,n2):
        s = n1//n2
        print(f"={s}")

    number1 = int(input('Enter a number\t'))
    number2 = int(input('Enter a number\t'))
    operation = input('Enter a operation\t')
    if operation == "+":
        suma(number1,number2)
    elif operation == "-":
        subtract(number1,number2)
    elif operation == "*":
        multiplication(number1,number2)
    elif operation == "/":
        divicion(number1,number2)
    elif operation == "**":
        cudrad(number1,number2)
    elif operation == "//":
        div(number1,number2)
    
    else:
        print("unrecognized operation")
except Exception as e:
    print(f"error {e}")