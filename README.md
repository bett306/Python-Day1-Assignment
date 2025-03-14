# Python-Day1-Assignment
operator = input("Choose an operator (+,-,*,/): ")
num1 = float(input("What is you first number"))
num2 = float(input("What is your second number"))

if operator == "+":
    result = round((num1 + num2),3)
    print(f"Your answer is {result}")
elif operator == "-":
    result = round((num1 - num2),3)
    print(f"Your answer is {result}")
elif operator == "*":
    result = round((num1 * num2),3)
    print(f"Your answer is {result}")
elif operator == "/":
    result = round((num1 / num2),3)
    print(f"Your answer is {result}")
else:
    print(f"The value {operator} is invalid")
