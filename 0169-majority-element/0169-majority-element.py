class Solution(object):
    def majorityElement(self, nums):
        count={}
        for i in nums:
            if i in count:
                count[i]=count[i]+1
            else:
                count[i]=1
        key=list(count.keys())
        value=list(count.values())

        return key[value.index(max(value))]

        