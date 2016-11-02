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
    s,Lc = input()
    a=[]
    a.append(DIY_split(s,Lc[0]))
    for i in range(1,len(Lc)):
        a.append([])
        for j in range(len(a[i-1])):
            a[i]=a[i]+DIY_split(a[i-1][j],Lc[i])
    print a[len(Lc)-1]

main()
        
        
    
