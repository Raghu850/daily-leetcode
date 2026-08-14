class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        a=len(matrix)
        b=len(matrix[0])
        high=a*b-1
        while low<=high:
            mid=(low+high)//2
            if matrix[mid//b][mid%b]==target:
                return True
            elif matrix[mid//b][mid%b]<target:
                low=mid+1
            else:
                high=mid-1
        else:
            return False