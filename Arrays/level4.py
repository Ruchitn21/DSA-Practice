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
