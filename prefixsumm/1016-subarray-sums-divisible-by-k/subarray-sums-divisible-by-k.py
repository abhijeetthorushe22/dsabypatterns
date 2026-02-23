class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixcount = defaultdict(int)
        count = 0
        prefix_sum = 0
        prefixcount[0]=1
        for num in nums:
            prefix_sum+=num
            remainder = prefix_sum % k
            if remainder < 0:
                remainder+=k

            count += prefixcount[remainder]
            prefixcount[remainder] +=1
        return count


        