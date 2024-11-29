class Solution(object):
    def longestPalindrome(self, s):
        result=""
        
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                word=s[i:j]
                if word==word[::-1]:
                    if len(result)<len(word):
                        print(result)
                        result=word
                    
            
            
        return result

        