import itertools
pool = (1,2,3,4)
viable = itertools.combinations(pool,len(pool)-1)
for x in viable:
    print(x)