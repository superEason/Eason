def main():
    num = input("Please enter a number:")
    b = judging(num)
    if b :
        print num,"is a prime number"
    else:
        print num,"is not a prime number"    
    raw_input("Press enter key...")

def judging(a):
    b=int(a**0.5)
    while b >= 2 :
        if a % b != 0:
            b = b-1
        else:
            return False
            b = 0
    if b == 1 :
        return True

main()
    
