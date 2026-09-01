# Name: 
# Period:
# Python Skills Check — Slides 1–60

# ============================================================
# DIRECTIONS
# ============================================================
# - I recommend you create a repo first and clone it.
# - Drag this folder into your repo and then push when you are done.
#
#
# Complete each task underneath its directions.
# 
#
# RULES:
# - Use ONLY concepts we have learned in class.
# - Use the EXACT variable names provided.
# - Do not delete the directions.
# - Your entire Python file must run without errors.
# - Do NOT manually type an answer that Python should calculate.
# - Read carefully. Some questions are intentionally tricky.


# ============================================================
# SECTION 1 — COMMENTS & PRINTING
# ============================================================

# TASK 1:
# Below this comment, write a SINGLE-LINE comment that says:
#
# This is my first comment

# This is my first comment



# TASK 2:
# Below, use print() to display:
#
# Python Skills Check
#
# Make sure Python treats the words as text.

print("Python Skills Check")



# TASK 3:
# Write THREE separate print() statements.
#
# Print:
#
# Your first name
# Your favorite food
# A number between 1 and 100
#
# IMPORTANT:
# The first two should be text.
# The third should be a number.
print("Your first name")
print("Your favorite food")
print("A number between 1 and 100")



# ============================================================
# SECTION 2 — CREATING VARIABLES
# ============================================================

# TASK 4:
# Below, create a variable named:
#
# student_name
#
# Store YOUR name inside the variable.

student_name = "Sanjay \"King of Autism\" Tirumalai"


# TASK 5:
# Create a variable named:
#
# student_age
#
# Store your age as an INTEGER.
#
# Do NOT put quotation marks around the value.

student_age = 16


# TASK 6:
# Create a variable named:
#
# account_balance
#
# Give it the value:
#
# 125.75
#
# Think about what type of data this is.

account_balance = 125.75



# TASK 7:
# Create a variable named:
#
# is_learning_python
#
# Store the Boolean value True inside it.
#
# Be careful with capitalization and quotation marks.

is_learning_python = True



# TASK 8:
# Print all FOUR variables you created in Tasks 4–7.
#
# Use four separate print() statements.
#
# IMPORTANT:
# Print the VALUES stored in the variables,
# not the names of the variables.

print(f"""
{student_name}
{student_age}
{account_balance}
{is_learning_python}
""")



# ============================================================
# SECTION 3 — DATA TYPES
# ============================================================

# TASK 9:
# Create these FOUR variables:
#
# whole_number
# decimal_number
# message
# answer
#
# Store a DIFFERENT type of data in each:
#
# whole_number should store an Integer.
# decimal_number should store a decimal.
# message should store a String.
# answer should store a Boolean.
#
# You choose the values.

whole_number = 1
decimal_number = 1.1
message = "1"
answer = True




# TASK 10:
# Create a variable named:
#
# tricky_number
#
# Store:
#
# "500"
#
# EXACTLY as shown above.
#
# THINK:
# Is tricky_number storing a number that Python can currently
# perform arithmetic with, or is it storing a String?

tricky_number = "500"



# TASK 11:
# Print tricky_number.
#
# Then, directly underneath it, create another variable named:
#
# actual_number
#
# Store the INTEGER 500 inside actual_number.
#
# Print actual_number.
#
# The output may look similar, but the two variables
# should NOT contain the same data type.
print(tricky_number)
actual_number = 500
print(actual_number)



# ============================================================
# SECTION 4 — ARITHMETIC WITH VARIABLES
# ============================================================

# TASK 12:
# Create:
#
# number_one = 45
# number_two = 17
#
# Create another variable named:
#
# total
#
# Use number_one and number_two to calculate their sum.
#
# Do NOT write:
#
# total = 62
#
# Python must perform the calculation.
number_one = 45
number_two = 17
total = number_one + number_two

# TASK 13:
# Using the SAME number_one and number_two variables,
# create:
#
# difference
#
# Store the result of subtracting number_two
# from number_one.
difference = number_one - number_two



# TASK 14:
# Using the SAME variables again, create:
#
# product
#
# Store the result of multiplying the two numbers.

product = number_one * number_two



# TASK 15:
# Using the SAME variables again, create:
#
# quotient
#
# Store the result of dividing number_one by number_two.

quotient = number_one / number_two



# TASK 16:
# Print:
#
# total
# difference
# product
# quotient
#
# Use four separate print statements.
print(total)
print(difference)
print(product)
print(quotient)



# ============================================================
# SECTION 5 — CALCULATIONS THAT REQUIRE THINKING
# ============================================================

# TASK 17:
# Create:
#
# price = 14
# quantity = 7
#
# Create:
#
# purchase_total
#
# Determine what arithmetic operation should be used
# to calculate the cost of buying 7 items.
#
# Do NOT manually type the answer.

price = 14
quantity = 7
purchase_total = price * quantity



# TASK 18:
# Create:
#
# money = 500
# people = 8
#
# Create:
#
# money_per_person
#
# Imagine the money is divided equally between everyone.
#
# Determine the correct calculation yourself.
# ???
money = 500
people = 8
money_per_person = money/people



# TASK 19:
# Create:
#
# starting_balance = 850
# amount_spent = 237
#
# Create:
#
# remaining_balance
#
# Determine how much money remains.
#
# Use the variables in your calculation.

starting_balance = 850
amount_spent = 237
remaining_balance = starting_balance - amount_spent

# TASK 20:
# Create:
#
# boxes = 12
# items_per_box = 24
#
# Create:
#
# total_items
#
# Calculate the total number of items.
#
# Do NOT manually calculate the answer.

boxes = 12
items_per_box = 24
total_items = items_per_box * boxes



# ============================================================
# SECTION 6 — REUSING VARIABLES
# ============================================================

# TASK 21:
# Create:
#
# hourly_pay = 20
# hours_worked = 8
#
# Create:
#
# daily_pay
#
# Calculate one day's pay.

hourly_pay = 20
hours_worked = 8
daily_pay = hourly_pay * hours_worked



# TASK 22:
# Now create:
#
# weekly_pay
#
# Assume the person works 5 days.
#
# REQUIREMENT:
# You MUST use daily_pay in your calculation.
#
# Do NOT redo the calculation from Task 21.

weekly_pay = daily_pay * 5



# TASK 23:
# Create:
#
# monthly_pay
#
# For this question, assume there are 4 work weeks
# in a month.
#
# REQUIREMENT:
# Use weekly_pay.
#
# Do NOT use hourly_pay or hours_worked in this calculation.
monthly_pay = weekly_pay * 4



# TASK 24:
# Create:
#
# yearly_pay
#
# For this question, assume there are 12 months in a year.
#
# REQUIREMENT:
# Your calculation may ONLY use:
#
# monthly_pay
#
# and one number.

yearly_pay = monthly_pay * 12



# ============================================================
# SECTION 7 — STRINGS
# ============================================================

# TASK 25:
# Create:
#
# first_name
# last_name
#
# Store your first and last name as Strings.
first_name = "Sanjay"
last_name = "Tirumalai"



# TASK 26:
# Create:
#
# full_name
#
# Combine first_name and last_name together.
#
# There MUST be a space between the names.
#
# REQUIREMENT:
# Use the two variables.
#
# Do NOT manually type your full name again.
full_name = first_name + " " + last_name



# TASK 27:
# Print full_name.
print(full_name)


# TASK 28:
# Create:
#
# word_one = "Python"
# word_two = "Programming"
#
# Create:
#
# course_name
#
# Combine the two variables so the result displays:
#
# Python Programming
#
# You may NOT manually type "Python Programming"
# into course_name.
word_one = "Python"; word_two = "Programming"



# ============================================================
# SECTION 8 — USER INPUT
# ============================================================

# TASK 29:
# Create:
#
# user_name
#
# Ask the user to enter their name.
#
# Store their answer inside user_name.

user_name = input("enter name: ")


# TASK 30:
# Print a message that says:
#
# Hello [their name]
#
# REQUIREMENT:
# Use user_name.
#
# The program must work no matter what name is entered.

print(f"Hello {user_name}")



# TASK 31:
# Create:
#
# favorite_food
#
# Ask the user for their favorite food.
favorite_food = input("favorite food: ")



# TASK 32:
# Create a personalized message using:
#
# user_name
# favorite_food
#
# Your output should use BOTH answers.
#
# Example idea:
#
# Alex likes pizza.
#
# Do NOT manually type the user's answers.
print(f"{user_name}'s favorite food is {favorite_food}")


# ============================================================
# SECTION 9 — INPUT + DATA CONVERSION
# ============================================================

# TASK 33:
# Ask the user:
#
# How old are you?
#
# Store the answer inside:
#
# user_age
#
# IMPORTANT:
# You are going to perform arithmetic with this value.
#
# Remember that input() gives you a String.
# Figure out what conversion is needed.

user_age = int(input("enter age: "))



# TASK 34:
# Create:
#
# age_next_year
#
# Calculate how old the user will be next year.
#
# REQUIREMENT:
# Use user_age.
#
# Do NOT ask for their age again.
age_next_year = 1 + user_age




# TASK 35:
# Create:
#
# age_in_ten_years
#
# Calculate how old the SAME user will be 10 years from now.
#
# Do NOT ask another question.
age_in_ten_years = user_age + 10



# ============================================================
# SECTION 10 — MULTIPLE USER INPUTS
# ============================================================

# TASK 36:
# Ask the user to enter a whole number.
#
# Store it inside:
#
# first_user_number
#
# Make sure Python can perform arithmetic with it.
first_user_number = int(input("enter whole number: "))



# TASK 37:
# Ask the user for another whole number.
#
# Store it inside:
#
# second_user_number
second_user_number = int(input("enter another whole number: "))



# TASK 38:
# Using ONLY those two variables, create:
#
# user_sum
# user_difference
# user_product
# user_quotient
#
# Each variable should contain the result of a
# DIFFERENT arithmetic operation.
user_sum = first_user_number + second_user_number
user_difference = first_user_number - second_user_number; user_product = first_user_number * second_user_number
user_quotient = first_user_number / second_user_number



# TASK 39:
# Print all four answers.
#
# Your program must work with different numbers entered
# by different users.
print(f"""
{user_sum}
{user_difference}
{user_product}
{user_quotient}
""")



# ============================================================
# SECTION 11 — HARDER MULTI-STEP CALCULATIONS
# ============================================================

# TASK 40:
# Ask the user how many hours they work in ONE day.
#
# Store the answer in:
#
# work_hours
work_hours = int(input("enter hours you work in a day: "))



# TASK 41:
# Ask the user how much money they earn PER HOUR.
#
# Store the answer in:
#
# hourly_rate
#
# THINK:
# A pay rate could contain cents.

hourly_rate = float(input("enter how much you make per hour: "))



# TASK 42:
# Create:
#
# one_day_pay
#
# Calculate how much the person earns in one day.
one_day_pay = hourly_rate * work_hours



# TASK 43:
# Create:
#
# five_day_pay
#
# Calculate how much the person earns after working
# five days.
#
# REQUIREMENT:
# Use one_day_pay.
#
# Do NOT repeat your previous calculation.
five_day_pay = one_day_pay * 5



# TASK 44:
# Create:
#
# money_after_spending
#
# Ask the user how much money they spent.
#
# Subtract that amount from five_day_pay.
#
# You will need to decide whether another variable
# is necessary before you can perform the calculation.
money_after_spending = five_day_pay - float(input("enter amount of money from working spent: "))



# ============================================================
# SECTION 12 — REVERSE THINKING
# ============================================================

# TASK 45:
# Create:
#
# total_cost = 360
# number_of_items = 12
#
# Create:
#
# cost_per_item
#
# You know the TOTAL and the NUMBER OF ITEMS.
#
# Determine the price of ONE item.
total_cost = 360
number_of_items = 12
cost_per_item = total_cost/number_of_items


# TASK 46:
# Create:
#
# total_distance = 450
# hours = 6
#
# Create:
#
# distance_per_hour
#
# Determine how many miles were traveled during
# each hour.
total_distance = 450
hours = 6
distance_per_hour = total_distance/hours



# TASK 47:
# Create:
#
# total_students = 120
# classrooms = 5
#
# Create:
#
# students_per_classroom
#
# Assume students are divided equally.
total_students = 120
classrooms = 5
students_per_classroom = total_students/classrooms



# ============================================================
# SECTION 13 — MORE ADVANCED VARIABLE REUSE
# ============================================================

# TASK 48:
# Create:
#
# item_price = 18
# number_purchased = 5
#
# Create:
#
# subtotal
#
# Calculate the subtotal.
item_price = 18
number_purchased = 5
subtotal = item_price*number_purchased


# TASK 49:
# Create:
#
# shipping_cost = 12
#
# Then create:
#
# total_with_shipping
#
# REQUIREMENT:
# Use subtotal and shipping_cost.
shipping_cost = 12
total_with_shipping = shipping_cost + subtotal



# TASK 50:
# Create:
#
# amount_paid = 150
#
# Then create:
#
# change_received
#
# Determine how much change should be returned.
#
# REQUIREMENT:
# Use total_with_shipping.
#
# Do NOT redo either of the previous calculations.
amount_paid = 150
change_received = amount_paid - total_with_shipping



# ============================================================
# SECTION 14 — STRING + NUMBER CHALLENGE
# ============================================================

# TASK 51:
# Create:
#
# current_year = 2026
#
# Ask the user what year they were born.
#
# Store their answer inside:
#
# birth_year
#
# Make sure you can perform arithmetic with it.
current_year = 2026
birth_year = int(input("enter birth year: "))



# TASK 52:
# Create:
#
# approximate_age
#
# Calculate the user's approximate age.
approximate_age = current_year - birth_year


# TASK 53:
# Create a variable named:
#
# age_as_string
#
# Convert approximate_age into a String.
#
# Do NOT manually type their age as text.
age_as_string = str(approximate_age)



# TASK 54:
# Create:
#
# age_message
#
# Using STRING CONCATENATION, make age_message contain:
#
# You are approximately [age] years old.
#
# REQUIREMENTS:
#
# - Use approximate_age somewhere in the process.
# - Use string concatenation.
# - Do NOT manually type the calculated age.
#
# Think carefully about the data types involved.
age_message = "you are approximately " + str(approximate_age) + " years old."



# ============================================================
# SECTION 15 — FINAL CHALLENGES
# ============================================================

# TASK 55:
# Ask the user for THREE whole numbers.
#
# Store them in:
#
# number1
# number2
# number3
#
# Create:
#
# combined_total
#
# Add all three numbers together.
numberedstring = input("enter 3 numbers separated by spaces: ")
numbers = numberedstring.split()
number1 = int(numbers[0])
number2 = int(numbers[1])
number3 = int(numbers[2])
print(f"{number1} {number2} {number3}")
combined_total = number1+number2+number3



# TASK 56:
# Create:
#
# average
#
# Calculate the average of the THREE numbers.
#
# REQUIREMENT:
# Use combined_total in your calculation.
#
# Do NOT add number1, number2, and number3 together again.
average = combined_total/3




# TASK 57:
# Create:
#
# doubled_average
#
# Make its value TWO TIMES the average.
#
# REQUIREMENT:
# Use average.
doubled_average = average*2



# TASK 58:
# Create:
#
# final_answer
#
# Subtract number1 from doubled_average.
#
# You may ONLY use:
#
# doubled_average
# number1
#
# in this calculation.
final_answer = doubled_average - number1



# ============================================================
# SECTION 16 — FIND THE PROBLEM
# ============================================================

# TASK 59:
# The programmer wanted score to store the NUMBER 95.
#
# Fix the line below so score stores the correct DATA TYPE.

score = 95



# TASK 60:
# The programmer wants to add 10 to the user's number.
#
# The code below will cause a problem.
#
# FIX IT.
#
# Do not replace the user's input with a number.

# user_number = int(input("Enter a number: "))
# answer = user_number + 10
# print(answer)



# TASK 61:
# The programmer wants the output:
#
# 15
#
# Fix the code WITHOUT changing the values 10 and 5.

# first = "10"
# second = 5
# total = int(first) + second
# print(total)



# TASK 62:
# The programmer wants to print the VALUE stored in student.
#
# Fix the print statement.

student = "Alex"

# print(student)



# ============================================================
# FINAL BOSS — CHECK FOR UNDERSTANDING
# ============================================================

# TASK 63:
#
# Ask the user for:
#
# - Their first name
# - Their last name
# - Their birth year
# - Their favorite number
#
# You decide what variables to create.
#
# Then your program must:
#
# 1. Combine their first and last name into ONE variable.
# 2. Calculate their approximate age using 2026.
# 3. Multiply their favorite number by their approximate age.
# 4. Store EVERY calculated result inside a variable.
# 5. Print a personalized message containing their full name.
# 6. Print their approximate age.
# 7. Print the result of their favorite number multiplied by their age.
#
# IMPORTANT:
#
# You are NOT being given the variable names for this problem.
# Choose clear and descriptive variable names yourself.
#
# Your program must work for ANY user.
#
# You may ONLY use concepts from slides 1–60.
# rip

fn_us = input("enter first name: ")
ln_us = input("enter last name: ")
by = int(input("enter birth year: "))
fv_n = float(input("enter favorite number: "))
fln = fn_us + " " + ln_us
apxa = 2026 - by
mfnapxar = fv_n * apxa
print("heh full name " + fln)
print(apxa)
print(mfnapxar)

# did i doed it?
# bruh



# ============================================================
# GIT CHECK
# ============================================================

# When you are completely finished:
#
# 
# 1. Save your file.
# 2. Run your ENTIRE program.
# 3. Fix all errors.
# 4. Make sure you can explain your code.
#
#
# Then use:
#
# git status
# git add .
# git commit -m "Complete Python skills check"
# git push