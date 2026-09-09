# welcome?
print("yo")
print("\"welcome\" to random theme park")
print("you're going to be put through discrimination tests for admission or whatever.")

# shorthands
true = True
false = False
# dox user
guest_name = input("enter name: ")
guest_age = int(input("enter age: "))
guest_height_inches = int(input("enter height in inches: "))
ticketTypeAsk = input("did you purchase a regular or premium ticket (r/p): ")
ticketType = -1
# resolve ticket type (rip i used camel case)
if (ticketTypeAsk == "r"):
    ticketType = 0
else:
    ticketType = 1

# resolve park membership
park_member_ask = input("are you a park member (y/n): ")
guest_member = False
if park_member_ask == "y":
    guest_member = true

# supervised?
with_adult_ask = input("are you visiting with an adult (y/n): ")
with_adult = false
# if input is anything other than 'Y' or 'y' default to false (why did I put n then?)
if (with_adult_ask.lower() == "y"):
    with_adult = true
visit_time_ask = input("are you visiting in the morning or evening (m/e): ")
visit_time = 1
if visit_time_ask.lower() == "m":
    visit_time = 0
    # defaults to evening if you didn't answer correctly
    # also there are a lot of inconsistencies and stuff

# get the uh price off your age
def calculate_admission(age):
    price = 0
    if age >= 65:
        price = 20
    elif age >= 13:
        price = 30
    elif age >= 5:
        price = 15
    return price
# when i first started python i never understood 'return' because it didn't tell me what
# i should be returning; why should i do that when i could just use a mutator function?
# java cleared it up though, now i know the use for return functions
# rip
admission_price_bfr = calculate_admission(guest_age)

# get the discount if you're special? subtracts from price
def calculate_discount(price, member, visitn_time):
    discount = 0
    if member:
        discount += 5
    if visitn_time == 1:
        discount += 3
    if member and visitn_time:
        discount += 2
    finalp = price - discount
    if finalp < 0:
        finalp = 0
    return finalp
# the first admission_price initialization might be redundant idk
# man i hate python
admission_price = calculate_discount(admission_price_bfr, guest_member, visit_time)

# caculate (???) ride level. i hate python so much
# python would be orders of magnitude better if it had enums
# lemme import enums bruh
# teach the damn enums so i can use them
# highest ride ye quality for (???)
def ride_level(ag, hit):
    level = -1
    slv = "no ridin'"
    if hit >= 54 and ag >= 16:
        level = 4
    elif hit >= 48 and ag >= 12:
        level = 3
    elif hit >= 42 and ag >= 8:
        level = 2
    elif hit >= 32:
        level = 1
    if level == 1:
        slv = 'tiny tot rides'
    elif level == 2:
        slv = "rides f' t' fam"
    elif level == 3:
        slv = "hair on ye chest rides"
    elif level == 4:
        slv = "'damn!' rides"
    return slv
guest_ride_lv = ride_level(guest_age, guest_height_inches)

# no entry if you're... underage the age of entry?
def check_supervision(a, vwa):
    getinstatus = "'prov'd"
    if a < 13 and not vwa:
        getinstatus = "not 'prov'd"
    return getinstatus
supervision_level = check_supervision(guest_age, with_adult)

# yeah apparently ticket type as an integer is not the way to go
ticket_t = "regular"
t_stat = "you have a ticket, cool"
if ticketType == 1:
    ticket_t = "premium"
    t_stat = "your premiumness gets you a 'free' foodstuff and priority ride access"
else:
    t_stat = "you have a ticket, cool"
    # redundant but ok ^^^

# print final report
# man, multi-line print format statements are the way to go, TEACH IT!
# please?
print(f"""
price and stuff and overview and stuff
{guest_name}'s the name
{guest_age} y/o
{guest_height_inches} in tall
{ticket_t} ticket
${admission_price_bfr} ticket cost before discount
${admission_price} ticket cost after discount
{guest_ride_lv} riding level
{supervision_level} to be in the park
{t_stat}
""")
# if statement
# HA! it's actually not that funny
# personalized message, i think (if you're not approved to enter)
if supervision_level == "not 'prov'd":
    print("better get a biggun to accompany you")

# what else am i supposed to comment about?
# im not looking over all those criterions you got me messed up
