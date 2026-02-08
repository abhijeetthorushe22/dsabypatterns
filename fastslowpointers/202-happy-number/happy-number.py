class Solution:
    def cal(self,n):
        total = 0
        while n>0:
            digit = n % 10
            total+=digit*digit
            n = n //10
        return total
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        slow = n
        fast = self.cal(n)
        while slow!=fast:
            if fast == 1:
                return True
            slow = self.cal(slow)
            fast = self.cal(fast)
            fast = self.cal(fast)
        return False
        