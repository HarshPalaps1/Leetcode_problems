class Solution(object):
    def subsets(self, nums):
        result=[]
        for num in range(2**len(nums)):
            sub=[]
            #print(num)

            for i in range(num):
                
                if(num&(1<<i)):
                    sub.append(nums[i])
            result.append(sub)
        return result

        