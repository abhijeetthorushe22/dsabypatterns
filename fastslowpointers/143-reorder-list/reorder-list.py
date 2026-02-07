# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Linked list → array
        sol = []
        curr = head
        while curr:
            sol.append(curr.val)
            curr = curr.next

        # 2. Reverse copy
        b = sol[::-1]

        # 3. Interleave correctly
        c = []
        for i in range(len(sol)//2):
            c.append(sol[i])
            c.append(b[i])

        if len(sol) % 2 != 0:
            c.append(sol[len(sol)//2])

        # 4. Write back into SAME linked list
        curr = head
        for val in c:
            curr.val = val
            curr = curr.next




        

        """
        Do not return anything, modify head in-place instead.
        """
        