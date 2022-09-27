
inputString = input("Please give your input: ")
algorithm_Type = inputString[-1:]   #get the last algo var
inputString = inputString[:-2]      #pancake order
inputList = []

# convert string to array
while(inputString):
    inputList.append(inputString[:2])
    inputString = inputString[2:]

def flip(arr, i):
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1
  
# Returns index of the maximum

def findMax(arr, n):
    mi = 0
    for i in range(0,n):
        if arr[i] > arr[mi]:
            mi = i
    return mi
  
# The main function that 
# sorts given array 
# using flip operations
def pancakeSort(arr, n):
      
    # Start from the complete
    # array and one by one
    # reduce current size
    # by one
    curr_size = n
    while curr_size > 1:
        # Find index of the maximum
        # element in 
        # arr[0..curr_size-1]
        mi = findMax(arr, curr_size)
  
        # Move the maximum element
        # to end of current array
        # if it's not already at 
        # the end
        if mi != curr_size-1:
            # To move at the end, 
            # first move maximum 
            # number to beginning 
            flip(arr, mi)
  
            # Now move the maximum 
            # number to end by
            # reversing current array
            flip(arr, curr_size-1)
        curr_size -= 1
  

# print an array of size n 
def printArray(arr, n):
    for i in range(0,n):
        print ("%d"%( arr[i]),end=" ")
  


n = len(inputString)
pancakeSort(inputString, n);
print ("Sorted Pancake:  ")
printArray(inputString,n)