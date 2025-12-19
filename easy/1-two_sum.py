

from ast import List


class Solution:

    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        see = {}
        for index, num in enumerate(nums): 

            need = target - num

           
            if( need in see ) :
                return [index, see[need]]

            see[num] = index

        