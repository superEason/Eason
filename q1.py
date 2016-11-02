def DIY_max(mylist):
    if mylist==[]:  
        return
    else:
        m = mylist[0]
        if m<DIY_max(mylist[1:]):   
            m=DIY_max(mylist[1:])
        return m

def main():
    s = input("please enter a list:")
    print DIY_max(s)

main()
