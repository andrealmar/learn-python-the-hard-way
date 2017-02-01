numbers = []


def num_append(head, tail):

    for i in range(head, tail):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

        print "The numbers: "


num_append(0, 9)

for num in numbers:
    print num
