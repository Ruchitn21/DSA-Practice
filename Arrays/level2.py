# left rotate the array by 1 place

# time complexity O(n)
# space used in algorithm O(n) but extra space used in algorithm O(1)
def leftRotate1(arr):

    n= len(arr)

    temp = arr[0]

    for i in range(n-1):

        arr[i] = arr[i+1]
    
    arr[n-1] = temp

    return arr

# print(leftRotate1([1,2,3,4,5]))

# ================================================================================================================================

# rotate array by K places

# brute force approach
# T.C. => O(d) + O(n-d) + O(d) => O(n+d)
# Extra Space => O(d)
def rotateK(arr,k):

    n= len(arr)

    temp_arr = []

    d = k%n

    for i in range(d):
        temp_arr.append(arr[i])
    
    for i in range(d,n):
        arr[i-d] = arr[i]
    
    j = 0
    x = n-d

    while x<n:
        arr[x] = temp_arr[j]
        j+=1
        x+=1

    
    return arr

# space optimal approach
# T.C. =>
# Extra Space => O(1)

def reverseArr(arr,left,right):

    while left<right:
        arr[left],arr[right] = arr[right], arr[left]
        left+=1
        right-=1

def rotateK2(arr,k):

    n= len(arr)

    d= k%n

    i =0

    reverseArr(arr,i,d)
    reverseArr(arr,d+1,n-1)
    reverseArr(arr,i,n-1)

    return arr

# print(rotateK2([1,2,3,4,5,6,7],9))


# =============================================================================================================================

# move all zeroes at the end of the array

# brute force solution
# T.C. => O(n)
# Extra Space Used => O(n)
def moveZeroes(arr):

    n= len(arr)

    cnt_0 = 0

    for i in range(n):

        if arr[i]==0:
            cnt_0 +=1
        
    ans_arr = [-1]*n

    i=0
    j=0

    while i<n:
        if arr[i]!=0:
            ans_arr[j]=arr[i]
            j+=1
        i+=1
    
    while j<n:
        ans_arr[j]=0
        j+=1
    
    return ans_arr

# optimal approach
def moveZeroes2(arr):

    n = len(arr)

    j =0

    for i in range(n):
        if arr[i]==0:
            j = i
            break

    for x in range(j+1,n):

        if arr[x]!=0:
            arr[x],arr[j]= arr[j],arr[x]
            j+=1
    

    return arr

    

# print(moveZeroes2([1,0,3,5,9,0,0,6,7]))

# ====================================================================================================================

# union of 2 sorted arrays

# brute force approach
# T.C. => O(nlogn) + O(mlogn) + O(n+m) 
# Extra Space => O(n+m)
def union(arr1,arr2):

    n= len(arr1)
    m= len(arr2)

    temp_set =set()

    for i in range(n):
        temp_set.add(arr1[i])
    
    for j in range(m):
        temp_set.add(arr2[j])
    
    # return temp_set

# optimized approach
# T.C. => O(n+m)
# Extra space used => O(n)
def union2(arr1,arr2):

    n= len(arr1)
    m= len(arr2)

    i=0
    j=0

    ans_arr = []

    while i<n and j<m:
        if arr1[i]<arr2[j]:

            ans_arr.append(arr1[i])
            i+=1
        
        elif arr2[j]<arr1[i]:
            ans_arr.append(arr2[j])
            j+=1

        else:
            ans_arr.append(arr2[j])
            i+=1
            j+=1
    
    while i<n:
        ans_arr.append(arr1[i])
        i+=1
    
    while j<m:
        ans_arr.append(arr2[j])
        j+=1
        

    return ans_arr

# print(union2([1,1,2,3,4,5],[2,3,4,4,5,6]))

# ================================================================================================================================

# find intersection of 2 sorted arrays. Also keep a check of duplicates

# brute force
# T.C. => O(n*m)
# Extra space user => O(max(m)+min(n,m))
def intersection1(arr1,arr2):

    n= len(arr1)
    m = len(arr2)

    ans = []

    visited= [0]*max(arr2)

    for i in range(n):

        for j in range(m):

            if arr1[i]==arr2[j] and visited[arr2[j]]!=1:

                ans.append(arr1[i])
                visited[arr2[j]]=1
    
    return ans 

# optimal approach
def intersection2(arr1,arr2):

    n= len(arr1)
    m= len(arr2)

    ans = []

    i=0
    j=0

    while i<n and j<m:

        if arr1[i]<arr2[j]:

            i+=1
        
        elif arr1[i]>arr2[j]:
            j+=1
        
        else:
            ans.append(arr1[i])
            i+=1
            j+=1
    
    return ans
        
# print(intersection2([1,1,2,2,3,3,4,4],[1,1,2,2,3,3,4,4]))

# =====================================================================================================================================

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# brute force
# T.C. => O(n+nlogn)
def missingNumber(arr):

    hashmap = dict()

    for i in range(len(arr)):

        if arr[i] not in hashmap:
            hashmap[arr[i]]=1
        
    for i in range(0,len(arr)):

        if i not in hashmap:
            return i

    return -1

# optimal approach
def missingNumber2(arr):
    
    n= len(arr)

    total_sum= (n*(n+1))//2

    arr_sum = sum(arr)

    return total_sum-arr_sum

# print(missingNumber2([0,3,1]))

# =====================================================================================================================================

# max consecutive ones

# brute and optimal approach
# T.C. => O(n)
# Extra Space => O(1)
def maxConsecutiveOnes(arr):

    n = len(arr)

    cnt_ones= 0

    ans = -1

    for i in range(n):

        if arr[i]==1:
            cnt_ones+=1

            ans = max(ans,cnt_ones)
        
        else:
            cnt_ones = 0
    
    return ans

# print(maxConsecutiveOnes([1,1,0,1,1,1,0,1,1]))

# =======================================================================================================

# find the number that appears once among other numbers that appear more than once

# brute force approach
# using linear search for every element
# T.C. => O(n^2)
# Extra Space => O(1)
def uniqueElement(arr):
    
    for i in range(len(arr)):
        
        count = 0
        
        for j in range(len(arr)):
            
            if arr[j]==arr[i]:
                
                count+=1
        
        if count==1:
            return arr[i]
            
    return -1

# Better Approach
# using hashmap to store frequencies of every element
# T.C. => O(nlogm + n)
def numberOnce(arr):

    hashmap = {}

    for i in range(len(arr)):

        if arr[i] not in hashmap:
            hashmap[arr[i]]=1
        else:
            hashmap[arr[i]]+=1

    # return hashmap
    
    for i in range(len(arr)):
        if hashmap[arr[i]]==1:
            return arr[i]
        
    return -1

# Optimized Approach
# using XOR in the whole array
# T.C. => O(N)
# Extra Space => O(1)
def uniqueElement2(arr):

    ans = 0
    
    for i in range(len(arr)):
        ans^=arr[i]

    return ans
    
print(numberOnce([4,1,2,1,2]))
