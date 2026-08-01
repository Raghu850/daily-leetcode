class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        pos=0
        neg=1
        for i in nums:
            if i>0:
                arr[pos]=i
                pos+=2
            else:
                arr[neg]=i
                neg+=2
        return arr