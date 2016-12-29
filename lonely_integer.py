#!/bin/python

import sys

def lonely_integer(a):
    
    bit_map = 0
    
    for num in a:
        bits_to_shit = 0
        
        if num > 0:
            bits_to_shit = num - 1
            
        bit_map = bit_map ^ (1 << bits_to_shit)
        
    num = 0
    while True:
        if bit_map == 0:
            break
        bit_map = bit_map >> 1
        num += 1
        
    return num
        
        
    

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)

