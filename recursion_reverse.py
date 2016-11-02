def main():
    s = input("Please enter a list:")
    ss = reverse(s,0)
    print ss

def reverse(s,i):
    n = len(s)
    if i<(n/2):
        s[i],s[n-i-1] = s[n-i-1],s[i]
        return reverse(s,i+1)
    else: return s
    

main()
    
    
