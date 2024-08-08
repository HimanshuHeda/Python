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


import calculator
print(calculator.add(5,13))          # OUTPUT : 18
print(calculator.sub(5,43))          # OUTPUT : -38
print(calculator.mul(52,2))          # OUTPUT : 104
print(calculator.divide(15,19))      # OUTPUT : 0.789
print(calculator.divide(5,3))        # OUTPUT : 1.6666
