import sys

"""
Properties for binary tree here:-
1. left < root and root < right.
2. No Duplicates.
"""

""" Node is defined as """
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorderTraversal(root):
    left_inorder = []
    if root.left is not None:
        left_inorder = inorderTraversal(root.left)
    
    root_val = [root.data]
    
    right_inorder = []
    if root.right is not None:
        right_inorder = inorderTraversal(root.right)
    
    return left_inorder + root_val + right_inorder

def check_binary_search_tree_(root):
    
    inorder = inorderTraversal(root)
    
    sorted_inorder = sorted(inorder)
    
    if sorted_inorder != inorder:
        return False
    
    # Check for duplicates
    
    val_count_map = {x:inorder.count(x) for x in set(inorder)}
    
    for key in val_count_map:
        if val_count_map[key] > 1:
            return False
    return True 
