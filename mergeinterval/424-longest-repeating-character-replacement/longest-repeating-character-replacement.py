from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        longest = 0
        max_freq = 0
        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]]+=1
            max_freq = max(max_freq, counts[s[r]])
            while r-l+1 - max_freq >k:
                counts[s[l]]-=1

                l+=1
            longest = max(longest,r-l+1)

        return longest
        