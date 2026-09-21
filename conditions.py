print("\n1. Check whether a number is positive, negative, or zero.\n")
n = int(input("Enter number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


print("\n2. Check whether a person is eligible to vote.\n")
age = int(input("Enter Age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


print("\n3. Find the largest of three numbers.\n")
a = 10
b = 22
c = 33

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)


print("\n4. Check whether a year is a leap year.\n")
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not leap year")


print("\n5. Create a grade system based on marks.\n")
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 50:
    print("Grade E")
else:
    print("Fail")


print("\n6. Check whether a number is divisible by 5 and 11.\n")
n = int(input("Enter number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")


print("\n7. Create a simple calculator using if-elif-else.\n")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", a + b)
elif operator == "-":
    print("Result =", a - b)
elif operator == "*":
    print("Result =", a * b)
elif operator == "/":
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
