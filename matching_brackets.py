class BracketType:
    Paren, Brace, Square = range(3)


class BracketNode:
    
    def __init__(self, bracketType):
        self.type = bracketType
        
        
def is_matched(expression):
    bracket_stack = []
    open_bracket_type_map = {'(':BracketType.Paren,
                            '{':BracketType.Brace,
                            '[':BracketType.Square}
    
    close_bracket_type_map = {')':BracketType.Paren,
                             '}':BracketType.Brace,
                             ']':BracketType.Square}
    
    for c in expression:
        
        if c in open_bracket_type_map:
            bracket_node = BracketNode(open_bracket_type_map[c])
            bracket_stack.append(bracket_node)
        elif c in close_bracket_type_map:
            if len(bracket_stack) == 0:
                return False
            top_of_stack = bracket_stack[-1]
            
            if top_of_stack.type != close_bracket_type_map[c]:
                return False
            
            bracket_stack.pop()
            
    if len(bracket_stack) != 0:
        return False
    
    return True

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"

