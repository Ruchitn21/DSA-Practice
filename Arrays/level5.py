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

# print(rearrangeSigns3([3,1,-2,-5,2,-4,-5,-9,-8,-10]))

# =====================================================================================================================

# Stock buy sell problem
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# brute force approach
def stockProblem(arr):
    
    n = len(arr)

    mini = arr[0]

    maxProfit = 0

    for i in range(n):

        cost = arr[i] - mini

        maxProfit = max(maxProfit,cost)

        mini = min(mini,arr[i])
    
    return maxProfit

# print(stockProblem([7,1,5,3,6,4]))

# ===========================================================================================================

# Leaders in an Array
# Leaders are those elements which are greater then all the elements in their right

# Brute Force Approach
# T.C. => O(N^2)
# Extra Space used => O(N) => in worst case when the array is in decreasing order and all elements will become leaders
def leaderArray(arr):

    n = len(arr)

    leaders= []

    for i in range(n):

        leader = True

        for j in range(i+1,n):

            if arr[j]>arr[i]:
                leader = False
                break

        if leader:
            leaders.append(arr[i])

    return leaders

# optimized approach
# T.c. => O(N)
# Extra Space => O(N) => in worst case when the array is in decreasing order and all elements will become leaders
def leaderArray2(arr):

    n = len(arr)

    leaders= [arr[n-1]]

    max_right = arr[n-1]

    for i in range(n-1,-1,-1):

        if arr[i]>max_right:

            leaders.append(arr[i])

            max_right = arr[i]
    
    return leaders[::-1]

# print(leaderArray2([10,22,12,3,0,6]))

# ====================================================================================================================================

# Longest Consecutive Sequence
# Return the length of the consecutive sequence

# brute force approach
# T.C. => O(N^2)
def longestConsecutive(arr):

    n = len(arr)

    maxLength = 0

    for i in range(n):

        length = 1
        for j in range(n):

            if arr[i]==arr[j]:
                length+=1
                maxLength = max(maxLength,length)
    
    return maxLength

# better approach
# T.C. => O(nlogn + N)
# Extra Space Used => O(1)
def longestConsecutive2(arr):

    n= len(arr)

    arr.sort()

    count = 0
    longest = 1

    lastSmaller= -9999999999999

    for i in range(n):

        if arr[i]-1==lastSmaller:
            count+=1
            lastSmaller = arr[i]
        elif arr[i]!=lastSmaller:
            count = 1
            lastSmaller = arr[i]

        longest = max(longest, count)
    
    return longest

# Optimized Approach
# We will adopt a similar approach to the brute-force method but with optimizations in the search process. Instead of searching sequences for every array element as in the brute-force approach, we will focus solely on finding sequences only for those numbers that can be the starting numbers of the sequences. This targeted approach narrows down our search and improves efficiency.

# We will do this with the help of the Set data structure.

# T.c.=> O(3N)
# Extra space Used => O(N)
def longestConsecutive3(arr):

    n = len(arr)
    
    count = 0

    longest = 1

    hashset = set()

    for i in arr:
        hashset.add(i)
    
    for i in hashset:

        if i-1 not in hashset:
            x = i
            count = 1

            while x+1 in hashset:
                count+=1
                x+=1
            
            longest = max(longest,count)
    
    return longest

print(longestConsecutive3([102,4,100,1,101,3,2,1,1]))

# [1,1,1,2,3,4,100,101,102]

            
