#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 23:15:06 2017

@author: hexu
"""

# codeU assignment 2, question 1 and 2 -- BinaryTree without parent node        
        
class BinaryTree(object):

    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left # a tree
        self.right = right # a tree


def findAncestor(tree, poorKid):
    # the first ancestor of a node is itself

    if tree is None:
        # if tree is empty, no ancestor
        return []
    elif tree.key == poorKid:
        return []
    elif tree.left == None or tree.right == None:
        # a node without kids cannot be an ancestor
        return []
    elif tree.left.key == poorKid or tree.right.key == poorKid:
        # the direct ancestor of a key
        return tree.key
    else:
        # not a direct ancestor, find in the subtrees
        if findAncestor(tree.left,poorKid): 
            return findAncestor(tree.left,poorKid)
        if findAncestor(tree.right,poorKid): 
            return findAncestor(tree.right,poorKid)

def findAllAncestor(tree,poorKid):
    if tree is None:
        return None
        
    if tree.key == poorKid:
        return tree.key
        
    # the treenode itself is its ancestor
    Ancestor = [poorKid]
    # append the direct ancestor
    if findAncestor(tree,poorKid):
        Ancestor.append(findAncestor(tree,poorKid))
    else:
        return None
        
    if Ancestor[-1] != tree.key:
        # terminate if the tree root has been collected, 
        # otherwise keep searching for ancestor of the ancestor
        Ancestor.append(findAncestor(tree,Ancestor[-1]))
    return Ancestor
    
def findCommonAncestor(tree,myKid, yourKid):
    # find the ancestor of all kids, two lists are returned
    myAncestor = findAllAncestor(tree, myKid)
    yourAncestor = findAllAncestor(tree, yourKid)
    
    assert myAncestor == None or yourAncestor == None,'sorry kid, cannot find your parent'
    
    # compare the two lists and find the first common item
    if len(myAncestor) >= len(yourAncestor):
        myAncestor, yourAncestor = yourAncestor, myAncestor
        # myKid has less ancestors, is nearer to the node
        # search from myAncestors
    for ancestor in myAncestor:
        if ancestor in yourAncestor:
            return ancestor
        

    

def printTree(tree):
    if tree != None:
        printTree(tree.left)
        print(tree.key)
        printTree(tree.right)

# test my tree
# step1: --- build a test tree   
#       E
#     C, D
#   A,B
left = BinaryTree('A')
right = BinaryTree('B')
treeleft = BinaryTree('C',left, right)
treeNew = BinaryTree('E', treeleft,BinaryTree('D'))

# step 2: --- test valid input (existing tree node)
assert findAllAncestor(treeNew,'B') == ['B', 'C', 'E'], 'cannot find your parents, poor kid'

# step 3: --- test invalid input (non-existing tree node)
assert findAllAncestor(treeNew,'F')== None, 'cannot find your parents, poor kid'

# step 4: --- test common ancestors with valid input
assert findCommonAncestor(treeNew,'B', 'A') == ['C'], 'you don\'t have the same parent, poor kids'

# step 5: --- test common ancesters with invalid input
assert findCommonAncestor(treeNew,'F', 'A') == None, 'you don\'t have the same parent, poor kids'
        
    
