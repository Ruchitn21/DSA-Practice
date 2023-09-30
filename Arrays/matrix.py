# Spiral Traversal of a Matrix
# It's an implementation problem so there is only one solution for this problem

# T.C. => O(N*M)
# Extra Space => O(N*M)
def spiralTraversal(matrix):

    rows = len(matrix)
    columns = len(matrix[0])

    top = 0
    bottom = rows-1
    left = 0
    right = columns-1

    ans = []

    while(left<=right and top<=bottom):

        # 1st left to right traversal
        for i in range(left,right+1):
            ans.append(matrix[top][i])

        top+=1
        # 2nd top to bottom
        for i in range(top,bottom+1):
            ans.append(matrix[i][right])
        
        right-=1
        # 3rd right to left
        if(top<=bottom):
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            
        bottom-=1
        if(left<=right):
        # 4th bottom to top
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])

        return ans

        left+=1
print(spiralTraversal([[1,2,3,4],
                       [5,6,7,8],
                       [9,10,11,12],
                       [13,14,15,16]]))
