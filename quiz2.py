def DIY_bin(num):
    s=""
    while num!=0:
        s,num=str(num%2)+s,num/2
    return "ob"+s
        
def main():
    b=input()
    print DIY_bin(b)

main()
        
        
