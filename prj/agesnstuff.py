import time
import sys
# here's subtraction
y = 5 - 2
print("yo, user")
print("this program will ask you some questions including your birth year")
print("then \"i\"'ll tell you how long you've been alive \nbased on your birth year (inaccurate)")

ac = False
while not ac:
    try:
        # birth year
        by = int(input("birth year:\n"))
        if by < 1900:
            print("i refuse to believe that you're still alive")
            continue
        if by > 2026:
            print("you're not from the future, shut up")
            continue
        elif by > 2022:
            print("you don't know how to use a goddamn computer yet")
            continue
        ac = True
    except ValueError:
        print("arabic numerals only bruh")
        ac = False

just_to_be_safe_imma_use_another_variable = False
while not just_to_be_safe_imma_use_another_variable:
    # name
    name = input("\nenter name:\n")
    if len(name) < 2:
        print("your name is not frickin one letter long bruh i refuse to believe it")
        continue
    # fav food
    fvfd = input("favorite food:\n")
    if len(fvfd) < 3:
        print("i don't care what language you're answering this \nquestion in but in english the least amount of letters \nin a food is 3 bubba")
        continue
    # fav hobby
    # yeah so uh i ain't going to go back in and rename
    # all the variables
    # yes i know how to multi line comment
    """
    oh look a wild fvhb
    """
    fvhb = input("favorite hobby:\n")
    
    if len(fvhb) < 2:
        print("dude just answer the damn questions with \nsomething longer than 2 characters")
        continue
    # city of residence rsm
    adrs = input("city you live in:\n")
    if len(adrs) <= 3:
        print("no abbreviations, please; i'm trying to piss you off")
        continue

    #fav movie
    # man i hate python
    favorite_movie = input("enter favorite movie:\n")
    if len(favorite_movie) < 1:
        print("no movies are zero characters long dumbass try again")
        continue
    try:
        sibling_number = int(input("number of siblings:\n"))
        if sibling_number < 0:
            print("answer the damn question correctly")
            continue
    except ValueError:
        print("ARABIC FRICKING NUMERALS ONLY!!!")
    just_to_be_safe_imma_use_another_variable = True
print("how am i supposed to know your birth month from your birth year? anyway")
# does stuff
def dpi(n, b, f, h, a, m, s):
    age_months = b*12
    age_days = b*365.2422
    age_hours = b*365.2422*24
    age_minutes = b*365.2422*24*60
    age_seconds = age_minutes*60
    print(f"""
    \nyour name is {n}. hi {n} i guess
    \nyour birth year is {b}, making you \n
    {2026 - b} years old or
    \n{2026*12 - b*12} months old or
    \n{2026*365.2422 - b*365.2422} days old or
    \n{2026*365.2422*24 - b*365.2422*24} hours old or
    \n{2026*365.2422*24*60 - b*365.2422*24*60} minutes old or
    \n{2026*365.2422*86400 - b*86400*365.2422} seconds old 
    as of 2026
    \nyour favorite food is {f}
    \nyour favorite hobby is {h}
    \nyour location of living is {a}
    \nyour favorite movie is {m}
    \nyou have {s} siblings
    \nbut that's just what you told the program and doesn't \nnecessarily reflect the truth
    """)

    # yeah so i forgot to give them separate variables
    # but whatever

dpi(name, by, fvfd, fvhb, adrs, favorite_movie, sibling_number)

complid = False
while not complid:
    try:
        future_year = int(input("enter year over 2026:\n"))
        if future_year < 2027:
            print("i said a FUTURE YEAR")
            continue
        complid = True
    except ValueError:
        print("bruh")
print(f"you will be {future_year - by} in {future_year}\n")

print("time for this program to end")
print("go do something productive now")

# how many criterions did i fulfill?
# also just do 365.2422 instead of jumping through hoops for leap years