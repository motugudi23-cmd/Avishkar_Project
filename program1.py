num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
operation=input("Enter the operation you want to perform (add, subtract, multiply, divide): ")  
if operation=="add":
    result=num1+num2
    print(f"The result of {num1} + {num2} is: {result}")  
elif operation=="subtract":
    result=num1-num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operation=="multiply":
    result=num1*num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operation=="divide": 
        result=num1/num2
        print(f"The result of {num1} / {num2} is: {result}")
else:
        print("Error: Division by zero is not allowed.")

    