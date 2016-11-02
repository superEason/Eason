for i in range(9):
    for j in range(9):
        if i<=j:
            print "%1d*%1d=%2d "%(i+1,j+1,(i+1)*(j+1)),
        else:
            print "       ",
    print
