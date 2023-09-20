# find the longest subarray witn sum k

# brute force
# T.C. => O(n^2)
def longestSubarrK(arr,k):

    n= len(arr)

    ans = 0

    for i in range(n):

        sum = 0

        for j in range(i,n):

            sum += arr[j]

            if sum==k:
                ans= max(ans,(j-i+1))
        
    return ans

# better approach
# prefix sum
# O(nlogm)
def LongestsubArrSumK2(arr,k):

    n = len(arr)

    preSumMap = {}

    sum = 0
    maxLen = 0

    for i in range(n):

        sum+=arr[i]

        if sum==k:
            maxLen = max(maxLen,i+1)
        
        rem = sum - k

        if rem in preSumMap:
            length = i - preSumMap[rem]

            maxLen = max(maxLen,length)
        
        if sum not in preSumMap:

            preSumMap[sum] = i
    
    return maxLen

# optimal approach
# sliding window
# T.C. => O(2N)
# Extra Space => O(1)
def LongestsubArrSumK3(arr, k):
    left = 0
    right = 0

    n = len(arr)

    _sum = 0
    maxLen = 0

    while right < n:
        _sum += arr[right]

        while _sum > k:
            _sum -= arr[left]
            left += 1

        if _sum == k:
            maxLen = max(maxLen, right - left + 1)

        right += 1

    return maxLen

        

print(LongestsubArrSumK3([1,2,3,1,1,1,4,2,3],3))
