# Fast way to create list and dicts
numbers = range(0,50)

print "Showing numbers"
print "---------------"
print numbers

print "Showing even numbers"
print "--------------------"
even_numbers = [i for i in range(0,50) if i % 2 == 0 and i >= 2 ]

print even_numbers

print "Showing even numbers again"
print "--------------------------"
even_numbers = [i for i in numbers if i % 2 == 0 and i >= 2 ]

print "Showing squares"
print "---------------"
squares = [i*i for i in numbers if i %  2 == 0 and i >=2]
print squares


print "Showing randoms"
print "---------------"
import random
random_numbers = [ random.randint(1,100) for x in range(50) ]
print random_numbers

print "Showing randoms unique using set"
print "--------------------------------"
unique_random_numbers = list(set(random_numbers))
print unique_random_numbers
print len(unique_random_numbers)
print "verses " + str(len(random_numbers))

print "Showing names as titles"
print "--------------------------------"
names = ['adam', 'Justin', 'joe', 'tony', 'zoe']
names_formatted = [x.title() for x in names]
print names_formatted

print "Showing names as titles"
print "--------------------------------"
names_formatted = map(lambda x: x.title(), names)
print names_formatted

print "Showing names starting with j"
print "--------------------------------"
names_starting_with_j = [name for name in names_formatted if name[0].lower() == 'j' ]
print names_starting_with_j

## Encoding example
import string
from random import shuffle
#-------------------------------------------------------------------------------
# Set the origional text string.
raw_text = "Hello and welcome to Linux Academy!!"
#-------------------------------------------------------------------------------
# Make a list of letters in order
letters = list(string.ascii_letters)

# copy the letters to an encoded letter list.
encoded_letters = letters[:]

# Shuffle the leters to mix them up randomaly.
shuffle(encoded_letters)
print "Encoded letters"
print letters
print "Mixed up letters"
print encoded_letters

# Create dictonary to hold the keys
encoding_key = {}
decoding_key = {}

# Take the two list letters, and encoded_letters and turn them
# into keys for decoding.
# encoding_key[ letters ] = encoded_letters
# decoding_key[ encode_letters ] = letters
for k, v in zip(letters, encoded_letters):
	encoding_key[k]=v
	decoding_key[v]=k

print 'Showing the encoding key'
print '------------------------'
print encoding_key

encoded_text = ''
for letter in raw_text:
	# get(key[, default])
	encoded_text += encoding_key.get(letter, letter)

print 'Showing the encoding Text'
print '------------------------'
print encoded_text

print 'Showing the encoding Text alternative way'
print '-----------------------------------------'
# Long form of how the zip / dict is working to create a dict
# >>> lista = 'aa', 'BB'
# >>> lista
# ('aa', 'BB')
# >>> listb = 'cc', 'DD'
# >>> listb
# ('cc', 'DD')
# >>> listC = zip(lista, listb)
# >>> listC
# [('aa', 'cc'), ('BB', 'DD')]
# >>> dicta = dict(listC)
# >>> dicta
# {'aa': 'cc', 'BB': 'DD'}
encoding_key = dict(zip(letters,encoded_letters))
decoding_key = dict(zip(encoding_key.values(),encoding_key.keys()))

encoded_text = ''.join([encoding_key.get(w,w) for w in raw_text])
print "Printing the encoded text"
print "-------------------------"
print encoded_text
# join will make it a string
decoded_text = ''.join([ decoding_key.get(w,w) for w in encoded_text])

print "Printing the decoded text"
print "-------------------------"
print decoded_text

