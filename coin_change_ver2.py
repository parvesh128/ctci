#!/bin/python

import sys

def make_change(coins, n):
    m = len(coins)
    table = [[0 for x in range(m)] for x in range(n+1)]
    
    for i in xrange(m):
        table[0][i] = 1
        
    for x in range(1,n+1):
        for y in range(m):
            
            a = table[x - coins[y]][y] if x-coins[y] >= 0 else 0
            
            b = table[x][y-1] if y-1 >= 0 else 0
            
            table[x][y] = a + b
            
    return table[n][m-1]
                
                
            
    

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)

