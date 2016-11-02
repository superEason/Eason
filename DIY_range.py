def DIY_range(a):    
    s = []
    if len(a)==1:
        n = 1
        while n<a[0]:
            s.append(n)
            n = n+1
    elif len(a)==2:
        n = a[0]
        while n<a[1]:
            s.append(n)
            n = n+1
    elif a[2]>0:
        n = a[0]
        while n<a[1]:
            s.append(n)
            n = n+a[2]
    else:
        n = a[0]
        while n>a[1]:
            s.append(n)
            n = n+a[2]
    return s

def main():
    a=input()
    s=DIY_range(a)
    print s

main()
    
        

    
