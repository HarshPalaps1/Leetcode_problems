class Solution(object):
    def isPalindrome(self, s):
        nlist=[]
        for i in s.lower():
            if i.isalnum() :
                nlist.append(i)
       
           
        return nlist==nlist[::-1]
        