# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:21:56 2017

@author: hexu
"""

def countIslands(nRow, nCol, boolArray):
    """
    funtion: 
    to find the number of islands in the given boolArray
    island -- > 2 adjacent True-s, horizontally or vertically, not diagonally
    
    input: 
    nRow, nCol --> number of rows and columns
    boolArray --> a 2d array made of booleans
    
    output: 
    number of adjacent 2-True-s
    
    algo details:
    1. turn boolArray into binary matrix (use function turnBool2Binary)
    2. for each row: count the number of islands (use function countOnes)
    3. for each colomn: count the number of islands (use function countOnes)
    4. sum up the number of islands and return
    
    external function:
    turnBool2Binary --> details in the function description
    countOnes --> details in the function description
    """
    
    # step 1 -- turn boolean array into binary array, True = 1, False = 0
    myArray = turnBool2Binary(boolArray)
    
    # step2 -- count the number of islands in each row
    rowIsland = 0
    for r in range(nRow):
        # get each row
        row = myArray[r]
        # count number of islands in each row and add up
        rowIsland = rowIsland + countOnes(row)
    
    # step3 -- count the number of islands in each colomn
    
    # transpose myArray for colomn operation, colomns of original myArray becomes rows of transposed myArray
    myArray = list(map(list,zip(*myArray)))
    colIsland = 0
    for c in range(nCol):
        # get each colomn
        col = myArray[c]
        # count the number of islands in each colomn and add up
        colIsland = colIsland + countOnes(col)
        
    return rowIsland+colIsland
    
def countOnes(row):
    """
    function:
    to find the number of islands in a row
    islands --> 2 adjacent 1s
    
    input: 
    row --> 1d binary array
    
    output:
    numIs --> number of islands
    
    algo details:
    1. find the number of consecutive 1s in the row
        Can be done by array manipulation
        1.1 calculate the diffArray --> for all x[i, i>0]: calculate x[i]-x[i-1]
        1.2 find all the indices of -1 in the diffArray (-1 comes from .....1 0....., marks the end of 1s)
        1.3 find all the indices of 1 in the diffArray (1 comes from ....0 1....., marks the start of 1s)
        1.4 the lengths list of consecutive 1s can be calculated by the result (1.2)-(1.3)
        1.5 drop the length which is smaller than 1 from the length list
        
        OR can be achieved in O(n)
        1.1 initialize pointerStart and pointerEnd as 0
        1.2 start moving pointerStart and pointerEnd until meeting 1
        1.3 keep moving pointerStart until meeting 0, pointerEnd stays
        1.4 the length of consecutive 1s = pointerStart-pointerEnd
        
    2. number of islands = number of consecutive 1s -1
    
    """
    
    # 1 -- find the number of consecutive 1s in the row
    
    # 1.1 -- calculate the diffArray
    shiftLeft = [0] + row
    shiftRight = row + [0]
    diffArray = list(map(int.__sub__, shiftRight,shiftLeft))
    
    # 1.2 -- find all the indices of -1 in the diffArray 
    ending = [i for i,val in enumerate(diffArray) if val==-1]
    
    # 1.3 -- find all the indices of 1 in the diffArray
    start = [i for i,val in enumerate(diffArray) if val==1]
            
    # 1.4 -- the lengths list of consecutive 1s can be calculated by the result ending - start
    lengthList = list(map(int.__sub__, ending,start))
            
    # 1.5 -- remove the length == 1 elements from lengthList
    lengthList = [value for value in lengthList if value != 1]
    
    # 2 -- count the number of islands = sum(number of consecutive 1s - 1)
    numIs = sum(lengthList)-len(lengthList)
    
    return numIs
            
def turnBool2Binary(boolArray):
    for row in range(len(boolArray)):
        for col in range(len(boolArray[row])):
            if boolArray[row][col] == False:
                boolArray[row][col] = 0
            else:
                boolArray[row][col] = 1
                
    return boolArray
    




# test cases

            
            
            
            
            
            
            
            
            
            
            
            
    
    