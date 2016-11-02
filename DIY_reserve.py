def main():
    s = input("Please enter a list:")
    reverse(s)
    print s

def reverse(s):
    L=s
    n=len(L)
    for i in range(0,n/2):
        s[i],s[n-i-1]=s[n-i-1],s[i]

main()
