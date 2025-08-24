class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = cnt = 0 
        for num in nums:
            if num == 0:
                res = max(res,cnt)
                cnt = 0
            else:
                cnt +=1
        return max(cnt,res)
        