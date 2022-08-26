
# Working with strings and numbers

# Using Strings with arithmetic operators
from ast import Num
from tokenize import Number


num = "2"
new_num = num+num
print(new_num)

num = "12"
new_num = num*3
print(new_num)
new_num = ""
new_num = 3*num
print(new_num)
new_num = ""
# newnum = "3"*"12" Typeerror: can't multiply sequence by non-int of type 'str'

# new_num = "3" + 3 TypeError : Can only concatenate str (not "int") to str
print(new_num)

num = int(input("Enter a number to be doubled : "))
doubled_num = num *2
print(doubled_num)

# Converting Numbers to Strings

num_packages = 10
string1 = "I am going to ship " + str(num_packages) +" packages."
print(string1)

total_pancakes = 10
pancakes_eaten = 5
string1 = "Only " + str(total_pancakes-pancakes_eaten) + " pancakes left"
print(string1)

# Review exercises

# 1. Create a string containing an integer, then convert that string into an actual integer object using int(). Test that your new object is a number by multiplying it by another number and displaying the result.
string1 = "5"
num_conversion = int(string1)
num = num_conversion * 3
print(num)

# 2. Repeat the previous exercise, but use a floating-point number and float()
string1 = "2.34"
num_conversion = float(string1)
num = num_conversion *2
print(num)

# 3. Create a string object and an integer object, then display them side by side with a single print statement using str().
string1 = "The festival day starts on "
date = 31
print(string1 + str(date))

# 4. Write a program that uses input() twice to get two numbers from the user, multiplies the numbers together, and displays the result. If the user enters 2 and 4, then your program should print the following text:
num1 = float(input("Enter number1 : "))
num2 = float(input("Enter number2 : "))
new_num = num1*num2
print("The product of 2 and 4 is "+str(new_num))
