# Basics of Python

# 1. Variables and Data Types
name = "Himanshu"
age = 25
is_student = True

# 2. Function to greet
def greet_user(user_name):
    return f"Hello, {user_name}!"

# 3. Loop and Conditional
def check_age(age):
    if age < 18:
        return "You are a minor."
    elif age < 60:
        return "You are an adult."
    else:
        return "You are a senior citizen."

# 4. Main Program
print(greet_user(name))  # Function call
print(f"Age: {age}")

# Iterating through a range
for i in range(1, 6):
    print(f"Number: {i}")

# Check the age category
print(check_age(age))
