def number_needed(a, b):
    len_a = len(a)
    len_b = len(b)
    
    map_char_a = {}
    map_char_b = {}
    
    for c in a:
        if c not in map_char_a:
            map_char_a[c] = 0
        map_char_a[c] += 1
        
    for c in b:
        if c not in map_char_b:
            map_char_b[c] = 0
        map_char_b[c] += 1
    
    num_deletions = 0
    
    #diff_len = abs(len_a - len_b)
    
    #num_deletions += diff_len
    
    for c in range(97,123):
        char_c = chr(c)
        
        count_c_a = 0
        count_c_b = 0
        
        if char_c in map_char_a:
            count_c_a = map_char_a[char_c]
            
        if char_c in map_char_b:
            count_c_b = map_char_b[char_c]
            
        num_deletions += abs(count_c_a - count_c_b)
        
    return num_deletions

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

