import string
date = raw_input("Please enter a date in the form morth/day/year:")
[m,d,y] = string.split(date,'/')
m,d,y =int(m),int(d),int(y)
if m<=12:
    if m==2:
        if y%4==0 and (y%100!=0 or y%400==0):
            if d<=29:
                print date,"is valid"
            else:
                print date,"is not valid"
        elif d<=28:
                print date,"is valid"
        else:
            print date,"is not valid"
    elif m==4 or m==6 or m==9 or m==11:
        if d<=30:
                print date,"is valid"
        else:
            print date,"is not valid"
    elif d<=31:
        print date,"is valid"
    else:
        print date,"is not valid"
else:
    print date,"is not valid."
        
