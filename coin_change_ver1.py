#!/bin/python

import sys

def make_change(coins, n):
    
    ways = {}
    ways[0] = [] # Empty list
    
    sorted_coins = sorted(coins)
    
    for val in xrange(1,sorted_coins[0]):
        ways[val] = []
        
    for val in xrange(sorted_coins[0],n+1,1):
        cur_ways = []
        
        if val in sorted_coins:
            cur_ways.append([val])
            
        coin_idx = 0
        ways_done_map = {}
        while True:
            
            if coin_idx >= len(sorted_coins):
                break
                
            coin = sorted_coins[coin_idx]
            coin_idx += 1
            
            if coin >= val:
                break
            
            rem_val = val-coin
            
            
            if coin in ways_done_map or rem_val in ways_done_map:
                continue
            
            temp_ways = ways[rem_val]
            
            if len(temp_ways) == 0:
                continue
            
            
            for way in temp_ways:
                #print way
                new_way = way[:]
                new_way.append(coin)
                new_way = sorted(new_way)
                
                if new_way in cur_ways:
                    continue
                    
                cur_ways.append(new_way)
        
            ways_done_map[coin] = True
            ways_done_map[rem_val] = True
        ways[val] = cur_ways        
    
    return len(ways[n])            
                
                
            
    

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)

