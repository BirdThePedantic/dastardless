workshops = ("Game Design", "AI Chatbots", "Robotics")

# todo -> write 3 more fns?

registrations = {
    "maya": "Game Design",
    "jordan": "AI Chatbots",
    "alex": "Robotics",
    "sam": "Game Design",
    "taylor": "AI Chatbots"
}

checked_in = set()
a=True
# extra credit is a naur bc idk what the question asks idk whatever rsm bruh ok now im just typing to type
# bruh
def wlegal(m) -> bool:
    return m.isdigit() and int(m)>0 and int(m)<len(workshops)+1

def wbarf():
    print("=== workshops ===")
    for i in range(len(workshops)):
        w=workshops[i]
        print(f"{i+1}) {w}")
    print("=================")
    return input("workshop number: ").strip()

def neverusedeverbutshouldbe():
    return registrations.keys() & checked_in

def wwbarf():
    print("=== workshops ===")
    for i in range(len(workshops)):
        w=workshops[i]
        print(f"{i+1}) {w}")
    print("=================")

def t():
    return input("enter student name: ").lower().strip()

while a:
    # no idea why there's an f there
    c=input(f"""
========== HACKATHON CHECK-IN ==========

1. View Workshops
2. Look Up a Registration
3. Check In a Student
4. View Attendance Report
5. Remove One Check-In
6. Clear All Check-Ins
7. Register a New Student
8. Change a Student's Workshop
9. View Check-Ins for One Workshop
10. Exit

Enter your choice:

""")
    if not c.isdigit() or (float(c)<1 and float(c)>10):
        print("that didn't work")
        continue
    if c=="10":
        print("see ya idiot")
        a=False;continue
    if c=="1":
        wwbarf()
    if c=='2':
        n=t()
        if n in registrations:
            print(f"\nworkshop: {registrations[n]}")
        else:
            print("\nstudent unfound\n")
    if c=='3':
        n=t()
        if n not in registrations or not n:
            print("student unfound")
        elif n in checked_in:
            print("student already checked in")
        else:
            # student in registrations and not in checked_in, etc
            checked_in.add(n)
            print(f"checked in {n}")
    if c=='4':
        print("========== ATTENDANCE REPORT ==========")
        print(f"register'd students: {len(registrations)}")
        # ch=0
        # deletethis=[]
        # for w in registrations:
        #     if w in checked_in:
        #         ch+=1
        #         continue
        #     deletethis.append(w)
        deletethis=registrations.keys()-checked_in
            
        print(f"checked in: {len(checked_in)}")
        print(f"unchecked in ({len(deletethis)}):\n")
        for m in deletethis:
            print(m)
        # not optimized lol?
        del deletethis
        # haha begone
                
        print("=======================================")
    if c=='5':
        if len(checked_in)<1:
            print("nobody to check out")
            continue
        thebiggestloser=checked_in.pop()
        print(f"removed {thebiggestloser}")
    if c=='6':
        if input("are you sure? (y/n):").lower() == 'y':
            checked_in.clear()
            print("checked everyone out")
        else:
            print("ok quit wasting my time")
    if c=='7':
        n=t()
        if n in registrations:
            print(f"{n} is already registered")
            continue
        if not n:
            print("what")
            continue
        w="2h"
        while not wlegal(w):
            w=wbarf()
        
            if wlegal(w):
                registrations[n]=workshops[int(w)-1]
                print(f"{n} registered for {registrations[n]}")
            else:
                print("unrecognized workshop number\n")
    if c=='8':
        n=t()
        if n not in registrations or not n:
            print("student unfound")
            continue
        w="illegal immigrants or something"
        while not wlegal(w):
            w=wbarf()
            if not wlegal(w):
                print("unrecognized")
                continue
            if workshops[int(w)-1]==registrations[n]:
                print("student already in this workshop")
                continue
            registrations[n]=workshops[int(w)-1]
            print(f"workshop of {n} changed to {registrations[n]}")
    if c=='9':
        w="bruh"
        while not wlegal(w):
            w=wbarf()
            if wlegal(w):
                destroy=set()
                m=workshops[int(w)-1]
                for r in registrations:
                    if registrations[r]==m:
                        destroy.add(r)
                destroy2=sorted(destroy&checked_in)
                if len(destroy2)<1:
                    print("nobody here")
                    continue
                print(f"=== check ins ===") # why is there f
                print(f"{m} goers checked in: {len(destroy2)}")
                for d in destroy2:
                    print(d)
                print("==================")
                

            else:
                print("unrecognized\n")


# uh
"""
1)
maybe
when workshops needed to be added or removed due to funding stuff?

2)
there's a new key with a new value
there's a same key with a new value

3)
4
9
set difference -> for sets a and b, a - b returns a set of the values of a that are not in b?
set intersection -> for sets a and b, a&b returns a set of the values present in both sets?

4)
a random thing from the set
if it's empty it raises a KeyError or something

5)
the check ins are cleared
the registrations are preserved
right?
"""

# hell im done




        
        


        
        
