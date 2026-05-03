class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for j in s:
            if st and st[-1] == j:
                st.pop()
            else:
                st+=[j]
        return "".join(st) 

        