def calculator():
    orderofoperator = input("Enter a operator (+/-/*): ")
    number1 = int(input("Enter number one: "))
    number2 = int(input("Enter number two: "))
    def subtraction():
        number3 = number1 - number2
        print(f"The number is")
        print(number3)
    def addition():
        number3 = number1 + number2
        print(f"The number is")
        print(number3)
    def multiplication():
        number3 = number1 * number2
        print(f"The number is")
        print(number3)
    if orderofoperator == '-':
        subtraction()
    elif orderofoperator == "+":
        addition()
    elif orderofoperator == "*":
        multiplication()
    else:
        print("Not an operator")

calculator()