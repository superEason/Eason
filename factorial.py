def factorial(n):
    if n==0:
        return 1
    elif n>=1:
        return n*factorial(n-1)

def main():
    n = input()
    print factorial(n)

main()
