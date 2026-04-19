class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlen = -1
        seen = set()
        if s is "":
            return 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                maxlen = max(maxlen,right-left+1)
               
              
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
                seen.add(s[right])
            
            
        return maxlen