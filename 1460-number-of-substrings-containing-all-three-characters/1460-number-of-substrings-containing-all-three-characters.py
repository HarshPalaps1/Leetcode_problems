class Solution(object):
    def numberOfSubstrings(self, s):
        map={"a":-1,"b":-1,"c":-1}
        count=0
        for i in range(len(s)):
            map[s[i]]=i
            if(map["a"]!=-1 and map["b"]!=-1 and map["c"]!=-1 ):
                count= count+1 +min(map["a"],map["b"],map["c"])

        return count