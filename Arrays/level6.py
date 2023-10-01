# count subarray sum equals K

# brute force
def countSubarrK(arr,k):

    n = len(arr)

    count = 0

    for i in range(n):

        sumi = 0

        for j in range(i,n):

            sumi+=arr[j]

            if sumi==k:
                count+=1

    return count

# optimal approach using Prefix Sum
from collections import *
def countSubarrK2(arr,k):

    n = len(arr)

    count = 0
    prefixSum = 0

    mp = defaultdict(int)
    mp[0] = 1

    for i in range(n):

        prefixSum+= arr[i]

        remove = prefixSum - k

        count += mp[remove]

        mp[prefixSum] +=1
        
    return count

print(countSubarrK([3,1,2,4],6))
print(countSubarrK2([3,1,2,4],6))