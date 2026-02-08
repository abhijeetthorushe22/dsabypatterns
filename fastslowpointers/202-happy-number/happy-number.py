class Solution:
    def cal(self,n):
        total = 0
        while n>0:
            digit = n % 10
            total+=digit*digit
            n = n //10
        return total
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:

            n = self.cal(n)
            if n in seen:
                return False
            seen.add(n)
        return True
        