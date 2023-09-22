# 2 sum problem

# brute force approach
# T.C. => O(n^2)
# Extra space => O(1)

def twoSum(arr,k):

    n= len(arr)

    ans = []

    for i in range(n):

        for j in range(i+1,n):

            if arr[i]+arr[j] == k:
                return [i,j]

print(twoSum([3,2,4],6))

# better approach
# hashmap
# T.C. => O(nlogn)
def twoSum2(arr,k):

    hashmap = {}

    for i in range(len(arr)):

        if (k-arr[i]) not in hashmap:
            hashmap[arr[i]]= i
        
        else:
            return [hashmap[k-arr[i]],i]
        
# approach to check if there is a pair which contains the sum...just return true or false
# T.C. => O(n + nlogn)
# Extra Space Used O(1)
def twoSum3(arr,k):

    arr.sort()

    n = len(arr)

    left = 0
    right = n-1

    while left<right:
        sum = arr[left] + arr[right]

        if sum>k:
            right-=1
        
        if sum<k:
            left+=1
        
        else:
            return "Pair is Present"
    
    return "No Pair for Sum is present"

# print(twoSum3([3,2,4],9))

# ========================================================================================================================================================================

# Sort an array of 0s 1s and 2s

# brute force approach would be to sort the array
# T.C. => O(nlogn)
# Extra Space => O(1)

# better approach
# T.C. => O(N+N) => O(2N)
# Extra Space => O(1)
def sortArray(arr):

    n = len(arr)

    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0

    for i in range(n):

        if arr[i]==0:
            cnt_0+=1
        
        if arr[i]==1:
            cnt_1+=1
        
        if arr[i]==2:
            cnt_2+=1
    
    i = 0

    while cnt_0>0:
        arr[i] = 0
        cnt_0-=1
        i+=1

    while cnt_1>0:
        arr[i] = 1
        cnt_1-=1
        i+=1
    
    while cnt_2>0:
        arr[i] = 2
        cnt_2-=1
        i+=1
    
    return arr

# optimized approach
# dutch national flag algorithm
# T.C. => O(N)
# Extra Space Used => O(1)
def sortArray2(arr):

    n = len(arr)

    low = 0
    mid = 0
    high = n-1

    while mid<=high:

        if arr[mid]==0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        
        elif arr[mid]==1:
            mid+=1
        
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
        
    return arr


# print(sortArray2([0,2,1,2,2,0,0,1,2,1,2,0]))

# =================================================================================================================================

# Majority Element (an element that occurs more than n/2 times in an array)

# brute force approach
# T.C. => O(n^2)
# Extra Space => O(1)
def majorityElement(arr):

    n= len(arr)

    for i in range(n):

        count = 0

        number = arr[i]

        for j in range(i,n):

            if arr[j]==number:
                count+=1

        if count>(n//2):
            return arr[i]
        
    return -1

# better approach
# using hashing
# T.C. => O(nlogn)
# Extra Space => O(n)
def majorityElement2(arr):

    n = len(arr)

    hashmap = {}

    for i in range(n):

        if arr[i] not in hashmap:
            hashmap[arr[i]]=1
        else:
            hashmap[arr[i]]+=1
    
    for i in hashmap:
        if hashmap[i]>n//2:
            return i

    return -1

# optimized approach
# Moore's Voting Algorithm
# T.c. => O(n)
# Extra Space => O(1)
def majorityElement3(arr):

    n = len(arr)

    cnt = 0
    element = arr[0]

    for i in range(n):

        if cnt==0:
            element = arr[i]
            cnt=1

        if arr[i]==element:
            cnt+=1

        else:
            cnt-=1


    cnt = 0
    for i in range(n):

        if arr[i]==element:
            cnt+=1
    
    if cnt>n//2:
        return element
    return -1


# print(majorityElement3([6,5,5,6,6,6,6,5,5,5,5,5,5]))

# =================================================================================================================================

# Maximum Subarray Sum

# brute force approach
# T.C. => O(n^2)
# Extra Space => O(1)
def maxSubarrSum(arr):

    n = len(arr)

    if n==0:
        return arr[0]

    ans = -9999999999

    for i in range(n):

        sum = 0

        for j in range(i,n):

            sum+=arr[j]

            ans = max(ans,sum)
    
    return ans

# optimized approach
# Kadane's Algorithm
# T.C. => O(N)
# Extra Space => O(1)
def maxSubarrSum2(arr):

    n= len(arr)

    if n==1:
        return arr[0]

    maxi = -999999999

    sum = 0

    for i in range(n):

        sum+=arr[i]

        if sum<0:
            sum=0
                
        maxi = max(maxi,sum)
            
    if maxi==0:
        return max(arr)
    return maxi

# follow up queston possible

# There might be more than one subarray with the maximum sum. We need to print any of them

#  approach is to store the starting index and the ending index of the subarray. Thus we can easily get the subarray afterward without actually storing the subarray elements.

# If we carefully observe our algorithm, we can notice that the subarray always starts at the particular index where the sum variable is equal to 0, and at the ending index, the sum always crosses the previous maximum sum(i.e. maxi).

def maxSubArrSum3(arr):

    n = len(arr)

    sum =0

    maxi = -999999999999

    start  = 0
    ansStart , ansEnd = -1,-1

    for i in range(n):

        if sum==0:
            start = i

        sum+= arr[i]

        if sum>maxi:

            maxi = sum
            ansStart = start
            ansEnd = i
        
        if sum<0:
            sum = 0

    return ansStart, ansEnd

arr = [-2,-3,1,2]
startIdx,endIdx = maxSubArrSum3(arr)

for i in range(startIdx,endIdx):
    print(arr[i],end=" ")


# =================================================================================================================================
