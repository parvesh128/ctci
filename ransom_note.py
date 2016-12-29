def ransom_note(magazine, ransom):
    
    map_magazine = {}
    
    for word in magazine:
        if word not in map_magazine:
            map_magazine[word] = 0
        map_magazine[word] += 1
        
    for word in ransom:
        if word not in map_magazine:
            return False
        count_word = map_magazine[word]
        count_word -= 1
        
        if count_word == 0:
            del map_magazine[word]
        else:
            map_magazine[word] = count_word
            
            
            
    return True
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    

