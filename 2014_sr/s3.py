# the Geneva confection
# basic file input
import os
import sys 
with open(os.path.join(sys.path[0], 's3.5.in'), 'r') as f:
    for i in range(int(f.readline())):
        # this list is listed backwards
        n = int(f.readline())
        numlist = []
        for i in range(n):  
            numlist.append(int(f.readline()))

        branch = []
        lake = []
        # logic start here 
        fail = True
        while fail and len(numlist) > 0: 
            nextCar = 1  
            if len(numlist) > 0 and nextCar == numlist[-1]:
                numlist.pop()
                nextCar = nextCar + 1
            
            elif len(branch) > 0 and nextCar == branch[-1]:
                branch.pop()
                nextCar = nextCar + 1
            
            elif len(numlist) > 0:
                branch.append(numlist.pop())
            
            if len(numlist) == 0 and len(branch) == 0:
                fail = False

        if not fail:
            print('Y')

        else: 
            print('N')

