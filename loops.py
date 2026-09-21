print("\n1. Print numbers from 1 to 10 using a for loop.\n")

for i in range(1, 11):
    print(i)


print("\n2. Print numbers from 10 to 1 using a while loop.\n")

i = 10

while i >= 1:
    print(i)
    i = i - 1


print("\n3. Print the multiplication table of a number.\n")

n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


print("\n4. Find the sum of numbers from 1 to n.\n")

n = int(input("Enter number: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)


print("\n5. Find the factorial of a number.\n")

n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


print("\n6. Print all even numbers between 1 and 100.\n")

for i in range(1, 101):
    if i % 2 == 0:
        print(i)


print("\n7. Reverse a number using a loop.\n")

n = int(input("Enter number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)


print("\n8. Count the digits of a number.\n")

n = int(input("Enter number: "))

count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Number of digits =", count)


print("\n9. Check whether a number is prime.\n")

n = int(input("Enter number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")


print("\n10. Print Fibonacci series up to n terms.\n")

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
