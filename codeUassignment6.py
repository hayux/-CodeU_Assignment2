# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:32:41 2017

@author: hexu
"""

def rearrangeCar(origArray, afterArray, swapList = None, lockPark = None):
    """
    input:
        - origArray (list): the original parking locations of the cars
        - afterArray (list): the parking locations after swapping cars with empty slot
        - swapList (list): the parking locations after each swap, swap only possible between 0 and other slots
        - lockPark (list): the locked parking locations which cannot be swapped with empty slot
    output:
        - swapList
        - lockPark
        - print each swap
    details:
        1. if original parking is the same with after paking, no swap needed, return
        2. if original parking is different from after parking, swap needed: 
            -2.1 find the best location for next swap (findSwapper)
            -2.2 swap the chosen location with 0 
            -2.3 if after swap parking is different from after parking, go to 2.1 
    functions needed:
        - findSwapper
        - swap
        - distance
    O(n):
        - the fastest swapping path = upperbound(N/2)+1, N = length of array
        - each distance calculation scans all elements in array --> O(n)
        - total O(n)=N*(N/2+1)=N*N
    """    
    
    
    if origArray == afterArray:
        print('no move needed any more')
        return origArray, []
        
    if swapList == None:
        swapList = []
    if lockPark == None:
        lockPark = [afterArray.index(0)]
        
    # compute the distance between origArray and afterArray
    dist_orig_after = swapDistance(origArray, afterArray)
    locations = []
    print('original array is '+str(origArray))
    print('after array is '+str(afterArray))
    while dist_orig_after > 1:
        # start swapping
        swappedArray, swapLocation= findSwapper(origArray, afterArray, swapList, lockPark)
#        swappedArray, swapLocation,lock = findSwapper(origArray, afterArray, swapList, lockPark)
        swapList.append(swappedArray)
        locations.append(swapLocation)
#        lockPark.append(lock)
        origArray = swappedArray
        print(swappedArray)
        dist_orig_after = swapDistance(origArray, afterArray)
    
    # if dist_orig_after == 1, swap 0 with the target location in origArray to achieve afterArray
    orig_loc = origArray.index(0)
    after_loc = afterArray.index(0)
    swappedArray = swap(origArray, orig_loc, after_loc)
    locations.append([orig_loc,after_loc])
    print('move 0 to '+str(swappedArray[orig_loc]))
    print(swappedArray)
    swapList.append(swappedArray)
    return swapList, locations
    
def swapDistance(arrayA, arrayB):
    """
    calculate how many swaps needed to turn arrayA into arrayB
    swap can only happens between 0 and another location
    detail:
    1. elementArray = sorted numbers in arrayA/arrayB
    2. locationA = an array contains all the index of elementArray in arrayA
    3. locationB = an array contains all the index of elementArray in arrayB
    4. distance = #Non-Zeros in (locationA-locationB)-1
    """
    locationA = []
    locationB = []
    
    for i in range(len(arrayA)):
        locationA.append(arrayA.index(i))
        locationB.append(arrayB.index(i))
        
    locationDiff = list(map(int.__sub__, locationA,locationB))
    numNonZero = [i for i, v in enumerate(locationDiff) if v != 0]
    distance = len(numNonZero)-1
    return distance
    
def swap(myArray, orig_loc, after_loc):
    #myArray[orig_loc], myArray[after_loc]=myArray[after_loc],myArray[orig_loc]
    newArray = []
    for i in range(len(myArray)):
        if i == orig_loc:
            newArray.append(myArray[after_loc])
        elif i == after_loc:
            newArray.append(myArray[orig_loc])
        else:
            newArray.append(myArray[i])
    
    return newArray
    
def findSwapper(origArray, afterArray, swapList, lockPark):
    """
    find the locations to be swapped with 0, return the location and the swapped array  
    input:
        - origArray (list)
        - afterArray (list)
        - swapList (2d list): keep track of previous swappedArray, no need to visit them again
        - lockPark (list): list of locations need to be locked, locked locations will not be swapped with 0 
    output:
        - location to be swapped with 0
        - swappedArray
    detail:
        1. candidateArray = for all locations in origArray, swap the value with 0, ignore locked locations and those who are
                            already in swapList
        2. calculate the swapDistance between each candidateArray and afterArray
        3. select one candidateArray with minimum swapDistance as swappedArray
        4. return swap location and swappedArray
    """
    candidateArray = swapAllLocation(origArray, swapList, lockPark)

    d_swap_after = []
    for candidate in candidateArray:
        d_swap_after.append(swapDistance(candidate, afterArray))

    if len(d_swap_after)>1:
        swappedArray = candidateArray[d_swap_after.index(min(d_swap_after))]
    else:
        swappedArray = candidateArray[0]

    location = [origArray.index(0),swappedArray.index(0)]


    print('move 0 to '+str(origArray[location[1]]))
    
    return swappedArray, location  
 
def swapAllLocation(origArray, swapList, lockPark):
    """
    swap 0 with all other locations except:
        - locked location in lockPark
        - existing array in swapList
    output:
        - candidateArray (2d list): contains all possible swapped arrays
    """
    candidateArray = []
    orig_loc = origArray.index(0)
    
    for loc in range(len(origArray)):
        
        if loc != orig_loc:
            if loc not in lockPark:
                # not locked location
                tempArray = swap(origArray, orig_loc, loc)
                if tempArray not in swapList:
                    # not come from previous swaps
                    candidateArray.append(tempArray)

    return candidateArray


# test case           
origArray = [1,5,4,3,0,2]
afterArray = [5,0,2,4,1,3]
  
swapList, locations = rearrangeCar(origArray, afterArray)

assert (len(swapList)<=len(origArray)),'too slow'