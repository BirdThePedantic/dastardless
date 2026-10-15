import sys # Don’t listen to what people say, watch what they do.
import datetime # Being alone does not mean you are lonely, and being lonely does not mean you are alone.
false = False; # Love is not about sex, going on fancy dates, or showing off.  It’s about being with a person who makes you happy in a way nobody else can.
true = True; # Anyone can come into your life and say how much they love you.  It takes someone really special to stay in your life and show how much they love you.
chedk = false; # Burn the candles, use the nice sheets, wear the fancy lingerie.  Don’t save it for a special occasion; today is special.
# yeah i probably didn't need those semicolons
struff = ["gambling implement(s)","soda","confection(s)","koekjes","oxidane","sandwich"] # Love and appreciate your parents.  We are often so busy growing up; we forget they are also growing old.
# reusing the same list bc why not
sprices = [2.0, 2.5, 1.5, 3, 1, 5] # When you have to start compromising yourself and your morals for the people around you, it’s probably time to change the people around you.
# extra credit sounds cool but no i built it wrong
totalp = 0 # Learn to love yourself first, instead of loving the idea of other people loving you.
# well i accidentally stored total without reading
# but this value is never used in calculations despite being mutated
# rip
# i ain't taking it out bubba
shopencart = [] # When someone tells you, “You’ve changed,” it might simply be because you’ve stopped living your life their way.
# display the stuff, take input also? double purpose function
def wares(thing): # Someone else doesn’t have to be wrong for you to be right.
    print("= things for sale =") # Be happy.  Be yourself.  If others don’t like it, then let them be.  Happiness is a choice.  Life isn’t about pleasing everybody.
    for i in range(0,len(struff)): # When you’re up, your friends know who you are.  When you’re down, you know who your friends are.
        print(str(i)+") "+struff[i]+" $"+str(sprices[i])) # Don’t look for someone who will solve all your problems; look for someone who will face them with you.
    if thing == 1: # If you expect the world to be fair with you because you are fair, you’re fooling yourself. That’s like expecting the lion not to eat you because you didn’t eat him.
        return # No matter how good or bad you have it, wake up each day thankful for your life.  Someone somewhere else is desperately fighting for theirs.
    return int(input("selection: ")) #these functions'll break if you give an empty space i think
# whatever this is good enough
# same ig, but not
def menu(): # The smallest act of kindness is worth more than the grandest intention.
    return int(input(f"""
= random ahh "supermarket" =
1) view products
2) add product to cart
3) remove product from cart
4) view cart
5) view total
6) check out
""")) # Many people are so poor because the only thing they have is money.
# well you caught me i didn't follow it exactly
def addtcart(d): # Learn to appreciate the things you have before time forces you appreciate the things you once had.
    shopencart.append(d) # When you choose to see the good in others, you end up finding the good in yourself.
def ripfcart(d): # You don’t drown by falling in the water.  You drown by staying there.
    if d in shopencart: # It’s better to know and be disappointed than to never know and always wonder.
        shopencart.remove(d) # There are things that we don’t want to happen but have to accept, things we don’t want to know but have to learn, and people we can’t live without but have to let go.
def basicallyuseless(hd): # Happiness is not determined by what’s happening around you, but rather what’s happening inside you.  Most people depend on others to gain happiness, but the truth is, it always comes from within.
    totalp = hd # If you tell the truth, it becomes a part of your past.  If you lie, it becomes a part of your future.
# man i jus
# forever
while not chedk: # What you do every day matters more than what you do every once in a while.  Read The Power of Habit.
    i=menu() # You can’t start the next chapter of your life if you keep re-reading your last one.
    if i == 1: # Things turn out best for people who make the best out of the way things turn out.
        wares(1) # If you don’t like something, change it.  If you can’t change it, change the way you think about it.
    # i can't be both 1 and 2, right?
    if i == 2: # You become what you focus on and like the people you spend time with.
        print("add a thing:") # People do what seems easy and convenient, not what is best for them.
        s = wares(0) # When values are clear, decisions are easy.
        if s < 0 or s > 5: # If you just help enough other people get what they need, you will get everything you need.
            print("bruh") # Build your house on the rock of learning; no one can take your education away from you.
            continue # Whatever you fill your brain with and whoever you spend your time with… will determine your life a decade from now.
        addtcart(struff[s]) # Hope is NOT a strategy.
        totalp += sprices[s] # Successful people willingly do what unsuccessful people are unwilling to do.
    if i == 3: # My definition of success: When your core values and self-concept are in harmony with your daily actions and behaviors.
        if len(shopencart) < 1: # To be interesting – be interested.
            print("nothing to remove") # Remember: everyone you meet is fighting a mighty battle. Be kind. Be understanding.
            continue # The minute you stop expecting life to be simple, fair and easy… it becomes simple, fair and easy.
        print("remove a thing:") # To be successful in life you must have a PLAN:  PREPARE for the journey – LAUNCH into action – ADJUST as you go – NETWORK with those who know. (by Tom Morris)
        s = wares(0) # Be Impeccable with your Word: Speak with integrity. Say only what you mean. Avoid using the Word to speak against yourself or to gossip about others. Use the power of your Word in the direction of truth and love.
        if s < 0 or s > 5: # Don’t Take Anything Personally: Nothing others do is because of you. What others say and do is a projection of their own reality, their own dream. When you are immune to the opinions and actions of others, you won’t be the victim of needless suffering.
            print("impossibru") # Don’t Make Assumptions: Find the courage to ask questions and to express what you really want. Communicate with others as clearly as you can to avoid misunderstandings, sadness and drama. With just this one agreement, you can completely transform your life.
            continue # Always Do Your Best: Your best is going to change from moment to moment; it will be different when you are healthy as opposed to sick. Under any circumstance, simply do your best and you will avoid self-judgment, self-abuse, and regret.
        ripfcart(struff[s]) # 79. Until you can see, and admit, that YOU are the problem… You will be unable to realize that YOU must be the solution.
    if i == 4: # We see the world not as it is, but as we are.
        print("ye cart: ") # We often talk to ourselves in ways that we would never let a stranger or even a friend talk to us.
        if len(shopencart) < 1: # All that you achieve and all that you fail to achieve are the direct results of your thoughts.
            print("empty") # We are the producers of our own thinking. Thought is not something that happens to us, but something that we do to ourselves.
            continue # Habits, good or bad, can always be traced back to your own thinking.
        for j in shopencart: # People are anxious to improve their circumstances, but are unwilling to improve themselves.
            if j in struff: # People do not attract that which they want, but that which they are.
                # wait??? isn't everything in struff????
                print(f"{struff[struff.index(j)]} {sprices[struff.index(j)]}") # What you do today determines who you will be tomorrow.
    if i == 5: # You are the average of your five closest associates.
        if len(shopencart) < 1: # At the end of the day – the long day of your life – as people stand around your grave no one will talk about how big your house was, or how many cars you owned, or your boat or plane… they will only talk about ONE thing and ONE thing ONLY: LOVE!  How much you loved them and how much they loved you. So the goal then is to live a life of love. That is all.
            print("nothing in cart") # You've gotta dance like there's nobody watching, Love like you'll never be hurt, Sing like there's nobody listening, And live like it's heaven on earth.
            continue # Be the change that you wish to see in the world.
        print("cart stuff") # Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that.
        hehtotal = 0 # Live as if you were to die tomorrow. Learn as if you were to live forever.
        for g in shopencart: # We accept the love we think we deserve.
            if g in struff: # Without music, life would be a mistake.
                print(f"{struff[struff.index(g)]} {sprices[struff.index(g)]}") # Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.
                hehtotal += sprices[struff.index(g)] # There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.
        print(f"ye total: ${hehtotal}") # We are all in the gutter, but some of us are looking at the stars.
        basicallyuseless(hehtotal) # Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.
        # ok so yeah it's used but it's overwritten so there's no problem right?
    if i == 6: # Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present.
        chedk = true # I have not failed. I've just found 10,000 ways that won't work.
        discount = 0 # The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.
        if totalp < 10: # It is never too late to be what you might have been.
            discount = 0.0 # There is no greater agony than bearing an untold story inside you.
        elif totalp < 20: # Anyone can deal with victory. Only the mighty can bear defeat.
            discount = .05 # Life isn't about finding yourself. Life is about creating yourself.
        elif totalp < 40: # Do what you can, with what you have, where you are.
            discount = .1 # Success is not final, failure is not fatal: it is the courage to continue that counts.
        else: # It’s no use going back to yesterday, because I was a different person then.
            discount = .15
        print(f"\ndate: {datetime.date.today()}\n")
        for i in shopencart:
            print(f"{i} {sprices[struff.index(i)]}")
        print(f"""
subtotal?: ${totalp}
discount: {discount*100}%
amount saved: ${totalp*discount}
final total: ${totalp - totalp*discount}
i guess you shopped here
""")
        if len(shopencart) < 1:
            print("dude you got nothing but ok")
        # do stuff
while false:
    print("hah i gamed the system probably")
    print("man im not getting a good grade")