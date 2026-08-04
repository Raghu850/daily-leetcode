class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        length = m + n
        gap = (length // 2) + (length % 2)

        def get(i):
            if i < m:
                return nums1[i]
            return nums2[i - m]

        def set_val(i, val):
            if i < m:
                nums1[i] = val
            else:
                nums2[i - m] = val

        while gap > 0:
            l = 0
            r = l + gap

            while r < length:
                if get(l) > get(r):
                    a = get(l)
                    b = get(r)

                    set_val(l, b)
                    set_val(r, a)

                l += 1
                r += 1

            if gap == 1:
                break

            gap = (gap // 2) + (gap % 2)

        for i in range(n):
            nums1[m + i] = nums2[i]