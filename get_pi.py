def main():
    num = input("Please enter a number:")
    s = get_pi(num)
    a = compare(s)
    if len(a)==2:
        print "We have %s (the same)"%(a[0])
    else: print "We have %s (the same)"%(a)

def get_pi(n):
    s = 0
    for i in range(n):
        s = s+((-1)**i)*4.0/(2*i+1)
    return s
    
def compare(s):
    import math
    s = str(s)
    pi = str(math.pi)
    same = ""
    i = 0
    while i>=0:
        if s[i]==pi[i]:
            same = same + s[i]
        else: i = -2
        i = i + 1   
    return same 
        
    
    
main()
