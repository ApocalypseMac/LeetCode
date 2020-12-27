from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(students)
        sw = deque(sandwiches)
        cnt = 0
        while sw and cnt < len(students):
            if st[0] != sw[0]:
                st.append(st[0])
                st.popleft()
                cnt += 1
            else:
                st.popleft()
                sw.popleft()
                cnt = 0
        return len(st)
        