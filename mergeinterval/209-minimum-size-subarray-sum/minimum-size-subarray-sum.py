class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        res= float('inf')
        total = 0
        n = len(nums)
        while high<n:
            total=total+nums[high]

            while total>=target:
                res = min(res,high-low+1)
                total = total-nums[low]
                low+=1
            high+=1
        
        return res if res!=float('inf') else 0
        