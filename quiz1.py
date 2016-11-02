def DIY_max(mylist):
    n = len(mylist)
    m = mylist[0]
    for i in range(n):
        if mylist[i]>=m:
            m = mylist[i]
    return m

def main():
    s = input("please enter a list:")
    print DIY_max(s)

main()
