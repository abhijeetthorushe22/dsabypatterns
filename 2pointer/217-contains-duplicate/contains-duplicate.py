class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = list(set(nums))
        if len(x)==len(nums):
            return False
        else:
            return True
       