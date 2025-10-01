class Solution(object):
    def rotate(self, nums, k):
        rotated = [0] * len(nums)
        for i in range(len(nums)):
            rotated[(i+k)%len(nums)]=nums[i]
        for i in range(len(nums)):
            nums[i] = rotated[i]
        
        