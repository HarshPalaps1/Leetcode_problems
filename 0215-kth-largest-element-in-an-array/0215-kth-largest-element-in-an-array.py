class Solution(object):
    def findKthLargest(self, nums, k):
        s_nums=nums.sort()
        return nums[len(nums)-k]