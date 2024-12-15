# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Main Program
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")
