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


def findAncester(tree, poorKid):
    # the first ancester of a node is itself

    if tree is None:
        # if tree is empty, no ancester
        return []
    elif tree.key == poorKid:
        return []
    elif tree.left == None or tree.right == None:
        # a node without kids cannot be an ancester
        return []
    elif tree.left.key == poorKid or tree.right.key == poorKid:
        # the direct ancester of a key
        return tree.key
    else:
        # not a direct ancester, find in the subtrees
        if findAncester(tree.left,poorKid): 
            return findAncester(tree.left,poorKid)
        if findAncester(tree.right,poorKid): 
            return findAncester(tree.right,poorKid)

def findAllAncester(tree,poorKid):
    if tree is None:
        return None
        
    if tree.key == poorKid:
        return tree.key
        
    # the treenode itself is its ancester
    Ancester = [poorKid]
    # append the direct ancester
    if findAncester(tree,poorKid):
        Ancester.append(findAncester(tree,poorKid))
    else:
        return None
        
    if Ancester[-1] != tree.key:
        # terminate if the tree root has been collected, 
        # otherwise keep searching for ancester of the ancester
        Ancester.append(findAncester(tree,Ancester[-1]))
    return Ancester
    
def findCommonAncester(tree,myKid, yourKid):
    # find the ancesters of all kids, two lists are returned
    myAncester = findAllAncester(tree, myKid)
    yourAncester = findAllAncester(tree, yourKid)
    
    assert not (myAncester is None) or (yourAncester is None),'sorry kid, cannot find your parent'
    
    # compare the two lists and find the first common item
    if len(myAncester) >= len(yourAncester):
        myAncester, yourAncester = yourAncester, myAncester
        # myKid has less ancesters, is nearer to the node
        # search from myAncesters
    for ancester in myAncester:
        if ancester in yourAncester:
            return ancester
        

    

def printTree(tree):
    if tree != None:
        printTree(tree.left)
        print(tree.key)
        printTree(tree.right)
        
# build a test tree   
#       E
#     C, D
#   A,B
left = BinaryTree('A')
right = BinaryTree('B')
treeleft = BinaryTree('C',left, right)
treeNew = BinaryTree('E', treeleft,BinaryTree('D'))
#findAllAncester(treeNew,'B')
#findAllAncester(treeNew,'A')
print(findAllAncester(treeNew,'B'))
print(findAllAncester(treeNew,'F'))
print(findCommonAncester(treeNew,'B', 'A'))
        
    