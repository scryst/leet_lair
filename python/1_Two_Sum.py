class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        
        # O(n^2) time
        # for i in range(len(nums)):  
        #     if target-(nums[i]) in nums and nums.index(target-nums[i]) != i:
        #         return [i,nums.index(target-nums[i])]
        
        #O(n) time using dictionary lookup   
        iter_values = {}    
        for index, value in enumerate(nums):
            if target - value in iter_values:
                return iter_values[target - value], index
            iter_values[value] = index
        