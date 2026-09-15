def calculator():

    # User calculation input
    number1 = int(input("Enter number one: "))
    orderofoperator = input("Enter a operator (+/-/*): ")
    number2 = int(input("Enter number two: "))

    # Calculations
    def subtraction():
        return number1 - number2
    def addition():
        return number1 + number2
    def multiplication():
        return number1 * number2

    #If-else statements to determine which operation to run based on user's operator choice
    if orderofoperator == '-':
        result = subtraction()
    elif orderofoperator == "+":
        result = addition()
    elif orderofoperator == "*":
        result = multiplication()
    else:
        result = None
        print("Not an operator")

    return result

# Display function to print solution
def display(result):
    print(f"The number is {result}")

result = calculator()
display(result)
