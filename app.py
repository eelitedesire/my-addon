#!/usr/bin/env python3

def calculate_sum(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = calculate_sum(num1, num2)

        print(f"The sum of {num1} and {num2} is: {result}")

    except ValueError:
        print("Please enter valid numbers.")
