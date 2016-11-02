# A program to convert Celsius to Fahrenheit
# It executes 5 times before quit
c1,c2,c3,c4,c5=input("Please enter five Celsius temperatures:")
print"The Fahrenheit temperatures are:" ,
for c in (c1,c2,c3,c4,c5):
    f=9.0/5.0*c+32
    print f,
