


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1  # primer espacio libre para escribir únicos

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        print(nums[:k])
        return k

    

print(Solution().removeDuplicates([1,1,2,3,4,5,6,6,7,7,8,9,9]))