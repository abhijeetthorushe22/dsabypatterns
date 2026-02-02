from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right  = left = 0
        majority = maxlen = 0
        counts = defaultdict(int)
        while right < len(s):
            counts[s[right]]+=1
            majority = max(majority,counts[s[right]])
            while majority+k < right-left+1:
                counts[s[left]]-=1
                left+=1

        
            maxlen = max(maxlen,right-left+1)
            right+=1
        
        return maxlen
        