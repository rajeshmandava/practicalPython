# strings and string methods
""" 
manipulate strings with string methods
Work with user input
Deal with strings of numbers
Format strings for printing 
 """

print(type('Hello world'))
phrase = "Hello, world"
print(type(phrase))

string3 = "we're #1"
string4 = 'I said, "put it over by the 11am a."'
print(string3)
print(string4)

print(len(string3))
# print(string4.__len__)

multiline_string = """ This is multiline string of line 1
The second line is starting in line number two.
Third line is starting in line number three.
Just wondering where the fourth line is going to be in.
Guess the size of the string five.
I hope the string in line six is no longer the limit by pep8"""

print(multiline_string)

# Review exercises

# 1. Print a string that uses double quotation marks inside the string.
string3 = 'This string is "double quotation marks inside a string"'
print(string3)
# 2. Print a string that uses an apostrophe inside the string.
string4 = "We're going to a festival on coming saturday"
print(string4)
# 3. Print a string that spans multiple lines with whitespace preserved
string3 = """We are testing a string with multilines 
Lets add a second value in line number two
Adding another string in line number three"""
print(string3)
# 4. Print a string that is coded on multiple lines but gets printed on a single line
string4 = "This is line number one \
  continuing in line number two"

print(string4)

# 4.2 Concatenation, Indexing and Slicing

# 1. Concatenation, which joins two strings together
# 2. Indexing, which gets a single character from a string
# 3. Slicing, which gets several characters from a string at once

string1 = "Hello"
string2 = "world!"
magic_string = string1 + string2
print(magic_string)

first_name = "Arthur"
last_name = "Dent"
full_name = first_name + " "+last_name
print(full_name)

# String indexing
flavor = "fig pie"
print(flavor[1])
print(flavor[0])

final_index = len(flavor)-1
last_character  = flavor[final_index]

print(final_index)
print(last_character)

# String slicing
first_three_letters = flavor[0] + flavor[1] +flavor[2]
print(first_three_letters)
print(flavor[0:3])
print(flavor[:3])
print(flavor[3:])
print(flavor[:])
print(flavor[13:15])

# Strings are Immutable
word = "goal"
# word[0] ='f' TypeError : 'str' object does not support item assignment

word = "f"  + word[1:]
print(word)

# Review Exercises

# 1. Create a string and print its length using len()
string1 = "This is string"
print(len(string1))

# 2. Create two strings, concatenate them, and print the resulting string.
# 3. Create two strings, use concatenation to add a space between them, and print the result
string1 = "This is string"
string2 = "Concatenation"

multi_string = string1+" "+ string2

print(multi_string)

# 4. Print the string "zing" by using slice notation to specify the correct range of characters in the string "zbazinga"
string1 = "bazinga"
last_index = len(string1)-1
print(last_index)
print(string1[2:last_index])
