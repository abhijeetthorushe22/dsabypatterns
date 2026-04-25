class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        sumwithskip = sumwithoutskip = res = arr[0]
        for num in arr[1:]:
            if sumwithskip < 0:
                sumwithskip = 0
            if num > 0:
                sumwithskip+=num
            else:
                sumwithskip = max(sumwithskip+num,sumwithoutskip)
            
            if sumwithoutskip < 0:
                sumwithoutskip = 0
            
            sumwithoutskip+=num

            res = max(sumwithoutskip,sumwithskip,res)
        return res
            


        