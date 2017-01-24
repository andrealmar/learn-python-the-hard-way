def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# calls the cheese_and_crackers function passing 20,30 as arguments
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# calls the cheese_and_crackers function passing 10 + 20, 5 + 6 as arguments
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"

"""
calls the cheese_and_crackers function passing amount_of_cheese + 100, amount
 _of_crackers + 1000 as arguments
"""
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

cheese_and_crackers(1, 2)

# asking the user to type an input
a = raw_input("Type the ammount of cheese: ")
b = raw_input("Type the ammount of crackers: ")
# calling the function and converting to int so it can do the math
cheese_and_crackers(int(a), int(b))
