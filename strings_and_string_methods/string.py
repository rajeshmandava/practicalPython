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