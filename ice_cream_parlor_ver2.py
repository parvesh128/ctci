def binarySearch(arr,start,end,val):
    
    while True:
        if start > end:
            break
            
        mid = (start + end )/ 2
        
        if arr[mid][0] == val:
            return mid
        
        if arr[mid][0] < val:
            start = mid + 1
            continue
        
        end = mid - 1
        
    return -1


def printCostIDs(firstCostID, secondCostID ):
    
    
    if firstCostID < secondCostID:
        print str(firstCostID) + " " + str(secondCostID)
    else:
        print str(secondCostID) + " " + str(firstCostID)
    

t = int(raw_input().strip())
for a0 in xrange(t):
    
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    
    # n is the number of flavors
    # m is the total sum of dollars
    # a is the actual array of costs
    sorted_a = sorted([(x,idx+1) for idx,x in enumerate(a)])
    len_sorted_a = len(sorted_a)
    
    #print "******************"
    for idx in range(len_sorted_a):
        cost = sorted_a[idx][0]
        other_cost = m - cost
        
        other_cost_idx = binarySearch(sorted_a,0,len_sorted_a-1,other_cost)
        
        if other_cost_idx == -1:
            continue
        
        if other_cost != cost or other_cost_idx != idx:
            first_cost_ID = sorted_a[idx][1]
            second_cost_ID = sorted_a[other_cost_idx][1]
            printCostIDs(first_cost_ID,second_cost_ID)
            break
            
        
        if (idx + 1) >= len_sorted_a or sorted_a[idx+1][0] != other_cost:
            continue
        
        first_cost_ID = a.index(cost) + 1 
        
        second_cost_ID = a.index(cost,first_cost_ID) + 1
        
        printCostIDs(first_cost_ID,second_cost_ID)
        break
