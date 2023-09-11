# Find the largest element in an array

# brute force approach
# O(nlogn) approach
def largestElement1(arr):

    return sorted(arr)[-1]

# optimized approach
# O(n) approach
def largestElement2(arr):
    largest= arr[0]

    for i in range(len(arr)):

        if arr[i]>largest:
            largest = arr[i]
    
    return largest

# print(largestElement1([5,2,1,8,4,6,3]))
# print(largestElement2([5,2,1,8,4,6,3]))

# ==================================================================================

# second largest element in an array

# brute force approach
# O(nlogn + n)
def secondLargest1(arr):

    n= len(arr)

    sorted_arr = sorted(arr)
    secondLargest = -1

    largest= arr[n-1]

    for i in range(n-2,-1,-1):
        if arr[i]!=largest:
            secondLargest = arr[i]
            break

    return secondLargest

# optimized approach
# O(N+N) = O(2N)
def secondLargest2(arr):

    n= len(arr)

    largest = -1

    for i in range(n):

        if arr[i]>largest:
            largest= arr[i]
    
    secondLargest = -1

    for i in range(n):

        if arr[i]>secondLargest and arr[i]<largest:

            secondLargest = arr[i]
    
    return secondLargest

# most optimized approach
# O(n)
def secondLargest3(arr):

    n= len(arr)

    largest = arr[0]
    secondLargest = -1

    for i in range(1,n):

        if arr[i]>largest:
            secondLargest = largest
            largest = arr[i]
        
        # elif arr[i]<largest and arr[i]>secondLargest:
        #     secondLargest = arr[i]
    
    return secondLargest

# arr = [5,9,1,2,4,3]

# print(secondLargest3(arr))

# =========================================================================================

# check if the array is sorted
# brute force approach and the only approach

def isSorted(arr):

    n = len(arr)

    ans = True

    for i in range(1,n):

        if arr[i]<arr[i-1]:
            ans = False
            return ans
    
    return ans

# print(isSorted([1,2,5,4,5]))

# ====================================================================================

# remove duplicates in-place from sorted array

# brute force
# O(nlogn) to insert elements into Set and then O(n) to put the elements back to array => O(nlogn + n)
def removeDuplicates1(arr):

    n= len(arr)

    return len(set(arr))

# optimized approach
# O(n)
def removeDuplicates2(arr):

    n = len(arr)

    i = 0
    j =1

    while j<n:
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1
        
        j+=1
    
    return i+1

print(removeDuplicates2([1,2,2,3,3,3,5]))