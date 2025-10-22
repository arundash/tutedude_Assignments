"""
ASSIGNMENT 3:
Task 1: Calculate Factorial Using a Function
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    if num == 1:
        return 1
    return num * factorial(num - 1)


number = int(input("Enter a number :"))
print(f"The factorial of {number} is: {factorial(number)}")
