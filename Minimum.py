n = input("Please enter a number for size of a list:")
a=[0]
for i in range(n):
    a.append(input("Please enter a number"))
m = a[1]
for i in range(n-1):
    if m>a[i+1]:
        m=a[i+1]
print "The min of the list is:",m

    
