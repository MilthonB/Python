from typing import List



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k  = (m+n)-1

        while j != -1:

            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1


        print(nums1)

            



        



Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# Solution().merge(nums1 = [1], m = 1, nums2 = [], n = 0)
# Solution().merge(nums1 = [0], m = 0, nums2 = [1], n = 1)