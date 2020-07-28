class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ') # remove space(s) at the end
        if len(s) == 0:
            return 0
        else:
            count = 0
            for i in range(1, len(s) + 1):
                if s[-i] != ' ':
                    count +=1
                else:
                    break
            return count