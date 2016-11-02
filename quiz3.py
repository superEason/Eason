def DIY_split(mystr,ch):
    import string
    i = string.find(mystr,ch)
    a=[]
    while i <> -1:
        n = len(mystr)
        a.append(str(mystr[0:i]))
        mystr = mystr[i+1:n]
        i = string.find(mystr,ch)
    a.append(mystr)
    return a

def main():
    s,c = input()
    print DIY_split(s,c)

main()
        
        
