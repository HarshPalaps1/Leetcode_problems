class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        i = n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i<0:
            nums.sort()
            return nums
        
        j = n-1
        while j>=0 and nums[i]>=nums[j]:
            j-=1
        
        nums[i],nums[j] = nums[j],nums[i]
        i += 1
        j = n-1

        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        return nums

            