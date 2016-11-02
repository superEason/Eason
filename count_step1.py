def creat_rand_array(x,y):
    import random
    a = []
    for i in range(x):
        a.append([])
        for j in range(y):
            a[i].append(random.randint(0,100))
    return a
    

def count_array(myarray):
    counts  = {}
    for i in myarray:
        for j in i:
            if j in counts:
                counts[j] += 1
            else: counts[j] = 1
    return counts

def main():
    row,col = input("Please enter row and column:")
    myarray = creat_rand_array(row,col)
    print myarray
    counts = count_array(myarray)
    print counts
    raw_input("Press Enter key...")

main()
