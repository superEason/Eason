file_name = raw_input("Which file to count? ") 
F = open(file_name,"r")
import string
line = F.readlines()
l=len(line)
w=0
for i in range(l):
    w = w + string.count(line[i]," ") + 1
print "There are",l,"lines and",w,"words"


