class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low = 0
        n = len(fruits)
        freq = {}
        res = -1

        for right in range(n):
            freq[fruits[right]] = freq.get(fruits[right],0)+1

            while len(freq)>2:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]

                low+=1

            res =  max(res,right-low+1)
        return res