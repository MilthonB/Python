from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target):
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
            print(nums[mid])


            if nums[mid] == target:
                return mid
        
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return left




# re = Solution().searchInsert([1,3,5,6], 5)
# re = Solution().searchInsert([1,3,5,6],2)
# re = Solution().searchInsert([1,3,5,6],7)
# re = Solution().searchInsert([1,3,5,6],9)
# re = Solution().searchInsert([1,3,5,6],0)
re = Solution().searchInsert([9],5)

print(re)