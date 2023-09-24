# Rearrange positives and negatives alternately in the array


# Brute Force Approach
# T.C. => O(2N)
# Extra Space => O(n)
def rearrangeSigns(arr):

    positives= []
    negatives = []

    n= len(arr)

    for i in range(n):

        if arr[i]<0:
            negatives.append(arr[i])
        else:
            positives.append(arr[i])
    
    ans_arr= [0]*(len(positives+negatives))

    i = 0
    j= 0

    while j<len(positives):

        ans_arr[i] = positives[j]
        i+=2
        j+=1
    
    i = 1
    j= 0

    while j<len(negatives):

        ans_arr[i] = negatives[j]
        i+=2
        j+=1

    return ans_arr

# better approach
# T.C. => O(N)
# Extra Space => O(N)
def rearrangeSigns2(arr):

    n = len(arr)

    pos_idx = 0
    neg_idx = 1

    ans_arr= [0]*n

    for i in range(n):

        if arr[i]>0:
            ans_arr[pos_idx] = arr[i]
            pos_idx+=2

        elif arr[i]<0:
            ans_arr[neg_idx] = arr[i]
            neg_idx+=2
        
    return ans_arr

# Variety 1 
# This time there might not be equal number of positives and negatives so add the remaining left elements from the end 
# this time we will go back to brute force approach to solve this problem

# T.C. = > O(2N)
# Extra Space = O(N)
def rearrangeSigns3(arr):

    n = len(arr)

    positives= []
    negatives = []

    for i in range(n):

        if arr[i]>0:
            positives.append(arr[i])
        
        else:
            negatives.append(arr[i])
    
    if len(positives)>len(negatives):
        
        for i in range(len(negatives)):
            
            arr[2*i] = positives[i]
            arr[2*i+1] = negatives[i]
        
        pos_idx = 2*len(negatives)

        for i in range(pos_idx,len(positives)):
            arr[i] = positives[i]

    else:
        for i in range(len(positives)):
            
            arr[2*i] = positives[i]
            arr[2*i+1] = negatives[i]
        
        neg_idx = 2*len(positives)

        for i in range(neg_idx,len(negatives)):
            arr[i] = negatives[i]

    return arr

print(rearrangeSigns3([3,1,-2,-5,2,-4,-5,-9,-8,-10]))
