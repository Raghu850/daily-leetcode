class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m=len(matrix),len(matrix[0])
        l,r=0,m-1
        top,bottom=0,n-1
        ans=[]
        while top<=bottom and l<=r:
            for i in range(l,r+1):
                ans.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                ans.append(matrix[i][r])
            r-=1
            if top<=bottom:
                for i in range(r,l-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            if l<=r:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][l])
                l+=1
        return ans