def DIY_bin(num):
    if num==0:
        return ""
    else:
        return DIY_bin(num/2)+str(num%2)

def main():
    n=input("enter a number:")
    s=DIY_bin(n)
    print "ob"+s

main()
