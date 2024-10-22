class Solution(object):
    def maxSubArray(self, nums):
        Max = nums[0]
        Sum = 0
        
        for n in nums:
            if Sum < 0:
                Sum = 0
            Sum += n
            Max = max(Max, Sum)
            
        return Max

                

        