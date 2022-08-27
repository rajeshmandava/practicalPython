
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

# num = int(input("Enter a number to be doubled : "))
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
# num1 = float(input("Enter number1 : "))
# num2 = float(input("Enter number2 : "))
# new_num = num1*num2
# print("The product of 2 and 4 is "+str(new_num))

# 4.7 Streamline your print statements
# String interpolation
name = "zaphod"
heads = 2
arms =3
string1 = name + " has " + str(heads) + " heads and " + str(arms) + " arms"
print(string1)

# formatted string literals or f-strings
string1 = f"{name} has {heads} heads and {arms} arms"
print(string1)

# f-strings are available from Python 3.6 and above. 
# format() has to be used before Python3.6. Lets build same string using format function

string1 = "{} has {} heads and {} arms".format(name,heads,arms)
print(string1)

# Review exercies
# 1. Create a float object named weight with the value 0.2, and create a string object anmed animal with the value "newt". Then use these objects to print tht following string using only string concatenation:
# 2. Display the same string using an f-string.
weight = 0.2
animal = "newt"
string1 = f"{weight} kg is the weight of the {animal}."
print(string1)

# 2. Display the same string by using .format and empty {} placeholders
string1 = "{} kg is the weight of the {}.".format(weight,animal)
print(string1)

# Find a string in a string
# find() -> to find a string in another string
# if find() doesn't find a desired substring, it will return -1
# find() is case sensitive

phrase = "the surprise is in here somewhere"
index = phrase.find("surprise")
print(index)
print(phrase.find("askdhsk"))

string1 = "I put a string in your string"
print(string1.find("string"))

string1 = "my number is 0123456789"
# print(string1.find(1)) TypeError: must be str, not int
print(string1.find("1"))

pun_intended = "I'm telling you the truth; no thing but the truth!"
pun_intended = pun_intended.replace("the truth", "lies")
print(pun_intended)

text = "some of the stuff"
new_text = text.replace("some of","all")
print(new_text)
new_text = new_text.replace("stuff","things")
print(new_text)

# Review exercises
# 1. In one line of code, display the result of tring to .find() the substring "a" in the string "AAA". The result should be -1
string="AAA"
print(string.find("a"))

# 2. Replace every occurence of the character "s" with "x" in the string "Somebody said something to Samantha."
string1 = "Somebody said something to Samantha."
string1 = string1.replace("s","x")
print(string1)

# 3. Write a program that accepts user input with input() and displays the result of tring to .find() a particular letter in that input.
string1 = input("Enter your input:")
string2 = input("Enter substring to find:")
print(string1.find(string2))