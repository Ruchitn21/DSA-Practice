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

print(twoSum3([3,2,4],9))

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


print(sortArray2([0,2,1,2,2,0,0,1,2,1,2,0]))
