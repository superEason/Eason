def DIY_split(mystr,ch):
    import string
    i = string.find(mystr,ch)
    if i==-1:
        return [mystr]
    else:
        return [mystr[0:i]]+DIY_split(mystr[i+1:],ch)

def main():
    s,chrlist = input()
    n = len(chrlist)
    L = []
    L.append(DIY_split(s,chrlist[0]))
    for i in range(1,n):
        m = len(L[i-1])
        for j in range(m):
            L.append([])
            L[i] = L[i]+DIY_split(L[i-1][j],chrlist[i])
    print L[n-1]
    
main()
