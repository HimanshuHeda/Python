# Python Basics

## Introduction

Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used in web development, data science, automation, AI, and more.

---

## 1️⃣ Installation

### Download & Install Python:

- Visit [Python Official Website](https://www.python.org/)
- Download the latest version for your OS
- Install Python (Ensure you check the box to add Python to PATH)
- Verify installation:
  ```bash
  python --version  # For Windows
  python3 --version # For macOS/Linux
  ```

---

## 2️⃣ Python Syntax Basics

### Hello World Program:

```python
print("Hello, World!")
```

### Variables & Data Types:

```python
name = "John"  # String
grade = 10      # Integer
price = 99.99   # Float
is_active = True # Boolean
```

### Data Type Conversion:

```python
num = "10"
converted_num = int(num)  # Convert string to integer
```

---

## 3️⃣ Control Flow

### If-Else Statements:

```python
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### Loops:

#### For Loop:

```python
for i in range(5):
    print(i)
```

#### While Loop:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 4️⃣ Functions

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

---

## 5️⃣ Lists & Dictionaries

### Lists:

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])  # Apple
```

### Dictionaries:

```python
person = {"name": "John", "age": 30}
print(person["name"])  # John
```

---

## 6️⃣ File Handling

### Writing to a File:

```python
with open("example.txt", "w") as file:
    file.write("Hello, File!")
```

### Reading a File:

```python
with open("example.txt", "r") as file:
    print(file.read())
```

---

## 7️⃣ Error Handling

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

## 8️⃣ Importing Modules

```python
import math
print(math.sqrt(25))  # 5.0
```

---

## 9️⃣ Virtual Environments

```bash
# Create a virtual environment
python -m venv myenv

# Activate virtual environment
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate     # Windows
```

---

## 🔟 Popular Libraries

- **NumPy** - Numerical computing
- **Pandas** - Data analysis
- **Matplotlib** - Data visualization
- **Requests** - HTTP requests

---

## 🚀 Next Steps

- Learn **Object-Oriented Programming (OOP)**
- Explore **Web Development (Flask, Django)**
- Try **Data Science & AI (Pandas, TensorFlow)**
- Build **Automation Scripts**

Happy Coding! 🎯

