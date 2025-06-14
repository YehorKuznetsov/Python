print("Hello, Python")

name=input("Enter your name: ")
print(f"Hello, {name}")
try:
    num1 = float(input("Enter 1st num: "))
    num2 = float(input("Enter 2nd num: "))
    sum = num1+num2
    print(f"Summary: {sum}")
except ValueError:
    print("Error! Please, enter the number")
