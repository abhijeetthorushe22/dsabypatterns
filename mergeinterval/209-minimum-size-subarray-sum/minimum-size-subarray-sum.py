class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        total = 0
        res = float('inf')
        n = len(nums)-1

        while high <= n:
            total=total+nums[high]

            while total >= target:
                length = high-low+1
                res = min(res,length)

                total = total - nums[low]
                low+=1
            high+=1
        
        return 0 if res == float('inf') else res
        

    

        