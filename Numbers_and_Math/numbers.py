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