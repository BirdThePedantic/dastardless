import time
import sys

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
    fvhb = input("favorite hobby:\n")
    
    if len(fvhb) < 2:
        print("dude just answer the damn questions with \nsomething longer than 2 characters")
        continue
    # city of residence rsm
    adrs = input("city you live in:\n")
    if len(adrs) <= 3:
        print("no abbreviations, please; i'm trying to piss you off")
        continue
    favorite_movie = input("enter favorite movie:\n")
    if len(favorite_movie) < 1:
        print("no movies are zero characters long dumbass try again")
        continue
    just_to_be_safe_imma_use_another_variable = True
print("how am i supposed to know your birth month from your birth year? anyway")
# does stuff
def dpi(n, b, f, h, a):
    print(f"""
    \nyour name is {n}
    \nyour birth year is {b}, making you \n
    {2026 - b} years old or
    \n{2026*12 - b*12} months old or
    \n{2026*365 - b*365} days old or
    \n{2026*365*24 - b*365*24} hours old or
    \n{2026*365*24*60 - b*365*24*60} minutes old or
    \n{2026*365*86400 - b*86400*365} seconds old 
    as of 2026
    \nyour favorite food is {f}
    \nyour favorite hobby is {h}
    \nyour location of living is {a}
    \nbut that's just what you told the program and doesn't \nnecessarily reflect the truth
    """)

dpi(name, by, fvfd, fvhb, adrs)