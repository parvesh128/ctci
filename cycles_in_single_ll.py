"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
""" 
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    hare = head
    tort = head 
    
    while True:
        
        if hare is None:
            return False
        hare = hare.next
        if hare is None:
            return False
        
        hare = hare.next
        tort = tort.next
        
        if hare == tort:
            return True
        
    return True
    

