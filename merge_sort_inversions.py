class Mergesort:
    def __init__(self,a):
        self.numInv = 0
        self.a = a 
    
    def mergeSort(self):
        self.mergeSortImpl(0,len(self.a)-1)
        
    def mergeSortImpl(self, start, end):
        
        if start >= end:
            return
        
        mid = (start + end) / 2
        
        self.mergeSortImpl(start,mid)
        self.mergeSortImpl(mid+1,end)
        self.mergeTwoHalves(start,mid,end)
        
       
    def mergeTwoHalves(self,lstart,lend,rend):
        rstart = lend + 1
        temp = []
        lidx = lstart
        ridx = rstart
        
        while lidx <= lend and ridx <= rend:
            if self.a[lidx] <= self.a[ridx]:
                temp.append(self.a[lidx])
                lidx += 1
            else:
                temp.append(self.a[ridx])
                ridx += 1
                self.numInv +=  lend + 1 - lidx
        
        #if lstart == 0 and rend == (len(self.a) -1):
        #    return 
         
        if lidx <= lend:
            for idx in range(lidx,lend+1,1):
                temp.append(self.a[idx])
        
        if ridx <= rend:
            for idx in range(ridx,rend+1,1):
                temp.append(self.a[idx])
                
        #self.a = self.a[:lstart] + temp + self.a[rend+1:]
        
        
        for idx in range(len(temp)):
            self.a[lstart + idx] = temp[idx]
            

def count_inversions(a):
    
    msort = Mergesort(a)
    
    msort.mergeSort()
    
    #if msort.a == sorted(a):
    #    print "Array is sorted"
    return msort.numInv
      

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print count_inversions(arr)

