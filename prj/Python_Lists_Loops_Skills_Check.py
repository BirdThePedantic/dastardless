# Name: Sanjay Tirumalai
# Period: 4?

# im lazy
def n():
    print("\n")
def deny():
    print("naur")
    
fastford=True


# ============================================================
# Python Skills Check — LISTS & LOOPS
# CHALLENGE VERSION — 40 TASKS
# ============================================================
# DIRECTIONS:
# - Create a repository, clone it, and add this file.
# - Complete each task UNDER its directions.
# - Do not delete the directions.
# - Use ONLY concepts learned in class, except for 'in' and 'not in'.
#   You must research these two new operators independently in Section 5.
# - Use the EXACT variable and function names provided.
# - The entire file must run without errors.
# - Do not hard-code results Python should calculate.
# - Unless a task says otherwise, do NOT use sum(), min(), max(),
#   sorted(), sort(), list comprehensions, sets, or dictionaries.
# - For functions, RETURN values when instructed; do not just print.
# - Test edge cases and change the starting values to check your logic.
# - Tasks that ask for input() may be tested individually.

# ============================================================
# SECTION 1 — LIST FUNDAMENTALS (TASKS 1–6)
# ============================================================

# TASK 1:
# Create a list named scores containing 85, 92, 78, 96, 88.
# Print the entire list and its length using len().
score = [85,92,78,96,88]
print(score,len(score))


# TASK 2:
# Using scores from Task 1, print the FIRST, THIRD, and LAST
# elements on separate lines. Use indexes, not hard-coded values.
print(score[0])
print(score[2])
print(score[len(score)-1])


# TASK 3:
# Change the third element of scores to 100.
# Print the updated list. Do not create a replacement list.
score[2]=100
print(score)


# TASK 4:
# Create games = ["Minecraft", "Roblox", "Fortnite"].
# Append "Valorant" and insert "Rocket League" at index 1.
# Print games. Check the order carefully.
games = ["Minecraft", "Roblox", "Fortnite"]
games.append("Valorant")
games.insert(1,"Rocket League")

print(games)


# TASK 5:
# Using games from Task 4, remove "Roblox" with remove().
# Then pop the FIRST item into a variable named removed_game.
# Print removed_game and the remaining games list.
games.remove("Roblox")
removed_game = games.pop(0)
print(removed_game,games)


# TASK 6:
# Create colors = ["red", "blue", "green", "yellow", "purple"].
# Store the index of "green" in green_index using index().
# Print green_index. Then replace "yellow" with "orange".
# Print the new list.
colors = ["red", "blue", "green", "yellow", "purple"]
green_index=colors.index("green")
print(green_index)
colors[colors.index("yellow")]="orange"
print(colors)


# ============================================================
# SECTION 2 — FOR LOOPS & RANGE (TASKS 7–12)
# ============================================================

# TASK 7:
# Use a for loop with range() to print numbers 1 through 20,
# INCLUDING 20. Do not manually print the numbers.
for i in range(21):
    print(i)


# TASK 8:
# Use a for loop with range() to print 30, 27, 24, ... 0.
# IMPORTANT: The zero must be included.
n()
for i in range(30,-3,-3):
    print(i)

n()
# TASK 9:
# Use a for loop to print all EVEN numbers from 1 to 50.
# You MUST use an if statement and the % operator inside the loop.
for w in range(1,51):
    if w%2==0:
        print(w)
    


# TASK 10:
# Create number = 7.
# Print its multiplication table from 1 through 12 using a for loop.
# Example line: 7 x 3 = 21
# Your code must also work if number changes.
number = 7
n()
for i in range(1,13):
    print(number,"*",i,"=",i*number)


# TASK 11:
# Create students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"].
# Use a for loop to print "Student: " followed by each name.
# Do NOT write five separate print statements.
students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
# these people sound like tools
n()
for i in students:
    print("Student:",i)


# TASK 12:
# Using students, print a NUMBERED roster:
# 1. Alex
# 2. Jordan
# ...
# 5. Casey
# Use range(len(students)) OR enumerate().
n()
for i, s in enumerate(students,1):
    print(i,"\b.",s)



# ============================================================
# SECTION 3 — WHILE LOOPS & VALIDATION (TASKS 13–18)
# ============================================================

# TASK 13:
# Create countdown = 10.
# Use a while loop to print from countdown down to 0.
# Then print "Blast off!". Avoid an infinite loop.
countdown = 10
n()
while countdown > 0:
    print(countdown)
    countdown -=1
print("Blast off!")
print("wait no hold on")
print(0)
print("Blast off!")



# TASK 14:
# Create password = "Python123".
# Keep asking the user for a password until it matches.
# Print "Access granted" exactly once after a correct entry.
password = "Python123"
q = ""
n()
if not fastford:
    while q != password:
        q = input("enter password: ")
    print("Access Granted")

# TASK 15:
# Ask the user for an integer between 1 and 10 INCLUSIVE.
# Keep asking while the value is invalid.
# After a valid entry, print "Valid number".
# Test 0, 1, 10, and 11.
m=100
if not fastford:
    while m < 1 or m > 10:
        m=int(input("enter number:"))
    print("Valid number")


# TASK 16:
# Create total = 0.
# Repeatedly ask for an integer. Add each nonzero entry to total.
# Stop when the user enters 0, then print total.
# Example inputs: 5, 8, -2, 0 -> Total: 11.
total = 0
q = 1
if not fastford:
    while q!=0:
        q=int(input("enter nonzero number: "))
        total += q
    print(total)


# TASK 17:
# Create secret = "robot" and attempts = 3.
# Ask the user to guess secret, allowing AT MOST 3 guesses.
# Print "Correct" if guessed in time; otherwise "Out of attempts".
# Make sure a correct guess does NOT print both messages.
secret = "robot"
attempts = 3
z=""
if not fastford:
    while z != secret and attempts > 0:
        
        z = input("enter secret: ")
        attempts -=1
    if z==secret:
        print("Correct")
    else:
        print("Out of attempts")


# TASK 18:
# Make a while-loop menu:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit
# Repeat until the user enters 3. Handle invalid choices.
# Print "Goodbye" only when option 2 is selected.
# ok so option 1 does nothing
if not fastford:
    while True:
        c =input("1. Say Hello\n2. Say Goodbye\n3. Exit\n")
        if c=="3":
            break
        elif c=="2":
            print("Goodbye")
        elif c=="1":
            pass # welp
        else:
            print("naur")
        
    


# ============================================================
# SECTION 4 — PROCESSING LISTS WITH LOOPS (TASKS 19–24)
# ============================================================

# TASK 19:
# Create numbers = [4, 8, 15, 16, 23, 42].
# Use a for loop to calculate and print their total.
# Do NOT use sum().
numbers = [4, 8, 15, 16, 23, 42]
f=0
for i in numbers:
    f+=i
n()
print(f)


# TASK 20:
# Create grades = [90, 85, 78, 92, 88].
# Use a loop and len() to calculate the average.
# Print the average. Do NOT use sum().
grades = [90, 85, 78, 92, 88]
z=0
for r in grades:
    z+=r
print(z/len(grades))



# TASK 21:
# Create numbers = [3, 8, 12, 7, 15, 20, 24, 9].
# Use ONE loop to count even and odd values separately.
# Print "Even: [count]" and "Odd: [count]".
numbers = [3, 8, 12, 7, 15, 20, 24, 9]
d=[0,0]
for i in numbers:
    if i%2==0:
        d[0]+=1
    else:
        d[1]+=1
print("Even:",d[0],"and Odd:",d[1])


# TASK 22:
# Create numbers = [-14, -67, -23, -89, -45].
# Use a loop to find and print the HIGHEST number.
# Do NOT use max() or sorting.
# IMPORTANT: Starting your answer at 0 gives a wrong result.
numbers = [-14, -67, -23, -89, -45]
h=-2**1024
for i in numbers:
    if i > h:
        h=i
print(h)



# TASK 23:
# Create numbers = [14, 67, 23, 89, 45, 12].
# Use a loop to find and print the LOWEST number.
# Do NOT use min() or sorting.
# Your logic must also work with all-negative numbers.
numbers = [14, 67, 23, 89, 45, 12]
lo=2**1024
for i in numbers:
    if i < lo:
        lo=i
print(lo)


# TASK 24:
# Create numbers = [5, 2, 5, 8, 5, 3, 2, 5].
# Create target = 5.
# Use a loop to count how often target appears; print the count.
# Do NOT use count(). It must work if target changes.
numbers = [5, 2, 5, 8, 5, 3, 2, 5]
target = 5
c=0
for i in numbers:
    if i==target:
        c+=1
print(c)


# ============================================================
# SECTION 5 — IN / NOT IN (TASKS 25–30)
# ============================================================
# INDEPENDENT RESEARCH REQUIRED:
# We have NOT covered 'in' and 'not in' in class. Before starting
# Tasks 25–30, research both operators on your own using reliable
# Python learning resources or the official Python documentation.
# Learn what each operator does, how it works with lists, and how
# to use it inside if statements and while loops.
# Write a short comment in your code explaining the difference
# between 'in' and 'not in' in your own words.
# The examples below are starting hints, NOT a substitute for research.
#
# NEW CONCEPT:
# 'in' checks whether a value is in a list.
# Example: "apple" in ["apple", "banana"] evaluates to True.
# 'not in' checks whether a value is missing.
# Example: "grape" not in ["apple", "banana"] evaluates to True.
# These expressions are useful in if statements and while loops.


# huh?
# "in" checks if there's a thing in a list and "not in" returns the opposite of "in" because "not in" is not its own keywordphrase but it has like a logical flipper thingy rsm

# TASK 25:
# Create foods = ["pizza", "burger", "tacos", "sushi", "pasta"].
# Ask the user to enter a food.
# Use 'in' to print "Available" or "Not available".
# Do NOT use index() to search.
n()
foods = ["pizza", "burger", "tacos", "sushi", "pasta"]
if not fastford:
    q=input("enter food: ")
    if q in foods:
        print("Available")
    else:
        print("Not available")
n()


# TASK 26:
# Create supplies = ["pencil", "notebook", "eraser", "backpack"].
# Ask the user for an item.
# Use 'not in' to print "Need to buy" if it is missing,
# otherwise print "Already have it".
supplies = ["pencil", "notebook", "eraser", "backpack"]
if not fastford:
    q=input("enter item?: ")
    if q not in supplies:
        print("Need to buy")
    else:
        print("Already have it")


# TASK 27:
# Create usernames = ["alex123", "gamer99", "pythonpro"].
# Ask the user to enter a new username.
# If it is already in the list, print "Username taken".
# Otherwise append it and print the updated list.
# Do not allow duplicates.
n()
usernames = ["alex123", "gamer99", "pythonpro"]
a = "alex123"
if not fastford:
    while a in usernames:
        a=input("enter username: ")
        if a in usernames:
            print("Username taken")
    usernames.append(a)
    print(usernames)


# TASK 28:
# Modify the idea from Task 27 using a NEW list named accounts. 
# yeah uh idk
# Start with accounts = ["admin", "guest"].
# Use a while loop to keep asking until the entered name
# is NOT in accounts. Append the accepted name and print accounts.
# REQUIREMENT: Use 'not in' in your solution.

# huh?
accounts =["admin","guest"]

# change this for meaning that i thought before? eh well whatever
eitherididathingorididntdoathing = False

if eitherididathingorididntdoathing:
    for m in usernames:
        accounts.append(m)
z=accounts[0]
n()
if not fastford:
    while z in accounts:
        z=input("enter account name?: ")
    accounts.append(z)
    print(accounts)

# TASK 29:
# Create secret_words = ["dragon", "robot", "python", "galaxy"].
# Keep asking the user for a word UNTIL it is in secret_words.
# Count and print the number of guesses made.
# A correct first guess should count as 1.
g=0
secret_words = ["dragon", "robot", "python", "galaxy"]
z=""
n()
if not fastford:
    while z not in secret_words:
        z=input("enter word: ")
        g+=1
    print(g)



# TASK 30:
# Create guests = [].
# Ask the user to enter EXACTLY FIVE UNIQUE guest names.
# If a name is already in guests, reject it and ask again.
# Use a while loop, 'in' or 'not in', and append().
# Print the finished list and its length.
guests=[]
n()
if not fastford:
    while len(guests)<5:
        z=input("enter guest name: ")
        if z in guests:
            print("naur")
        else:
            guests.append(z)
    print(guests,len(guests))


# ============================================================
# SECTION 6 — LISTS + FUNCTIONS (TASKS 31–35)
# ============================================================

# TASK 31:
# Create a function named count_positive(numbers).
# RETURN how many elements are greater than 0.
# Do NOT use count().
# Test: count_positive([-2, 0, 4, 9, -1]) -> 2
testor=[-2,0,4,9,-1]
def count_positive(t):
    c=0
    for r in t:
        if r>0:
            c+=1
    return c
n()

# TASK 32:
# Create a function named find_item(items, target).
# RETURN the index of the FIRST matching item, or -1 if missing.
# Do NOT use index().
# Test: find_item(["cat", "dog", "cat"], "cat") -> 0
# Test: find_item(["cat", "dog"], "fish") -> -1

def find_item(items, target):
    for i in range(len(items)):
        if items[i]==target:
            return i
    return -1


# TASK 33:
# Create a function named unique_items(items).
# RETURN a NEW list without duplicate values, preserving first
# appearance order. REQUIREMENT: Use 'not in'.
# Test: unique_items([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
def unique_items(items):
    z=[]
    for i in items:
        if i not in z:
            z.append(i)
    # print(z)
    return z
unique_items([1,2,2,3,1,4])


# TASK 34:
# Create a function named common_items(list1, list2).
# RETURN a NEW list of values found in BOTH lists.
# Include each matching value only once, in list1's order.
# REQUIREMENT: Use both 'in' and 'not in'.
# Test: common_items([1, 2, 3, 3], [3, 4, 1]) -> [1, 3]
def common_items(list1,list2):
    z=[]
    for i in list1:
        if i in list2 and i not in z:
            z.append(i)
            # hm
    # print(z)
    return z
common_items([1, 2, 3, 3], [3, 4, 1])


# TASK 35:
# Create a function named reverse_list(items).
# RETURN a NEW list in reverse order, without changing items.
# Do NOT use reverse(), reversed(), or [::-1].
def reverse_list(items):
    z=[]
    for i in items:
        z.insert(0,i)
    # print(z)
    return z
reverse_list([10, 20, 30])



# ============================================================
# SECTION 7 — DEBUGGING (TASKS 36–37)
# ============================================================

# TASK 36:
# Fix this code so it prints 1, 2, 3, 4, 5 exactly once each.
# Explain in a comment what was wrong.
#
# number = 1
# while number <= 5:
#     print(number)
#
# Do NOT replace the while loop with a for loop.

# number doesn't increment -> infinite loop
number = 1
while number <=5:
    print(number)
    number+=1


# TASK 37:
# Fix this code so it removes ALL 4s without skipping any.
# Explain in a comment why the original approach can fail.
#
# values = [4, 4, 7, 4, 9]
# for value in values:
#     if value == 4:
#         values.remove(value)
# print(values)
#
# Expected: [7, 9]
# HINT: A while loop and 'in' can help.

# removing shifts indexes and some indexes are lost
values = [4,4,7,4,9]
while 4 in values:
    values.remove(4)
print(values)


# ============================================================
# FINAL BOSS CHALLENGES (TASKS 38–40)
# ============================================================
# heh lol oh wait goddamn it

# TASK 38 — SHOPPING LIST MANAGER:
# Build a menu-driven program with:
# 1. Add item
# 2. Remove item
# 3. View numbered items
# 4. Search for item
# 5. Exit
# Start with shopping_list = [].
# REQUIREMENTS:
# - Use a while loop for the menu and a for loop to display items.
# - Use 'in' to prevent duplicates and 'not in' to reject missing items.
# - Handle an empty list and invalid menu selections.
# - Keep running until the user chooses Exit.
n()

done = False
shopping_list = []
iterms = ["dingleberries","horse pills","dehydrated water","self-esteem","cheese"]
def barf(o):
    n()
    if o == 0:
        
        print("== wares ==")
        for i in range(len(iterms)):
            z =iterms[i]
            print(str(i)+". "+z)
        
        
    if o==2:
        
        for i in range(len(shopping_list)):
            print(str(i)+". "+shopping_list[i])
        
    n()
if not fastford:
    while not done:
        n()
        print("=== inconvenience store ===")
        print("1. Add item\n2. Remove item\n3. View numbered items\n4. Search for item\n5. Exit")
        # well you haven't taught us about try except so i guess that'll go unchecked?
        w = int(input("> "))
        if w < 1 or w > 5:
            print("naur")
            n()
        if w==1:
            if len(shopping_list) == len(iterms):
                print("cart's full, cap'n")
            else:
                barf(0)
                m = int(input("add item to cart: "))
                if m < 0 or m >= len(iterms):
                    deny()
                else:
                    if iterms[m] in shopping_list:
                        print("already in there, cap'n")
                    else:
                        shopping_list.append(iterms[m])
        if w==2:
            if len(shopping_list) <= 0:
                print("cart empty, cap'n")
                
            else:
                barf(2)
                dfruhz = int(input("remove item from cart: "))
                if dfruhz < 0 or dfruhz >= len(shopping_list):
                    deny()
                else:
                    shopping_list.remove(shopping_list[dfruhz])
        if w==3:
            barf(0)
        if w==4:
            zruh = input("lookup item: ")
            if zruh not in iterms:
                print("ain't carried here")
            else:
                print("in stock")
        if w == 5:
            if len(shopping_list) > 0:
                print("shoplift much?")
            else:
                print("cya")
            break



# TASK 39 — GRADE ANALYZER:
# Create a function named analyze_grades(grades).
# RETURN a list containing, IN THIS ORDER:
# [highest_grade, lowest_grade, average_grade, passing_count, failing_count]
# Passing means 70 or higher.
# Do NOT use sum(), min(), max(), or sorting.
# For an empty list, RETURN [].
# Test: analyze_grades([95, 82, 67, 74, 58])
# Expected: [95, 58, 75.2, 3, 2]
# Test with a single grade and all-negative values too.

# placeholder variables, you say? probably not said, but i'm lazy so whatever

thething = [95, 82, 67, 74, 58]

def analyze_grades(grades):
    if len(grades)==0:
        return []
    highest_grade=-2**1024
    lowest_grade=2**1024
    average_grade=0
    passing_count=0
    failing_count=0

    zz = 0
    for z in grades:
        zz+=z
        if z < lowest_grade:
            lowest_grade=z
        elif z > highest_grade:
            highest_grade=z
        if z >=70:
            passing_count+=1
        else:
            failing_count+=1
    average_grade=zz/len(grades)
    return [highest_grade, lowest_grade, average_grade, passing_count, failing_count]

# print(analyze_grades(thething))




# TASK 40 — STUDENT ATTENDANCE SYSTEM:
# Start with:
# students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
# present = []
# absent = []
# For EACH student, ask whether they are Present (P) or Absent (A).
# REQUIREMENTS:
# - Use a for loop to process the student list.
# - Use a while loop to reject anything other than P or A.
# - Prevent duplicate attendance records using 'in' / 'not in'.
# - Print numbered present and absent lists.
# - Print the number present, number absent, and attendance percentage.
# - Print "Perfect Attendance!" if everyone is present.
# - Create attendance_percentage(present, students) that RETURNS
#   the percentage; if students is empty, RETURN 0.
# - Test with all present, all absent, and a mixture.

students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
dernumbers = [1,2,3,4,5]
present = []
absent = []

def attendance_percentage(present,students):
    if len(students) == 0:
        return 0
    return (len(present)/len(students))*100


for s in students:
    p = ""
    while p != "A" and p != "P":
        p = input(s+" there? (P/A): ")
    if p == "A":
        if s in students:
            absent.append(s)
            # dude idk what you want me to do with in and not in bruh
    else:
        if not s not in students:
            present.append(s)
print(present,absent)
print(len(present),len(absent),attendance_percentage(present,students))
if len(present) == len(students):
    print("Perfect Attendance!")



# ============================================================
# END OF CHECKPOINT — REVIEW YOUR WORK BEFORE PUSHING
# ============================================================
