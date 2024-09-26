# wap for performing different arithmetic operations call a function call def add a+b sub a-b
# save this program as a calculator.

# Parents Class

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b

# Child Class

import calculator
print(calculator.add(5,3))          # OUTPUT : 8
print(calculator.sub(5,3))          # OUTPUT : 2
print(calculator.mul(5,3))          # OUTPUT : 15
print(calculator.divide(5,3))       # OUTPUT : 1.66666
print(calculator.divide(5,0))       # OUTPUT : Cant divided by zero


