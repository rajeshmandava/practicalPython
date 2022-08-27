# Numbers and Math
# In this chapter, you'll learn how to:
# 1. Create integers and floating-point numbers
# 2. Round numbers to a given number of decimal places
# 3. Format and display numbers in strings


# Python has three built-in numberic data types
# 1. integers
# 2. floating-point numbers
# 3. complex numbers

# Integers
print(type(1))
num = 1_000_000
print(num)

# Floating-point numbers
num = 1.0
print(type(num))
num1 = 1_000_00.0
print(type(num))
print(num1)

num1 = 2e+3
print(num1)
num1=2e-4
print(num1)
num=2e400
print(num)
print(type(num))
num = -1e400
print(num)
print(type(num))

# Review exercises

# 1. Write a program that creates two variables, num1 and num2. Both num1 and num2 should be assigned the integer literal 25000000, one written with underscores and one without. 
# Print num1 and num2 on two seperate lines.

num1 = 25000000
num2 = 25_000_000
print(num1)
print(num2)

# 2. Write a program that assigns the floating-point literal 175000.0 to the variable num using E notation and then prints num in the interactive window
num1 = 175000.0
num2 = 1.75e5
print(num1)
print(num2)

num = 2e308 # 2e308 is smallest exponent number which returns inf
print(num)

# Airthmetic Operators and Expressions

# Addition
num1 = 1
num2 = 2
num = num1+num2
print(num)
num1 = 10.0
num = num1+num2
print(num)

# Subtraction
num = num1 - num2
print(num)
num1 = -3
print(num1)

num1 = 1
num2= -3
num = num1 - num2
print(num)

# Multiplication

num1 = 3
num2 = 4
num = num1 * num2
print(num)

num1 = 2
num2 = 8.0
num = num1 * num2
print(num)

# Division
num1 = 9
num2 = 3
num = num1 / num2
print(num)

num1 = 5.0
num2 = 2
num = num1 / num2
print(num)

num1 = 9
num2 = 3
num = int(num1 / num2)
print(num)

# Integer Division
num1 = 9
num2 = 3
num = num1 // num2
print(num)

num1 = 5.0
num2 = 2
num = num1//num2
print(num)

# Exponents
num1 = 2
num2 = 2
num = num1 ** num2
print(num)

num1 = 2
num2 = 3
num = num1 ** num2
print(num)

num1 = 3
num2 = 1.5
num = num1 ** num2
print(num)

num1 = 9
num2 = 0.5
num = num1 ** num2
print(num)

num1 = 2
num2 = -1
num = num1 ** num2
print(num)

num1 = 2
num2 = -2
num = num1 ** num2
print(num)

# The Modulus Operator

num1 = 5
num2 = 3
num = num1 % num2
print(num)

num1 = 20
num2 = 7
num = num1 % num2 
print(num)

num1 = 16
num2 = 8
num = num1 % num2
print(num)