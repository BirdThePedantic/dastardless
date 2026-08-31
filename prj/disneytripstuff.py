import sys
"""
needed:
ppl going, days, ticket price,
food-souvenir-trip budget, hotel cost,
distance, mpg vehicle, gas price
parking cost
"""

def p(inp):
    print(inp)
def i(inp):
    w = input(inp)
    return w

true = True
false = False

p("yo")
p("driving to frickin disneyland, huh?")
p("let me probably help you with that. \"I\"'ll calculate the finances, just answer these questions.")

name_user = i("your name: ")

try:

    ppl_going: int = int(i("number of people going: "))

    park_days: int = int(i("days you plan to stay: "))

    # overwritten, ignore this
    if park_days == 2:
        ph_ticket_price = 435
    elif park_days == 3:
        ph_ticket_price = 535
    elif park_days == 4:
        ph_ticket_price = 600
    elif park_days == 5:
        ph_ticket_price = 655
    else:
        ph_ticket_price = 9999999
        # haha screw you
    # ok you can stop ignoring now
    
    ph_ticket_price = float(input(f"cost of 1 {park_days}-day park hopper ticket: "))

    budget_food: float = float(i("food budget: "))

    cost_food = float(i("cost of food: "))

    budget_svnr: float = float(i("souvenir budget (what a loser): "))

    cost_svnr = float(i("cost of souvenirs: "))

    svnr_count = int(i("souvenirs per person: "))

    cost_hotel: float = float(i("hotel cost per night per person: "))

    rooms_hotel = int(i("hotel rooms needed: "))

    distance_miles: float = float(i("distance to disneyland in miles: "))

    mpg_vehicle = float(i("miles per gallon of vehicle: "))

    gas_price_current_actual_regular = 4.0807

    gas_price_current = float(i("current gas prices: "))

    cost_parking = float(i("cost of parking at disney: "))

    budget_total = float(i("total budget: "))

    if (budget_total < budget_svnr or budget_total < budget_food or budget_food + budget_svnr > budget_total):
        p("the math is not mathing")
        p("try again with good mathing")
        sys.exit("bad math skills and stuff")

except ValueError:
    p("bruh")

cost_ph_tickets_all = ppl_going * ph_ticket_price
# assuming each person eats 3 times a day
cost_food_all = ppl_going * 3 * park_days * cost_food

# assuming everyone wants one souvenir
cost_svnr_all = cost_svnr * ppl_going * svnr_count

cost_hotel_all = cost_hotel * park_days * ppl_going * rooms_hotel

drive_distance_round_trip = distance_miles * 2

gallons_gas_needed_one_trip = distance_miles / mpg_vehicle

gallons_needed_round_trip = gallons_gas_needed_one_trip * 2

cost_gas_round_trip = gallons_needed_round_trip * gas_price_current

# everyone's going in one car, right? nobody needs to get into a car to go to a hotel, right? eh whatever

cost_parking_all = cost_parking * park_days

total_cost_disney = cost_parking_all + cost_gas_round_trip + cost_hotel_all + cost_svnr_all + cost_food_all + cost_ph_tickets_all

total_cost_person = total_cost_disney / ppl_going

total_cost_day = total_cost_disney / park_days

budget_difference = budget_total - total_cost_disney

print(f"""
{name_user}'s trip to disney overview:
{ppl_going} people going
{park_days} days to be spent
${ph_ticket_price} for a {park_days}-day ticket
${cost_ph_tickets_all} for everyone's tickets
${cost_food_all} for food for everyone
${cost_svnr_all} for souvenirs for everyone
${cost_hotel_all} for hotel expenses
{distance_miles} miles for a one way trip
{drive_distance_round_trip} miles for a round trip
{mpg_vehicle} miles per gallon on your vehicle
${gas_price_current} per gallon of gas
{gallons_needed_round_trip} gallons of gas needed for a round trip
${cost_gas_round_trip} for gas for a round trip
${cost_parking_all} cost of parking for all days

${total_cost_disney} in total for trip
${total_cost_day} per park day
${total_cost_person} per person

${budget_total} trip budget
${budget_difference} budget difference

""")
if (budget_difference > 0):
    print("you can afford this trip")
    print("have fun, if you're planning to go")
else:
    print("better get your broke ass to great america")
    print("maybe rob a bank or something, why dont you")





