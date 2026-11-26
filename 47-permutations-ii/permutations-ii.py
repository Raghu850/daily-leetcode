class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def next_perm(perm: List[int]) -> List[int]:
            i = n - 2
            while i >= 0 and perm[i] >= perm[i + 1]:
                i -= 1
            if i < 0:
                return perm[::-1]
            j = i + 1
            while j + 1 < n and perm[j + 1] > perm[i]:
                j += 1
            perm[i], perm[j] = perm[j], perm[i]
            perm[i + 1:] = perm[:i:-1]
            return perm
        permutations = [nums]
        current = nums
        while True:
            current = next_perm(current.copy())
            if current == permutations[0]:
                break
            permutations.append(current)
        return permutations