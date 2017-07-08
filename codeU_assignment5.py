#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:54:36 2017

@author: hexu
"""

class Node(object):
    """
    a node class, contains attribute:
        - data
        - neighbour (a set of neighbouring nodes)
        # unidirection: A->B (A's neighbour is B, but B's neighbour is not A)
    contains method:
        - add_neighbour
        - printNode
        - get_data
    """
    def __init__(self, data = None, neighbour = None):
        self.data = data
        if neighbour is None:
            self.neighbour = set()
        else:    
            self.neighbour = neighbour

    def add_neighbour(self, new_neighbour):
        self.neighbour.add(new_neighbour)
    
    def get_data(self):
        return self.data
    
    def has_neighbour(self):
        return self.neighbour.__len__()!=0

    def is_neighbour_of(self, aNode):
        return self.data in [x.data for x in aNode.neighbour]
        
    def printNode(self):
        print(str(self.data)+ '-neighbours:' + str([x.data for x in self.neighbour]))
 
class Graph(object):
    """
    a class of directed graph, each node has 3 direction neighbours, contains attributes:
        - node_dict (a set)
    contains methods:
        - add_node (newNode)
        - add_neighbour (fromNode, toNode, direction)
        - find_path (fromNode)
    """
    def __init__(self):
        self.node_dict = set()
        self.node_vals = set()

    def add_node(self, newNode):
        if newNode.data not in self.node_vals:
            self.node_vals.add(newNode.data)
            self.node_dict.add(newNode)
            
    def has_node(self,node):
        return node.data in self.node_vals
        
    def add_neigh(self, fromNode, toNode):
        """
        check if fromNode/toNode already in node_dict, if not, add them
        input:
            - fromNode / toNode: Node object
            - direction (a string: 'left'/'right'/'down')
        """
        if fromNode not in self.node_dict:
            self.add_node(fromNode)
        if toNode not in self.node_dict:
            self.add_node(toNode)
        
        fromNode.add_neighbour(toNode)
        # for test
#        fromNode.printNode()
#        print('has neighbour-'+str(fromNode.has_neighbour()))
    
    def find_path(self, fromNode, visited = None):
        """
        iterate through nodes and find all possible path from given node
        search through each neighbour until there is no neighbour anymore
        """
        # case 1 - for the graph build upon first char order
        if visited is None:
            visited = []
        
        if fromNode not in visited:
            visited.append(fromNode)
            for neigh in fromNode.neighbour:
                self.find_path(neigh, visited)
     
        return visited
    
    def find_isolated_path(self, visited):
        """
        case 2 - find isolated trees/graphs, contains nodes in g.node_dict - set(visited)
        isolated paths can be:
            1. graph
            2. single node (also a graph)
        """
        remainer = self.node_dict - set(visited) # a set of node
        fromNodes = []
        for rNode in remainer:
            is_neigh = False
            for r in remainer:
                if rNode.is_neighbour_of(r):
                    is_neigh = True
                    break
            if is_neigh == False:
                fromNodes.append(rNode)
                
        paths = [visited]
        for fNode in fromNodes:
            new_visit = self.find_path(fNode)
            paths.append(new_visit)
            
        return paths

    def findNode(self,value):
        for n in self.node_dict:
            if n.data == value:
                return n
                
    def printOrder(self, fromChar):
        
        fromNode = self.findNode(fromChar)
            
        visited = self.find_path(fromNode)
        path = self.find_isolated_path(visited)
        
        for p in path:
            for n in p:
                print(n.data)
            print('another order')
            
        print('path finished')

        
        
def findLexOrder(myDict):
    """
    find the lexicographic order from a given dictionalry 
    input:
        - myDict: a list of words (string)
    output:
        - print the list of chars in alien lex order
    
    detail:
        1. read the first chars of each word, make a list
        2. if the list contains duplicates (words with same first char),\
        read the second char of the words with same first char, make new lists
        3. repeat 2 until there is no dupilicates in the lists
        4. turn the lists into a Graph
        5. find the path in the graph and print
        
    external class used:
        - Graph
    """
    prefix = ''

    # find the next char of words given certain prefix, char_list is a 2d list of all ordered chars  
    char_list = findOrderChar(myDict, prefix)
    new_list = []
    # remove duplicate
    for ls in char_list:
        ls = removeDuplicas(ls)
        new_list.append(ls)
        
    
    # turn char_lit into node_list
    node_list = new_list
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            node_list[i][j] = Node(new_list[i][j])
        

    # turn char_list into a Graph
    g = Graph()
    for l in range(len(node_list)):
        lst = node_list[l]
        if len(lst)>0:
            for i in range(len(lst)-1):                   
                nodeS = lst[i]
                nodeE = lst[i+1]
                g.add_neigh(nodeS, nodeE)


    g.printOrder(char_list[0][0])
        
def findOrderChar(myDict, prefix):
    """
    find the next char of given prefix of all the words in myDict
    """
    orderchar = []
    nextchar = []
    if len(prefix) == 0:
        # no prefix required, find the 1st char of all words
        for word in myDict:
            nextchar.append(word[0])
    else:
        # has prefix, find the next char after prefix
        for word in myDict:
            if word.startswith(prefix):
                if len(word)>len(prefix):
                    nextchar.append(word[len(prefix)])
            
#    print('next chars are-')
#    print(nextchar)
    orderchar = [nextchar]
    duplicate_char = findDuplicas(nextchar)
    if len(duplicate_char) == 0:
        # no duplication anymore
        return [nextchar]
    else:
        # has duplication, deal with each one
        duplist = []
        for dup in duplicate_char:
            prefix = prefix+dup
            duplist = findOrderChar(myDict,prefix)
            for d in duplist:
                orderchar.append(d)

    return orderchar
 
def findDuplicas(seq):
    """
    find the duplicated chars in given sequence(list)
    """   
    dup = [x for n, x in enumerate(seq) if x in seq[:n]] 
    return removeDuplicas(dup)

def removeDuplicas(seq):
    """
    remove duplications in a list while keep the order
    """
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]        
            
# test findLexOrder
myDict = ['SUA','SAPM','SAMOX','SOX','UAE','UPO','UX','IOX','IOXAE','PMO','PX','MO','MOX']
charlist = findLexOrder(myDict)

## test list to graph
#g = Graph()
#mylist = [Node('a'),Node('c'),Node('b'),Node('f')]
##mylist = ['a','c','b','f']
#for i in range(len(mylist)-1):
#    nodeS = mylist[i]
#    nodeE = mylist[i+1]
#    g.add_neigh(nodeS, nodeE)
#    
#nodeA = g.findNode('a')
#g.printOrder('a')
## test findOrderChar
#myDict = ['abc','ab','ac']
#oderchar = findOrderChar(myDict,'')
#print(oderchar)
            
## test graph
#g = Graph()
#
## add nodes
#Anode = Node('A')
#Bnode = Node('B')
#Cnode = Node('C')
#Dnode = Node('d')
#Enode = Node('e')
#
## add neighboour
## C <-A->B
##        |
##        d
##   e
#g.add_neigh(Node('A'),Node('B')) # A->B
#g.add_neigh(Node('B'),Node('d'))
##g.add_neighbour(Anode,Cnode)
#g.add_node(Node('e'))
#
##p = g.find_path(Anode)
#g.printOrder(Node('A'))




## test nodes
#Anode = Node('A')
#Bnode = Node('B')
#Cnode = Node('C')
#Dnode = Node('d')
#
## -- make links
## C->A->d
##    |
##    B
#
#Anode.add_neighbour(Bnode)
#Anode.add_neighbour(Cnode)
#Anode.add_neighbour(Dnode)
#Anode.printNode()