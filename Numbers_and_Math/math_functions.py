# round function to round of the values to nearest value

# 1. rounding ties to even

from tokenize import Number


num = round(2.3)
print(num)

num = round(2.7)
print(num)

num = round(2.5)
print(num)

num = round(3.5)
print(num)

num = round(3.14159, 3)
print(num)

num = round(2.71828, 2)
print(num)

num = round(2.675, 2)
print(num)

#  Floating-point representation error, not a bug in round()

# The abs() function

num1= abs(3)
print(num1)

num2= abs(-5.0)
print(num2)

# pow() function

num1 = pow(2,3)
print(num1)

num1 = pow(2,-2)
print(num1)

#  Difference between ** and pow()
# The pow() function takes third parameter apart from base and exponenent and then takes modulo of the calulcated pow

num1 = pow(2,3,4)
print(num1)


# Check if a float is integral

num = 2.5
print(num.is_integer())

num = 2.0
print(num.is_integer())

# Review exercises

# 1. Write a program that asks the user to input a number and then displays that number rounded to two decimal places. When run, your program should like this:

num = float(input("Enter a number  : "))
rounded_num = round(num,2)
print(f"{num} rounded to 2 decimal places is {rounded_num}")

# 2. Write a program that asks the user to input a number and then displays the absolute value of that number. When run, your program should like this:
num = float(input("Enter a number:"))
abs_num = abs(num)
print(f"The absolute value of {int(num)} is {abs_num}")

# 3. Write a program that asks the user to input two numbers by using input() twice, then displays whether the difference between those two numbers is an integer. When run, your program should look like this:
num1 = float(input("Enter a number : "))
num2 = float(input("Enter another number:"))
diff_num = num1 - num2
print(f"The difference between {num1} and {num2} is an integer? {diff_num.is_integer()}")