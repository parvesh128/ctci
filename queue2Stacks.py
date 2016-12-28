class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peekOrPop(self,flag):
        
        if len(self.second) == 0:
            first_len = len(self.first)

            for ctr in xrange(first_len):
                self.second.append(self.first.pop())

        if flag == 0:
            retval = self.second.pop()
        else:
            retval = self.second[-1]
        
            #second_len = len(self.second)
            #for ctr in xrange(second_len):
                #self.first.append(self.second.pop())
        
        return retval
        
    
    def peek(self):
        #print self.first
        #print self.second
        return self.peekOrPop(1)
        
        
    def pop(self):
        #print self.first
        #print self.second
        return self.peekOrPop(0)
        
        
    def put(self, value):
        self.first.append(value)
        

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        

