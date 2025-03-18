operator = input("Choose an operator (+,-,*,/): ")
num1 = float(input("What is your first number:"))
num2 = float(input("What is your second number:"))

if operator == "+":
    result =((num1 + num2))
    print(f"Your answer is {result}")
elif operator == "-":
    result =((num1 - num2))
    print(f"Your answer is {result}")
elif operator == "*":
    result =((num1 * num2))
    print(f"Your answer is {result}")
elif operator == "/":
    result =((num1 / num2))
    print(f"Your answer is {result}")
else:
    print(f"The value {operator} is invalid")