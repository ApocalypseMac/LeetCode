class Solution:
    def maximumTime(self, time: str) -> str:
        h1, h2, m1, m2 = time[0], time[1], time[3], time[4]
        if h1 == '?' :
            if h2 != '?' and ord(h2) > ord('3'):
                h1 = '1'
            else:
                h1 = '2'
        if h2 == '?':
            if h1 == '2':
                h2 = '3'
            else:
                h2 = '9'
        if m1 == '?':
            m1 = '5'
        if m2 == '?':
            m2 = '9'
        return h1 + h2 + ':' + m1 + m2