"""
Task 2: Using the Math Module for Calculations

Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
 Expected Output:
 For example, if the user enters 25, the output should be:
Expected Output: For example, if the user enters 25,
the output should be:
    Enter a number : 25
    square root :5
    Logarithm: 3.218875 Sine : -0.132
"""
import math

# Step 1: Ask the user for a number
num = float(input("Enter a number: "))

# Step 2: Perform calculations using math module
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

# Step 3: Display the results
print(f"Square root: {sqrt_val:.3f}")
print(f"Logarithm: {log_val:.6f}")
print(f"Sine: {sine_val:.3f}")
