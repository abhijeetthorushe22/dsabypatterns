class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        dict = defaultdict(int)
        count = 0
        dict[0]=1
        for num in nums:
            total+=num
            if total-k in dict:
                count+=dict[total - k]
            
            dict[total]+=1

        return count
        