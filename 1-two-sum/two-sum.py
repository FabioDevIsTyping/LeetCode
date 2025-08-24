class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = {}
        for i,x in enumerate(nums):
            y = target - x 
            if y in pos:
                return [pos[y], i]
            pos[x] = i