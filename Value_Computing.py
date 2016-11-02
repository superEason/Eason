# An advanced program to compute the value of an investment
print"This program calculates the future value"
principal=input("Please enter the initial principal:")
year=input("Please enter the investment years:")
apr=input("Please enter the annual interest rate:")
for i in range(year):
    principal=principal*(1+apr)
print"The value in",year,"years is:",principal

