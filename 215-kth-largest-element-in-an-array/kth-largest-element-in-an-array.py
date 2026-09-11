class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        # Choose a pivot element from nums
        pivot = random.choice(nums)

        left, right, equal = [], [], []
        for num in nums:
            if num > pivot:
                right.append(num)   # greater than pivot
            elif num < pivot:
                left.append(num)    # smaller than pivot
            else:
                equal.append(num)   # equal to pivot

        # Number of elements greater than pivot
        count_right = len(right)

        # If kth largest lies in right
        if k <= count_right:
            return self.findKthLargest(right, k)

        # If kth largest is in pivot group
        elif k <= count_right + len(equal):
            return pivot

        # Else, it lies in left
        else:
            # Adjust k because we skip right+equal elements
            return self.findKthLargest(left, k - count_right - len(equal))

        