# a program that counts the number of words in a sentence
sentence=raw_input("Please enter a sentence:")
import string
import re
s=sentence.count(" ") + 1
print "There are",s,"words in the sentence."
