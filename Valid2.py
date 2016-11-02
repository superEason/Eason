# Judging whether or not the date is valid
def date_input():
    import string
    input_date = raw_input("Please enter a date in the form morth/day/year:")
    [m,d,y] = input_date.split('/')
    date = [int(m),int(d),int(y)]
    return date

def leap_year(y):
    if y%4==0 and (y%100!=0 or y%400==0):
        return True
    else:
        return False

def max_day(m,year):
    A=[1,3,5,7,8,10,12]
    B=[4,6,9,11]
    if m in A :
        Max = 31
    elif m in B :
        Max = 30
    elif m==2 :
        if year :
            Max = 29
        else:
            Max = 28
    else:
        Max = 0
    return Max
        
def judging(date):
    m = date[0]
    d = date[1]
    y = date[2]
    Max = max_day(m,leap_year(y))
    if d>0 and d<=Max:
        return True        
    else:
        return False
               
def output(date,judgement):
    if judgement:
       print "The date is valid"
    else:
       print "The date is not valid" 
        
def main():
    date = date_input()
    judgement = judging(date)
    output(date,judgement)

main()
