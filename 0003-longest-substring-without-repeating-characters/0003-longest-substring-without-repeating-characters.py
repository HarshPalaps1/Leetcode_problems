class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len=0
        
        for i in range(len(s)):
            sub=""
            for j in range(i,len(s)):
                #print(s[i:j])
                if s[j] in sub:
                    break
                sub+=s[j]
                max_len=max(len(sub),max_len)

        return max_len
     

        