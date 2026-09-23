# print("\n1. Write a function to print 'Hello World'\n")
# def hello():
#     print("Hello WOrld")
# hello()

# print("\n2. Write a function that takes a name and prints a greeting\n")
# def greet(name):
#     print("Hello...", name, "Har Har Mahadev")
# greet("Nikhil")

# print("\n3. Write a function to add two number\n")
# def add(a, b):
#     return a+b
# result = add(101, 201)
# print("Sum = ", result)

# print("\n4. Write a function to find the square of a number\n")
# def square(num):
#     return num * num

# result = square(5)
# print("Square =", result)

# print("\n5. Write a function to check whether a number is even or odd\n")
# def check_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# num = int(input("Enter a number: "))
# check_even_odd(num)

# print("\n6. Write a function to find the maximum of two numbers\n")
# def find_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("Maximum =", find_max(num1, num2))

# print("\n7. Write a function to convert Celsius to Fahrenhit\n")
# def celsius_to_fahrenheit(c):
#     return (c * 9/5) + 32

# celsius = float(input("Enter temperature in Celsius: "))
# print("Temperature in Fahrenheit =", celsius_to_fahrenheit(celsius))

# print("\n8. Write a function to calculatee the area of a circle\n")
# def area(radius):
#     pi = 3.14
#     return pi * radius * radius
# radius = float(input("Enter radius of circle : "))
# print("Area of circle =", area(radius))

# print("\n9. Write a function to calculate the factorial of a number\n")
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# n = int(input("Enter a number: "))
# print("Factorial =", factorial(n))

# print("\n10. Write a function to check whether a number is positive, negative or zero\n")
# def check_number(num):
#     if num > 0:
#         print("Positive")
#     elif num < 0:
#         print("Negative")
#     else:
#         print("Zero")
# num = int(input("Enter a number: "))
# check_number(num)

# print("\n11. Write a function to find the maximum of three numbers\n")
# def max(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# print("Maximum =", max(a, b, c))

# print("\n12. Write a function to count vovels in a string\n")
# def vowel(string):
#     count = 0
#     for char in string:
#         if char in 'aeiouAEIOU':
#             count += 1
#     return count
# string = input("Enter a string: ")
# print("Number of vowels =", vowel(string))

# print("\n13. Write a function to reverse a string\n")
# def reverse_string(string):
#     return string[::-1]
# string = input("Enter a string: ")
# print("Reversed string =", reverse_string(string))

# print("\n14. Write a function to check whether a string is palindrome\n")
# def pelindrome(string):
#     return string == string[::-1]
# string = input("Enter a string: ")
# if pelindrome(string):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# print("\n15. Write a function to find the sum of all elements in a list\n")
# def list_sum(numbers):
#     total = 0

#     for num in numbers:
#         total = total + num

#     return total

# numbers = list(map(int, input("Enter numbers: ").split()))
# print("Sum =", list_sum(numbers))

# print("\n16. Write a function to find the largest element in a list\n")
# def largest(numbers):
#     large = numbers[0]

#     for num in numbers:
#         if num > large:
#             large = num

#     return large

# numbers = list(map(int, input("Enter numbers: ").split()))
# print("Largest =", largest(numbers))

# print("\n17. Write a function to remove duplicate element from a list\n")
# def remove_duplicates(numbers):
#     new_list = []

#     for num in numbers:
#         if num not in new_list:
#             new_list.append(num)

#     return new_list

# numbers = [1, 2, 3, 4, 5, 11, 22, 33, 4, 5, 2, 1, 66, 22, 11, 44, 5, 1, 2, 3, 4, 5]
# print(remove_duplicates(numbers))

# print("\n18. Write a function to count how many times an element appears in a list\n")
# def count_element(numbers, element):
#     count = 0

#     for num in numbers:
#         if num == element:
#             count += 1

#     return count

# numbers = [10, 20, 10, 30, 20, 10, 40, 10, 20 ,30, 50, 60]
# print("List: ", numbers)
# element = int(input("Enter the element to count: "))
# print("Count =", count_element(numbers, element))

# print("\n19. Write a function to check whether a number is prime\n")
# def is_prime(num):
#     if num < 2:
#         return False

#     for i in range(2, num):
#         if num % i == 0:
#             return False

#     return True

# num = int(input("Enter a number: "))
# if is_prime(num):
#     print("Prime number")
# else:
#     print("Not a prime number")

# print("\n20. Write a function to return all prime numbers between two numbers\n")
# def is_prime(num):
#     if num < 2:
#         return False

#     for i in range(2, num):
#         if num % i == 0:
#             return False

#     return True

# def prime_numbers(start, end):
#     primes = []

#     for num in range(start, end + 1):
#         if is_prime(num):
#             primes.append(num)

#     return primes

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# print("Prime numbers:", prime_numbers(start, end))

# print("\n21. Write a function to calculate Fibonacci numbers\n")
# def fibonacci(n):
#     a = 0
#     b = 1

#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b


# n = int(input("Enter number of terms: "))

# fibonacci(n)

# print("\n22. Write a function to find second-largest number in a list\n")
# def second_largest(numbers):
#     largest = numbers[0]
#     second = numbers[0]

#     for num in numbers:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             second = num

#     return second

# numbers = [10, 25, 30, 15, 40, 35]
# print("List:", numbers)
# print("Second largest =", second_largest(numbers))

# print("\n23. Write a function to sort a list without using sort()\n")
# def sort_list(numbers):
#     for i in range(len(numbers)):
#         for j in range(len(numbers) - 1):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

#     return numbers


# numbers = [40, 10, 30, 20, 50]
# print("Original list:", numbers)
# print("Sorted list:", sort_list(numbers))

# print("\n24. Write a function to merge two list and remove duplicates\n")
# def merge_lists(list1, list2):
#     new_list = []

#     for num in list1 + list2:
#         if num not in new_list:
#             new_list.append(num)

#     return new_list


# list1 = [10, 20, 30, 40]
# list2 = [30, 40, 50, 60]
# print("List 1:", list1)
# print("List 2:", list2)
# print("Merged list:", merge_lists(list1, list2))