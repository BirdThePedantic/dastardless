import datetime

products = {"nothing":99,"dingleberries":5,"dehydrated water":7,"self-esteem":50,"nothing again but this time it costs more":999}

true=True;false=False
shopping_cart={
} # things and count

# uh i forgor

def getfromindex(i): # returns an entry from products, but takes a 1 indexed number parameter
    # at least thats what i think it does
    # does not check if index is valid lol
    return list(products.items())[i-1]
def n():
    print("\n")

# acts differently depending on contorl
def barfinv(contorl):
    if contorl==1:
        print(f"""
========== SMART SHOPPING CART ==========

1. View Available Products
2. Add Product to Cart
3. Remove Product from Cart
4. View Shopping Cart
5. View Current Total
6. Checkout
""")
        return int(input("\nEnter your choice: "))

    # 1 -> displays main menu and returns int input value
    # no try catch yet
    # teach us more stuff man!
    
    # wares
    # displays wares without returning anything
    if contorl==0:
        print("=== wares ===")
        for i,(p,v) in enumerate(products.items()):
            i+=1
            # im using print format man
            # js teach it to us already
            print(f"{i}) {p} ${v:.2f}")
        print("=============\n")

def amsaved(t,r):
    # price multiplier: r?
    # t=100 r=0.85
    return t*r

# return discount based upon the stuff in a dictionary
# heavily implied that the dictionary parameter must be shopping_cart
# shouldve accepted a float/integer parameter but whatever
# should not be used with any dictionary other than shopping_cart :skull:
def gitthedisc(s):
    m=0
    discoteca=0 # default 0
    for k,v in s.items():
        m+=products[k]*v
    if m >= 40:
        discoteca=.15
    elif m > 20:
        discoteca=.1
    elif m > 10:
        discoteca=.05 # 5%, etc.
    return discoteca

# dk what this does
solongnerds=0
# ok so this variable does nothing because i did not do anything with it
# im keeping it for no reason

while True:
    m= barfinv(1) # input that determines everything down there
    if m < 1 or m > 6: # catches invalid numbers
        print("naur")
        continue

    if m==1 or m==2 or m==3: # groups inputs that all displays products
        # what is done with the products is evaluated?
        mades=false # too lazy to capitalize so i made a variable :skull:
        barfinv(0)
        while not mades and m != 1: # go away if input not required, and repeat until valid input
            w=int(input("enter product number: "))
            if w < 1 or w > 5: # doesn't actually change the value of mades but it still repeats the loop
                # whatever i guess
                print("naur")
                continue
            # print(str(getfromindex(w)))
            f=getfromindex(w)[0] # gets the key from the kv pair?

            # adding products
            if m==2: # should be its own function
                qty = int(input("how many to add: "))
                if qty==0:
                    print("ok then quit wasting my time")
                if qty<0:
                    print("illegal, aborted")
                    continue
                # doesn't continue if qty is 0, adds 0 to the count instead
                # continues if negative
                if f in shopping_cart:
                    shopping_cart[f]+=qty
                else:
                    shopping_cart[f]=qty # quantity stays the same
                    # apparently it got to the point where... nvm
            elif m==3:
                
                if f not in shopping_cart:
                    print("nothing there already")
                    # yeah?
                else:
                    
                    shopping_cart[f]-=1
                    if shopping_cart[f]<=0:
                        begone=shopping_cart.pop(f)
                        # that value is goneeeeee
            mades=True
    if m==4:
        # view stuff

        if len(shopping_cart)<1:
            print("nothing in cart, cap'n")
            continue
        print("=== cart ===")
        for i,(k,v) in enumerate(shopping_cart.items()):
            print(f"{i+1}) {k} ${products[k]:.2f} x{v} (${v*products[k]:.2f})")
        print("============")
    if m==5: # moneys, discount as well?
        # similar in gitthedisc bruh
        total=0
        fp=.2
        if len(shopping_cart)<1:
            print("nothing in cart, cap'n ($0)")
            continue
        for k,v in shopping_cart.items():
            total+=products[k]*v
            pass
        if total >= 40:
            fp=.15
        elif total > 20:
            fp=.1
        elif total > 10:
            fp=0
            # l bozo?
        print(f"${total} total, {100*fp}% discount -> (${total-total*fp})")
        # on the fly computation? dont carry over
            
    if m==6:
        # can't leave until you buy sm
        if len(shopping_cart) < 1:
            print("buy something or die")
            continue
        
        else:
            # print format sue me
            print(f"""
===== receipt =====
date: {datetime.date.today()}
""")
            theoldtarttoter=0
            sbt=0;
            the=gitthedisc(shopping_cart)
            # stuff
            for k,v in shopping_cart.items():
                print(f"{k} x{v} ${products[k]} (${products[k]*v})")
                sbt+=products[k]*v
                theoldtarttoter+=v
            print(f"\ntotal stuff: {theoldtarttoter}")
            print(f"subtotal: ${sbt}")
            print(f"discount: {the*100}%")
            print(f"amount saved: ${amsaved(sbt,the)}")
            fin=sbt-sbt*the
            print(f"final total: ${fin}")

            print("thanks for wasting your time here")
            print("===================")
            break

# end of file?
# dude i cannot put comments everywhere
# just turn it in already man
        
