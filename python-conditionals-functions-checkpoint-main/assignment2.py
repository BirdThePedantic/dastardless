# Name: Sanjay Tirumalai
# Period: 4?

# ============================================================
# Python Skills Check — Slides 61–116
# CONDITIONALS & FUNCTIONS — CHALLENGE VERSION
# ============================================================

# DIRECTIONS
# ============================================================
# - I recommend you create a repo first and clone it.
# - Drag this file into your repo and push when you are done.
#
# Complete each task underneath its directions.
#
# RULES:
# - Use ONLY concepts we have learned in class.
# - Use the EXACT variable and function names provided.
# - Do not delete the directions.
# - Your entire Python file must run without errors.
# - Do NOT manually type an answer that Python should determine.
# - Pay attention to indentation.
# - Read carefully. MANY questions are intentionally tricky.
# - Unless a task says otherwise, do NOT use min() or max().
# - Your conditions should work even if the variable values are changed.
#
# IMPORTANT:
# Some questions are designed so that the ORDER of your conditions matters.
# Some questions have edge cases such as ties or boundary values.
# Test your logic carefully.


# ============================================================
# SECTION 1 — COMPARISON WARM-UP
# ============================================================

# TASK 1:
# Create:
#
number_one = 25
number_two = 40
#
# Write an if statement that prints:
#
# number_two is greater
#
# ONLY if number_two is greater than number_one.
if number_one < number_two:
    pass
# done haha

# TASK 2:
# Create:
#
score = 80
#
# Print:
# Passing score
#
# if score is GREATER THAN OR EQUAL TO 70.
if score >= 70:
    print("passing score\n\nman i always forget that python doesn't need semicolons at the end of everything\ni'm still going to put them there though");


# TASK 3:
# Create:
#
lives = 0
#
# Print:
# Game over
#
# ONLY if lives is exactly 0.
if lives == 0:
    print("game over\nhaha no capitalization l bozo");


# TASK 4:
# Create:
#
username = "student"
#
# Print:
# Different username
#
# ONLY if username is NOT equal to "admin".
if username != "admin":
    print("different username");


# ============================================================
# SECTION 2 — BOUNDARIES & ORDER MATTER
# ============================================================

# TASK 5:
# Create:
#
age = 18
#
# Print:
# Child       if age is under 13
# Teen        if age is 13 through 17
# Adult       if age is 18 through 64
# Senior      if age is 65 or older
#
# Use if / elif / else.
#
# THINK:
# Which condition should be checked first?
strage = "child"
if age >= 65:
    strage = 'senior'
elif age >= 18:
    strage = 'adult'
elif age >= 17:
    strage = 'teen'
else:
    pass
    # haha
print(strage);



# TASK 6:
# Create:
#
grade = 90
#
# Print:
# A if grade is 90 or higher
# B if grade is 80–89
# C if grade is 70–79
# D if grade is 60–69
# F if grade is below 60
#
# IMPORTANT:
# grade = 90 should print ONLY:
# A
sg = "F"
if grade >= 90:
    sg = 'A'
elif grade >= 80:
    sg = "B"
elif grade >= 70:
    sg = 'C'
elif grade >= 60:
    sg = 'D'
print(sg);


# TASK 7:
# Create:
#
temperature = 70

#
# Print:
# Cold       if below 50
# Mild       if 50 through 69
# Warm       if 70 through 89
# Hot        if 90 or higher
#
# Be careful with 50, 70, and 90.
t = "cold"
if temperature >= 90:
    t = 'hot'
elif temperature >= 70:
    t = 'warm'
elif temperature >= 50:
    t = 'mild'
print(t);


# TASK 8:
# Create:
#
speed = 65
#
# Print:
# Too Slow       if speed is below 25
# Normal         if speed is 25 through 65
# Speeding       if speed is 66 through 80
# Reckless       if speed is above 80
#
# The value 65 must print:
# Normal
# naw im good
dsp = 'too slow'
if speed >= 80:
    dsp = 'reckless'
elif speed >= 66:
    dsp = 'speeding'
elif speed >= 25:
    dsp = 'normal'
print(dsp);
    
# TASK 9:
# Create:
#
amount = 100
#
# Print:
# Small purchase       if amount is below 25
# Medium purchase      if amount is 25 through 99
# Large purchase       if amount is 100 through 499
# Huge purchase        if amount is 500 or more
#
# THINK carefully about your comparison operators.
amt = 'small'
amt2 = 'purchase'
if amount >= 500:
    amt = 'huge'
elif amount >= 100:
    amt = 'large'
elif amount >= 25:
    amt = 'medium'
print(amt, amt2)
    
# man i hate python
true = True
false = False
# ============================================================
# SECTION 3 — AND / OR THINKING
# ============================================================

# TASK 10:
# Create:
#
age = 16
has_ticket = True
#
# Print:
# You may enter
#
# ONLY if age is at least 13 AND has_ticket is True.
#
# Otherwise print:
# Entry denied
print('you may enter') if age >= 13 and has_ticket else print("entry denied")
# man python ternary operators


# TASK 11:
# Create:
#
temperature = 91
#
# Print:
# Extreme temperature
#
# if temperature is below 32 OR above 90.
#
# Otherwise print:
# Normal temperature
print("extreme temperature") if temperature > 90 or temperature < 32 else print("normal temperature")


# TASK 12:
# Create:
#
username = "admin"
password = "python123"
#
# Print:
# Access granted
#
# ONLY if BOTH values are correct.
#
# Otherwise print:
# Access denied
acs = "denied"
acs2 = 'access'
if username == "admin" and password == 'python123':
    acs = 'granted'
print(acs2, acs);

# TASK 13:
# Create:
#
age = 70
has_membership = False
#
# Print:
# Discount applies
#
# if the person is 65 or older OR has_membership is True.
#
# Otherwise print:
# No discount
print("discount applies") if age >= 65 or has_membership else print("no discount l bozo")


# TASK 14:
# Create:
#
number = 25
#
# Print:
# In range
#
# if number is from 10 through 30 INCLUDING 10 and 30.
#
# Otherwise print:
# Out of range
print("in range") if number >= 10 and number <= 30 else print("out of range")


# TASK 15:
# Create:
#
number = 10
#
# Print:
# Outside middle range
#
# if number is LESS THAN 20 OR GREATER THAN 80.
#
# Otherwise print:
# Inside middle range
#
# Test mentally with:
# 10
# 50
# 90
print("outside middle range") if number < 20 or number > 80 else print("inside middle range")


# ============================================================
# SECTION 4 — HIGHEST / LOWEST / MIDDLE
# ============================================================

# TASK 16:
# Create:
#
a = 12
b = 7
c = 19
#
# WITHOUT using max(), determine which variable contains
# the HIGHEST value.
#
# Print:
# a is highest
# OR
# b is highest
# OR
# c is highest

# i put the comments in backwards, look at find lowest loop and swap out lowest for highest ig
currenthilol = -2**1024
m = ''
stuff = {'a':a,'b':b, 'c':c}
for bruh in stuff:
    if stuff[bruh] > currenthilol:
        currenthilol = stuff[bruh]
        m = bruh
print(m, "is highest")
# dude idk man

# TASK 17:
# Create:
#
x = 44
y = 13
z = 28
#
# WITHOUT using min(), determine which variable contains
# the LOWEST value.
#
# Print the correct variable name followed by:
# is lowest

# current low is high number
currentlolol = 2**1024
# dictionary?
stuff = {'x':x,'y':y,"z":z}
# go through stuff, if value at key bruh less than currentlolol update new current low
for bruh in stuff:
    if stuff[bruh] < currentlolol:
        m = bruh
        currentlolol = stuff[bruh]
print(m, "is lowest")


# TASK 18:
# Create:
#
num1 = 10
num2 = 30
num3 = 20
#
# WITHOUT using min(), max(), or sorting,
# determine the MIDDLE value.
#
# Print:
# Middle: [value]
#
# HINT:
# The middle value is not the highest and not the lowest.
# ok loops might not work here idk

# mean of numbers
cm = (num1+num2+num3)/3
# difference from means
md1 = abs(num1 - cm)
md2 = abs(num2 - cm)
md3 = abs(num3 - cm)
# default to num1
nsi = num1
# check if difference of means is smaller than every other number?
if md3 < md2 and md3 < md1:
    nsi = num3
elif md2 < md1 and md2 < md3:
    nsi = num2
print(f"middle: {nsi}")





    



# TASK 19:
# Create:
#
first = 20
second = 20
third = 8
#
# Determine what is highest.
#
# Your program must correctly handle the tie.
#
# Possible outputs:
# first is highest
# second is highest
# third is highest
# first and second are tied for highest
# first and third are tied for highest
# second and third are tied for highest
# all three are tied

# smol hi
currenthilol = -2**1024
# states of current highness
tis = {"first ":false,"second ":false,'third ':false}
# if etc > etc2, etc.
if first >= second and first >= third:
    tis['first '] = true
if second >= first and second >= third:
    tis['second '] = true
if third >= first and third >= second:
    tis['third '] = true
# print the ones that are hi
print("highest:")
for bruh in tis:
    if tis[bruh]:
        print(bruh)
# this is good enough man




# TASK 20:
# Create:
#
first = 5
second = 5
third = 5
#
# Determine whether:
#
# - all three are equal
# - exactly two are equal
# - none are equal
#
# Print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# Your code should still work if the values are changed.

# a = b = c, a = c
# a != b != c, a != c, etc. i think
# then if the other thing happens
if first == second == third:
    print("all equal")
elif first != second and first != third and second != third:
    print("all different")
else:
    print("exactly 2 equal or i screwed something up")
    


# TASK 21:
# Create:
#
a = 9
b = 4
c = 9
#
# Determine whether AT LEAST TWO numbers match.
#
# Print:
# A match exists
#
# Otherwise print:
# No match

# a matchy matchy with a
# then check if b=c rsm
if a == b or a == c:
    print("a match exists")
elif b == c:
    print("a match exists")
else:
    print("no match")


# TASK 22:
# Create:
#
a = 14
b = 17
c = 20
#
# Determine whether a is BETWEEN b and c.
#
# Print:
# a is between b and c
#
# if that is true.
#
# Otherwise print:
# a is not between b and c
#
# IMPORTANT:
# Your code should still work if b is greater than c.

# i think b < a < c
if (a < c and a > b):
    print("a is between b and c")
# c < a < b
elif a < b and a > c:
    print("a is between b and c")
else:
    print("a is not between b and c")


# TASK 23:
# Create:
#
a = 50
b = 20
c = 80
#
# Determine whether b is the lowest AND c is the highest.
#
# If BOTH are true, print:
# Correct order
#
# Otherwise print:
# Different order

# c > b, a
# then b < c, a
# etc.
# can't you read this?
if c > b and c > a:
    if b < c and b < a:
        print("correct order")
    else:
        print("different order")
else:
    print("different order")

# i think

# ============================================================
# SECTION 5 — USER INPUT LOGIC
# ============================================================

# TASK 24:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# first_number
# second_number
# third_number
#
# WITHOUT using min() or max(), print the LOWEST number.

# large upper bound?
lost = 2**1024
# the input
number_string = input("enter 3 whole numbers separated by spaces: ")
# turn it into x, y, z, etc. etc.
numbers = number_string.split()
# yes
first_number = int(numbers[0])
second_number = int(numbers[1])
third_number = int(numbers[2])
# continuous updation?
if first_number < lost:
    lost = first_number
if second_number < lost:
    lost = second_number
if third_number < lost:
    lost = third_number
print(lost)



# TASK 25:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# value1
# value2
# value3
#
# WITHOUT using min() or max(), print the HIGHEST number.

# same thing but reversed kinda
lost = -2**1024
number_string = input("enter 3 whole numbers separated by spaces: ")
numbers = number_string.split()
value1 = int(numbers[0])
value2 = int(numbers[1])
value3 = int(numbers[2])
if value1 > lost:
    lost = value1
if value2 > lost:
    lost = value2
if value3 > lost:
    lost = value3
print(lost)


# TASK 26:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# n1
# n2
# n3
#
# Determine whether the user entered them in STRICTLY increasing order.

# shorthand for shorthanded shorthand probably but not really
numbers = input("enter 3 whole numbers separated by spaces: ").split()
n1 = int(numbers[0]); n2 = int(numbers[1]);  n3 = int(numbers[2])
if n2 > n1:
    if n3 > n2:
        print("increasing")
    else:
        print("not increasing")
else:
    print("not increasing")
# n3 > n1 right?

# Example: 3 4 5
# 3, 8, 10 -> Increasing
#
# 3, 3, 10 -> NOT Increasing
#
# Print:
# Increasing
# OR
# Not increasing


# TASK 27:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# n1
# n2
# n3
#
# Determine whether the numbers are in STRICTLY decreasing order.
#
# Print:
# Decreasing
# OR
# Not decreasing

numbers = input("enter 3 whole numbers separated by spaces: ").split()
n1 = int(numbers[0]); n2 = int(numbers[1]);  n3 = int(numbers[2])
if n1 < n2:
    if n2 < n3:
        print("decreasing")
    else:
        print("not decreasing")
else:
    print("not decreasing")


# TASK 28:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# a
# b
# c
#
# Print:
# All same
# if all three match
#
# Two same
# if exactly two match
#
# All different
# if none match
numbers = input("enter 3 whole numbers separated by spaces: ").split()
a = int(numbers[0]); b = int(numbers[1]);  c = int(numbers[2])
if a == b == c:
    print("all same")
elif (a == b or a == c) or (c == b):
    print("2 same")


# TASK 29:
# Ask the user for a score from 0 to 100.
#
# Store it in:
#
# user_score
#
# FIRST determine if the score is valid.
#
# If it is below 0 OR above 100, print:
# Invalid score
#
# Otherwise print the letter grade:
# A, B, C, D, or F
#
# THINK:
# You should not assign a letter grade to an invalid score.
lg = 'F'
user_score = int(input("enter score from 0 to 100: "))
if user_score < 0 or user_score > 100:
    print("invalid score")
else:
    if user_score >= 90:
        lg = 'a'
    elif user_score >= 80:
        lg = 'b'
    elif user_score >= 70:
        lg = 'c'
    elif user_score >= 60:
        lg = 'd'
    print(lg.upper())


# ============================================================
# SECTION 6 — FUNCTIONS BASICS
# ============================================================

# TASK 30:
# Create a function named:
#
# say_hello
#
# It should print:
# Hello!
#
# Call it once.
def say_hello():
    print("Hello!")


# TASK 31:
# Create a function named:
#
# greet_student
#
# Give it ONE parameter:
#
# name
#
# Print:
# Hello [name]
#
# Call it THREE times using different names.

def greet_student(name):
    print(f"Hello {name}")
greet_student("john")
greet_student("jon")
greet_student("chicken of the sea")


# TASK 32:
# Create a function named:
#
# add_three
#
# Give it THREE parameters:
#
# a
# b
# c
#
# Print the sum of all three.
#
# Call it at least TWO times.
def add_three(a, b, c):
    print(a+b+c)
add_three(1, 2, 3)
add_three(0, 0, 0)
# =======================================
# =====================
# SECTION 7 — FUNCTIONS + CONDITIONALS
# ============================================================

# TASK 33:
# Create a function named:
#
# check_number
#
# Give it ONE parameter:
#
# number
#
# Print:
# Positive
# Negative
# or
# Zero
#
# Call it using:
# 10
# -5
# 0
def check_number(number):
    if number < 0:
        print("negative")
    elif number > 0:
        print("positive")
    elif number == 0:
        print("zero")
    else:
        print("how did you manage to screw up your own function?")
check_number(10)
check_number(-5)
check_number(0)


# TASK 34:
# Create a function named:
#
# check_even_odd
#
# Give it ONE parameter:
#
# number
#
# Print:
# Even
# OR
# Odd
#
# Test it at least FOUR times.
def check_even_odd(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
check_even_odd(1)
check_even_odd(2)
check_even_odd(3)
check_even_odd(2**1024)


# TASK 35:
# Create a function named:
#
# ticket_type
#
# Give it ONE parameter:
#
# age
#
# Print:
# Child
# Teen
# Adult
# Senior
#
# using these ranges:
#
# Child: under 13
# Teen: 13–17
# Adult: 18–64
# Senior: 65+
#
# Test boundary values:
# 12
# 13
# 17
# 18
# 64
# 65
def ticket_type(age):
    ag = 'child'
    if age >= 65:
        ag = 'senior'
    elif age >= 18:
        ag = 'adult'
    elif age >= 13:
        ag = 'teen'
    print(ag)
ticket_type(12)
ticket_type(13)
ticket_type(17)
ticket_type(18)
ticket_type(64)
ticket_type(65)


# TASK 36:
# Create a function named:
#
# find_highest
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using max(), print the highest value.
#
# Test:
# find_highest(5, 20, 11)
# find_highest(100, 25, 60)
# find_highest(8, 9, 30)

def find_highest(aa, bb, cc):
    hist = -2**1024
    if aa > hist:
        hist = aa
    if bb > hist:
        hist = bb
    if cc > hist:
        hist = cc
    print(hist)

find_highest(5, 20, 11)
find_highest(100, 25, 60)
find_highest(8, 9, 30)

# TASK 37:
# Create a function named:
#
# find_lowest
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), print the lowest value.
#
# Test at least THREE times.
def find_lowest(a, b, c):
    lost = 2**1024
    if a < lost:
        lost = a
    if b < lost:
        lost = b
    if c < lost:
        lost = c
    print(lost)

# you should teach us about min and max now, i'm getting annoyed
find_lowest(999, 99, 3)
find_lowest(-123, 2, 2)
find_lowest(5**1024, 123, 3213123)

# TASK 38:
# Create a function named:
#
# find_middle
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), max(), or sorting,
# print the MIDDLE value.
#
# Test:
# find_middle(10, 30, 20)
# find_middle(100, 5, 50)
# find_middle(7, 9, 8)

# wait what do you mean by middle
# print(b)
# function's over lol
def find_middle(a, b, c):
    if (a > b and a < c) or (a > c and a < b):
        print(a)
    elif (b > c and b < a) or (b > a and b < c):
        print(b)
    elif (c > a and c < b) or (c > b and c < a):
        print(c)
    else:
        print(a)
    # this is badly done but it works man shshshsh

find_middle(10, 30, 20)
find_middle(100, 5, 50)
find_middle(7, 9, 8)



# TASK 39:
# Create a function named:
#
# compare_three
#
# Give it THREE parameters:
#
# a
# b
# c
#
# Print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# Test all three situations.

def compare_three(a, b, c):
    if a == b == c:
        print("all equal")
    elif a != b and a != c and b != c:
        print("all different")
    else:
        print("2 equal")

compare_three(1, 1, 1)
compare_three(1, 1, 2)
compare_three(1, 2, 0)
# TASK 40:
# Create a function named:
#
# is_in_range
#
# Give it THREE parameters:
#
# number
# low
# high
#
# Print:
# In range
#
# if number is between low and high INCLUDING the endpoints.
#
# Otherwise print:
# Out of range
#
# IMPORTANT:
# Your function should still work if low and high
# are accidentally passed in backwards.
#
# Example:
# is_in_range(50, 100, 1)
#
# should still print:
# In range
def is_in_range(number, low, high):
    if low < high:
        if number <= high and number >= low:
            print("in range")
        else:
            print("out of range")
    elif low > high:
        if high <= number <= low:
            print("in range")
        else:
            print("out of range")
    else:
        print("no")

# uh did you tell me to use the function?
# you just gave me an example, it's like telling me here's an apple and not telling me what to do with the apple
# cmon man!



# ============================================================
# SECTION 8 — RETURN VALUES
# ============================================================

# TASK 41:
# Create a function named:
#
# multiply_numbers
#
# Give it TWO parameters:
#
# num1
# num2
#
# RETURN their product.
#
# Store the result of:
# multiply_numbers(6, 7)
#
# inside:
# multiplication_result
#
# Print multiplication_result.
def multiply_numbers(num1, num2):
    return num1*num2
multiplication_result = multiply_numbers(6, 7)
# you do realize we don't have to reinvent the wheel right?
print(multiplication_result)


# TASK 42:
# Create a function named:
#
# larger_number
#
# Give it TWO parameters:
#
# a
# b
#
# RETURN the larger value.
#
# If they are equal, RETURN that value.
#
# Store the result of:
# larger_number(15, 40)
#
# inside:
# bigger
#
# Print bigger.
def larger_number(a, b):
    if a > b:
        return a
    if b > a:
        return b
    else:
        return (a+b)/2

bigger = larger_number(15, 40)
print(bigger)


# TASK 43:
# Create a function named:
#
# highest_of_three
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using max(), RETURN the highest value.
#
# Store:
# highest_of_three(18, 42, 27)
#
# inside:
# highest_result
#
# Print highest_result.

# dude you've made us do this like 3 times already BRO!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def highest_of_three(a, b, c):
    hist = -2**1024
    if a > hist:
        hist = a
    if b > hist:
        hist = b
    if c > hist:
        hist = c
    return hist
highest_result = highest_of_three(18, 42, 27)
print(highest_result)
# i swear bruh i actually js copied the find_highest stuff

# TASK 44:
# Create a function named:
#
# lowest_of_three
#
# Give it THREE parameters:
#
# a
# b
# c
#
# WITHOUT using min(), RETURN the lowest value.
#
# Test it at least THREE times.
def lowest_of_three(a, b, c):
    lost = 2**1024
    if a < lost:
        lost = a
    if b < lost:
        lost = b
    if c < lost:
        lost = c
    return lost
# im bout to TWEAK
print(lowest_of_three(0, 1, 3))
print(lowest_of_three(0, 21, 3))
print(lowest_of_three(3, 1, 3123))

# TASK 45:
# Create a function named:
#
# middle_of_three
#
# Give it THREE parameters:
#
# a
# b
# c
#
# RETURN the middle value.
#
# Do NOT use min(), max(), or sorting.
#
# Test:
def middle_of_three(a, b, c):
    if (a > b and a < c) or (a > c and a < b):
        return a
    elif (b > c and b < a) or (b > a and b < c):
        return b
    elif (c > a and c < b) or (c > b and c < a):
        return c
    else:
        return a
    # RAH

middle_of_three(10, 30, 20)
middle_of_three(50, 5, 25)
middle_of_three(8, 7, 9)


# ============================================================
# SECTION 9 — RETURN + REUSE
# ============================================================

# TASK 46:
# Create a function named:
#
# get_highest
#
# Give it THREE parameters and RETURN the highest number.
#
# Then create another function named:
#
# get_lowest
#
# Give it THREE parameters and RETURN the lowest number.
#
# Use:
#
# a = 30
# b = 10
# c = 20
#
# Store the returned values in:
#
# highest
# lowest
#
# Then calculate:
#
# difference
#
# by subtracting lowest from highest.
#
# Print difference.
#
# IMPORTANT:
# Do NOT repeat the highest/lowest logic outside the functions.

# you have actually got to be kidding me.
# oh wait you didn't say don't use min max or sort this is a gift from GOD i mean EVOLUTION

def get_highest(a, b, c):
    return max([a, b, c])
highest = get_highest(30, 10, 20)
def get_lowest(a, b, c):
    return min([a, b, c])
lowest = get_lowest(30, 10, 20)
difference = highest - lowest
# wdym dont repeat logic?
print(difference)


# TASK 47:
# Create:
#
a = 9
b = 4
c = 15
#
# Use your get_highest() and get_lowest() functions from above.
#
# Store both returned values.
#
# Then determine if the difference between highest and lowest
# is greater than 10.
#
# Print:
# Large spread
#
# or:
# Small spread
bigboy = get_highest(a, b, c)
smallboy = get_lowest(a, b, c)
print("large spread") if bigboy - smallboy > 10 else print("small spread")


# TASK 48:
# Create a function named:
#
# best_of_two
#
# Give it TWO parameters and RETURN the larger value.
#
# Then use it to determine the highest of THREE numbers
# WITHOUT writing a new three-number comparison.
#
# You should call best_of_two() more than once.
#
# Use:
a = 12
b = 50
c = 31
#
# Store the final answer in:
#
# highest
#
# Print highest.
#
# THINK:
# How can one function call feed into another?
def best_of_two(a, b):
    return max(a, b)
highest = best_of_two(best_of_two(a, b,c))
print(highest)



# TASK 49:
# Create a function named:
#
# worst_of_two
#
# Give it TWO parameters and RETURN the smaller value.
#
# Use it more than once to find the LOWEST of:
#
a = 22
b = 5
c = 17
#
# Store the final result in:
#
# lowest
#
# Print lowest.
def worst_of_two(ar, br):
    return min(ar, br)
lowest = worst_of_two(c,worst_of_two(a, b))
print(lowest)



# ============================================================
# SECTION 10 — LOGIC CHALLENGES
# ============================================================

# TASK 50:
# Create:
#
a = 12
b = 7
c = 19
#
# Determine whether b is the MIDDLE value.
#
# Print:
# b is middle
#
# or:
# b is not middle
#
# Do NOT calculate the middle value separately first.
print("b is middle") if (b < a and b > c) or (b < c and b > a) else print("b is not middle")


# TASK 51:
# Create:
#
a = 25
b = 25
c = 10
#
# Determine whether the HIGHEST value appears more than once.
#
# Print:
# Highest is tied
#
# or:
# Highest is unique
i = [a, b, c]
m = i.pop(i.index(max(i)))
if (m == i[0] or m == i[1]):
    print("highest is tied")
else:
    print("highest is unique")



# TASK 52:
# Create:
#
a = 3
b = 8
c = 5
#
# Determine whether the numbers are:
#
# Strictly increasing
# Strictly decreasing
# Neither
#
# Print ONE result.
z = [a, b, c]
i = sorted(z)
d = sorted(z, reverse=True)
if z[0] == z[1] == z[2] or (i[2] == i[1]) or (i[0] == i[1]):
    print("neither")
elif z == i:
    print("strictly increasing")
elif d == z:
    print("strictly decreasing")


# TASK 53:
# Create:
#
a = 5
b = 5
c = 10
#
# Determine whether the values are in NON-DECREASING order.
#
# This means each value may stay the same or get larger.
#
# Examples:
# 3, 3, 7 -> yes
# 3, 7, 7 -> yes
# 3, 7, 2 -> no
#
# Print:
# Non-decreasing
# OR
# Not non-decreasing
# decreasing?
z = [a, b, c]
h = sorted(z)
if z == h:
    print("non decreasing")
else:
    print("not non-decreasing")


# TASK 54:
# Create:
#
# age = 17
# has_permission = True
# has_ticket = False
#
# A person may enter if:
#
# - they are 18 or older
#
# OR
#
# - they are under 18 AND have_permission is True AND have_ticket is True
#
# Print:
# Entry allowed
#
# or:
# Entry denied
#
# Read this one carefully.


# TASK 55:
# Create:
#
# score = 88
# attendance = 92
#
# Print:
# Honors
#
# if score is at least 90 AND attendance is at least 90.
#
# Print:
# Pass
#
# if score is at least 70 AND attendance is at least 75,
# but the student did not qualify for Honors.
#
# Otherwise print:
# Fail
#
# Only ONE message should print.


# ============================================================
# SECTION 11 — DEBUGGING CHALLENGES
# ============================================================

# TASK 56:
# The programmer wants exactly ONE result.
#
# Fix the code so score = 95 prints ONLY:
#
# Excellent
#
# score = 95
#
# if score >= 70:
#     print("Passing")
# if score >= 90:
#     print("Excellent")


# TASK 57:
# The programmer wants 18 to count as Adult.
#
# Fix the logic.
#
# age = 18
#
# if age > 18:
#     print("Adult")
# else:
#     print("Minor")


# TASK 58:
# The programmer wants numbers from 10 through 20,
# INCLUDING 10 and 20, to print:
#
# Valid
#
# Fix the condition.
#
# number = 20
#
# if number > 10 and number < 20:
#     print("Valid")
# else:
#     print("Invalid")


# TASK 59:
# The programmer wants the function to RETURN the answer.
#
# Fix it.
#
# def add_numbers(a, b):
#     total = a + b
#     print(total)
#
# result = add_numbers(4, 6)
# print(result)


# TASK 60:
# Fix the function so the variable result works outside
# of the function.
#
# def subtract(a, b):
#     answer = a - b
#
# result = subtract(20, 8)
# print(result)


# ============================================================
# FINAL BOSS 1 — THREE NUMBER ANALYZER
# ============================================================

# TASK 61:
# Create a function named:
#
# analyze_three_numbers
#
# Give it THREE parameters:
#
# a
# b
# c
#
# It must:
#
# 1. Determine the highest value.
# 2. Determine the lowest value.
# 3. Determine the middle value.
# 4. Determine whether all three are equal.
# 5. Determine whether exactly two are equal.
#
# Print:
#
# Highest: [value]
# Lowest: [value]
# Middle: [value]
#
# Then print ONE of:
#
# All equal
# Exactly two equal
# All different
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Test:
# analyze_three_numbers(8, 3, 15)
# analyze_three_numbers(20, 20, 20)
# analyze_three_numbers(5, 5, 9)
# analyze_three_numbers(-5, 0, -12)


# ============================================================
# FINAL BOSS 2 — NUMBER RANKING
# ============================================================

# TASK 62:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# user_num1
# user_num2
# user_num3
#
# Print the numbers from LOWEST to HIGHEST.
#
# Example:
# User enters:
# 30
# 10
# 20
#
# Output:
# 10
# 20
# 30
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Your program must still work if the order of inputs changes.


# ============================================================
# FINAL BOSS 3 — FUNCTION REUSE
# ============================================================

# TASK 63:
# Create these THREE functions:
#
# get_highest(a, b, c)
# get_lowest(a, b, c)
# get_middle(a, b, c)
#
# Each function must RETURN the correct value.
#
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# first
# second
# third
#
# Call all three functions.
#
# Store the returned results in:
#
# highest
# lowest
# middle
#
# Then print:
#
# Highest: [highest]
# Middle: [middle]
# Lowest: [lowest]
#
# Do NOT use min(), max(), or sorting.


# ============================================================
# FINAL BOSS 4 — CONDITIONAL DECISION SYSTEM
# ============================================================

# TASK 64:
# Create a function named:
#
# admission_decision
#
# Give it THREE parameters:
#
# grade
# attendance
# interview
#
# Rules:
#
# - If grade is 90 or higher AND attendance is 90 or higher,
#   print "Accepted"
#
# - Otherwise, if grade is 80 or higher AND attendance is 80 or higher
#   AND interview is "pass", print "Accepted"
#
# - Otherwise print "Not accepted"
#
# Test:
#
# admission_decision(95, 95, "fail")
# admission_decision(85, 85, "pass")
# admission_decision(85, 85, "fail")
# admission_decision(75, 100, "pass")
#
# THINK:
# The first person should still be accepted even though
# the interview value is "fail".


# ============================================================
# FINAL BOSS 5 — THINK CAREFULLY
# ============================================================

# TASK 65:
# Create:
#
# a = 15
# b = 8
# c = 15
#
# Your program must determine BOTH:
#
# 1. The highest value
# 2. Whether that highest value is unique or tied
#
# Print:
#
# Highest: [value]
#
# Then print ONE of:
#
# Unique highest
# Tied highest
#
# RESTRICTIONS:
# - Do NOT use min()
# - Do NOT use max()
# - Do NOT use sorting
#
# Your logic should still work if the variable values change.




# ============================================================
# SECTION 12 — LEETCODE-STYLE REAL PROBLEM CHALLENGES
# ============================================================
#
# These problems are intentionally DIFFERENT from the earlier tasks.
# Instead of simply asking you to find the highest number, check a range,
# or assign a grade, each problem gives you a small situation to solve.
#
# RULES:
# - Use the EXACT function name and parameters given.
# - Do NOT use input() unless the problem specifically tells you to.
# - RETURN the answer unless the problem specifically tells you to print.
# - Your function must work for ALL valid test cases.
# - Do NOT hard-code the example answers.
# - Use only concepts covered in class.
# - Test every example after writing your function.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 66 — TEMPERATURE CONVERTER
# ------------------------------------------------------------
#
# Write a function named:
#
# convert_temperature
#
# Parameters:
#
# temperature
# scale
#
# The scale will be either:
#
# "C"
# or
# "F"
#
# If scale is "C", the temperature given is Celsius.
# Convert it to Fahrenheit using:
#
# Fahrenheit = Celsius * 1.8 + 32
#
# If scale is "F", the temperature given is Fahrenheit.
# Convert it to Celsius using:
#
# Celsius = (Fahrenheit - 32) / 1.8
#
# RETURN the converted temperature.
#
# Examples:
#
# convert_temperature(0, "C")      -> 32
# convert_temperature(100, "C")    -> 212
# convert_temperature(32, "F")     -> 0
# convert_temperature(68, "F")     -> 20
#
# CHALLENGE:
# The same function must be able to convert in BOTH directions.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 67 — KELVIN CONVERTER
# ------------------------------------------------------------
#
# Write a function named:
#
# to_kelvin
#
# Parameters:
#
# temperature
# scale
#
# If scale is "C":
#
# Kelvin = Celsius + 273.15
#
# If scale is "F":
#
# First convert Fahrenheit to Celsius:
#
# Celsius = (Fahrenheit - 32) / 1.8
#
# Then convert Celsius to Kelvin.
#
# RETURN the Kelvin temperature.
#
# Examples:
#
# to_kelvin(0, "C")     -> 273.15
# to_kelvin(100, "C")   -> 373.15
# to_kelvin(32, "F")    -> 273.15
# to_kelvin(212, "F")   -> 373.15
#
# THINK:
# One input can require TWO calculations before you return the answer.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 68 — PARKING GARAGE
# ------------------------------------------------------------
#
# Write a function named:
#
# parking_cost
#
# Parameter:
#
# hours
#
# Parking costs:
#
# First hour: $5
# Each additional hour: $3
#
# If the car is parked for more than 8 hours,
# the maximum daily charge is $25.
#
# RETURN the total parking cost.
#
# Examples:
#
# parking_cost(1)   -> 5
# parking_cost(2)   -> 8
# parking_cost(5)   -> 17
# parking_cost(9)   -> 25
# parking_cost(20)  -> 25
#
# THINK:
# Do not accidentally charge $3 for the first hour.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 69 — MOVIE TICKET TOTAL
# ------------------------------------------------------------
#
# Write a function named:
#
# movie_total
#
# Parameters:
#
# age
# is_weekend
#
# Ticket prices:
#
# Under 13: $8
# Ages 13–64: $12
# Age 65+: $7
#
# On weekends, add $3 to the ticket price.
#
# RETURN the final ticket price.
#
# Examples:
#
# movie_total(10, False)  -> 8
# movie_total(10, True)   -> 11
# movie_total(30, False)  -> 12
# movie_total(70, True)   -> 10
#
# THINK:
# First determine the base ticket price.
# Then decide whether something must be added.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 70 — ELECTRIC BILL
# ------------------------------------------------------------
#
# Write a function named:
#
# electric_bill
#
# Parameter:
#
# usage
#
# The bill is calculated using these rules:
#
# 0–100 units:
# $0.10 per unit
#
# More than 100 units:
# The first 100 units cost $0.10 each.
# Every unit AFTER 100 costs $0.20 each.
#
# RETURN the total bill.
#
# Examples:
#
# electric_bill(50)   -> 5.0
# electric_bill(100)  -> 10.0
# electric_bill(120)  -> 14.0
# electric_bill(200)  -> 30.0
#
# IMPORTANT:
# For 120 units, only 20 units should be charged at $0.20.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 71 — LEAP YEAR
# ------------------------------------------------------------
#
# Write a function named:
#
# is_leap_year
#
# Parameter:
#
# year
#
# A year is a leap year if:
#
# - it is divisible by 400
#
# OR
#
# - it is divisible by 4 BUT NOT divisible by 100
#
# RETURN True if it is a leap year.
# Otherwise RETURN False.
#
# Examples:
#
# is_leap_year(2024)  -> True
# is_leap_year(2025)  -> False
# is_leap_year(1900)  -> False
# is_leap_year(2000)  -> True
#
# This problem is intentionally tricky.
#
# THINK:
# A year divisible by 100 is NOT automatically a leap year.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 72 — TRIANGLE VALIDITY
# ------------------------------------------------------------
#
# Write a function named:
#
# valid_triangle
#
# Parameters:
#
# a
# b
# c
#
# Three side lengths can form a triangle only if:
#
# a + b > c
# a + c > b
# b + c > a
#
# ALL THREE conditions must be true.
#
# RETURN True if the sides can form a triangle.
# Otherwise RETURN False.
#
# Examples:
#
# valid_triangle(3, 4, 5)   -> True
# valid_triangle(5, 5, 5)   -> True
# valid_triangle(1, 2, 10)  -> False
# valid_triangle(2, 3, 5)   -> False
#
# Notice that 2 + 3 = 5 is NOT enough.
# It must be GREATER THAN.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 73 — TRIANGLE TYPE
# ------------------------------------------------------------
#
# Write a function named:
#
# triangle_type
#
# Parameters:
#
# a
# b
# c
#
# First, determine whether the three sides form a valid triangle.
#
# If they do NOT, RETURN:
#
# "invalid"
#
# If all three sides are equal, RETURN:
#
# "equilateral"
#
# If exactly two sides are equal, RETURN:
#
# "isosceles"
#
# Otherwise RETURN:
#
# "scalene"
#
# Examples:
#
# triangle_type(3, 3, 3)   -> "equilateral"
# triangle_type(5, 5, 8)   -> "isosceles"
# triangle_type(3, 4, 5)   -> "scalene"
# triangle_type(1, 2, 10)  -> "invalid"
#
# THINK:
# Check whether the triangle is valid BEFORE classifying it.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 74 — ROCK PAPER SCISSORS
# ------------------------------------------------------------
#
# Write a function named:
#
# rps_winner
#
# Parameters:
#
# player1
# player2
#
# Each argument will be:
#
# "rock"
# "paper"
# or
# "scissors"
#
# RETURN:
#
# "tie"
#
# if both players choose the same thing.
#
# RETURN:
#
# "player1"
#
# if player 1 wins.
#
# RETURN:
#
# "player2"
#
# if player 2 wins.
#
# Rules:
#
# rock beats scissors
# scissors beats paper
# paper beats rock
#
# Examples:
#
# rps_winner("rock", "scissors")  -> "player1"
# rps_winner("paper", "rock")     -> "player1"
# rps_winner("rock", "paper")     -> "player2"
# rps_winner("paper", "paper")    -> "tie"
#
# This is a logic problem.
# There are several possible combinations.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 75 — CLOSEST TO 100
# ------------------------------------------------------------
#
# Write a function named:
#
# closest_to_100
#
# Parameters:
#
# a
# b
#
# RETURN whichever number is closer to 100.
#
# If they are equally far away from 100, RETURN:
#
# -1
#
# Examples:
#
# closest_to_100(90, 80)    -> 90
# closest_to_100(105, 120)  -> 105
# closest_to_100(90, 110)   -> -1
#
# RESTRICTION:
# Do NOT use abs().
#
# THINK:
# A number may be above OR below 100.
# You will need to determine each number's distance from 100.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 76 — DELIVERY FEE
# ------------------------------------------------------------
#
# Write a function named:
#
# delivery_fee
#
# Parameters:
#
# order_total
# distance
#
# Rules:
#
# If order_total is $50 or more AND distance is 5 miles or less:
# RETURN 0
#
# Otherwise, if distance is 5 miles or less:
# RETURN 5
#
# Otherwise:
# RETURN 10
#
# Examples:
#
# delivery_fee(60, 3)  -> 0
# delivery_fee(30, 3)  -> 5
# delivery_fee(60, 8)  -> 10
# delivery_fee(30, 8)  -> 10
#
# THINK:
# A large order does NOT always mean free delivery.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 77 — ATM WITHDRAWAL
# ------------------------------------------------------------
#
# Write a function named:
#
# can_withdraw
#
# Parameters:
#
# balance
# amount
#
# A withdrawal is allowed only if:
#
# - amount is greater than 0
# - amount is less than or equal to balance
# - amount is divisible by 20
#
# RETURN True if the withdrawal is allowed.
# Otherwise RETURN False.
#
# Examples:
#
# can_withdraw(500, 100)  -> True
# can_withdraw(500, 125)  -> False
# can_withdraw(50, 100)   -> False
# can_withdraw(500, 0)    -> False
#
# ALL conditions must be true.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 78 — RESTAURANT TIP
# ------------------------------------------------------------
#
# Write a function named:
#
# tip_amount
#
# Parameters:
#
# bill
# service
#
# service will be:
#
# "poor"
# "good"
# or
# "excellent"
#
# Tip rules:
#
# poor       -> 10%
# good       -> 18%
# excellent  -> 25%
#
# RETURN the tip amount.
#
# Examples:
#
# tip_amount(100, "poor")       -> 10
# tip_amount(100, "good")       -> 18
# tip_amount(100, "excellent")  -> 25
# tip_amount(80, "good")        -> 14.4
#
# THINK:
# RETURN only the TIP, not the final bill.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 79 — PHONE BATTERY WARNING
# ------------------------------------------------------------
#
# Write a function named:
#
# battery_status
#
# Parameters:
#
# battery
# is_charging
#
# RETURN:
#
# "critical"
# if battery is 5 or lower AND it is NOT charging
#
# "low"
# if battery is 20 or lower AND it is NOT charging
#
# "charging"
# if is_charging is True
#
# "normal"
# otherwise
#
# Examples:
#
# battery_status(3, False)   -> "critical"
# battery_status(15, False)  -> "low"
# battery_status(3, True)    -> "charging"
# battery_status(80, False)  -> "normal"
#
# THINK:
# The order of the conditions matters.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 80 — TAXI FARE
# ------------------------------------------------------------
#
# Write a function named:
#
# taxi_fare
#
# Parameters:
#
# miles
# is_night
#
# Fare rules:
#
# Base fare: $4
# Each mile: $2
#
# If is_night is True, add a $5 night fee.
#
# RETURN the total fare.
#
# Examples:
#
# taxi_fare(0, False)  -> 4
# taxi_fare(5, False)  -> 14
# taxi_fare(5, True)   -> 19
#
# Build the final answer from the rules instead of
# hard-coding different totals.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 81 — GAME DAMAGE
# ------------------------------------------------------------
#
# Write a function named:
#
# calculate_damage
#
# Parameters:
#
# attack
# defense
# critical
#
# First calculate:
#
# damage = attack - defense
#
# If damage would be less than 0, damage becomes 0.
#
# If critical is True, DOUBLE the damage.
#
# RETURN the final damage.
#
# Examples:
#
# calculate_damage(20, 5, False)  -> 15
# calculate_damage(20, 5, True)   -> 30
# calculate_damage(5, 20, False)  -> 0
# calculate_damage(5, 20, True)   -> 0
#
# THINK:
# The critical hit should happen AFTER defense is removed.


# ------------------------------------------------------------
# LEETCODE-STYLE TASK 82 — STORE COUPON
# ------------------------------------------------------------
#
# Write a function named:
#
# final_price
#
# Parameters:
#
# price
# coupon
#
# coupon will be:
#
# "none"
# "SAVE10"
# "SAVE25"
#
# Rules:
#
# "none"   -> no discount
# "SAVE10" -> 10% off
# "SAVE25" -> 25% off
#
# RETURN the FINAL price after the discount.
#
# Examples:
#
# final_price(100, "none")    -> 100
# final_price(100, "SAVE10")  -> 90
# final_price(100, "SAVE25")  -> 75
# final_price(80, "SAVE25")   -> 60
#
# THINK:
# A 25% discount means the customer pays 75% of the price.


# ============================================================
# GIT CHECK
# ============================================================

# When you are completely finished:
#
# 1. Save your file.
# 2. Run your ENTIRE program.
# 3. Fix all errors.
# 4. Make sure you can explain your code.
#
# Then use:
#
# git status
# git add .
# git commit -m "Complete conditionals and functions challenge"
# git push
