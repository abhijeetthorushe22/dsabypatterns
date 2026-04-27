class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total  = sum(nums)
        left, right = 0,0
        for i in range(len(nums)):
            
            right = total-nums[i]-left

            if left == right:
                return i
            left+=nums[i]
        return -1
                