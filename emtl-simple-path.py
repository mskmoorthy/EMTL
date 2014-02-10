import itertools
print "0", "\t", 1
print "1","\t",3
for j in range(5,17,2):
    x = range(1,j+1)
    sum2 = 0
    for a in itertools.permutations(x):
        x = list(a)
        sum1 = x[0]+x[1]+x[2]
        d = 1
        for i in range(2,j-2,2):
            if (sum1== x[i]+x[i+1]+x[i+2]):
                d = 1
            else:
                d = 0
                break
        if (d==1):
            if (a[0]<a[j-1]):
                #print x, sum1
                sum2 = sum2+1
    print (j-1)/2, "\t", sum2
