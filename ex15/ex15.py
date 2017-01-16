# importing argv from sys library
from sys import argv

# take script and the filename as arguments
script, filename = argv

# assign the filename to txt variable and open the ex15_sample.txt file
txt = open(filename)

print "Here is your file %r: " % filename
# reads our filename assigned to txt variable
print txt.read()
txt.close()

print "Type the filename again"
file_again = raw_input("> ")

# assign the filename to txt_again variable and open the ex15_sample.txt file
txt_again = open(file_again)

# reads our filename assigned to txt_again variable
print txt_again.read()
txt_again.close()
