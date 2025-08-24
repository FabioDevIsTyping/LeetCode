class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for i,x in enumerate(nums):
            if x in seen:
                return True
            seen[x]=i
        return False
        