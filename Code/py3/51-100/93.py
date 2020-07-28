class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        result = []
        def backtrack(pos):
            if pos[-1] >= len(s):
                return 
            if len(pos) == 4:
                if s[pos[3]:] == '0':
                    result.append(s[0:pos[1]] + '.' + s[pos[1]:pos[2]] + '.' + s[pos[2]:pos[3]] + '.' + s[pos[3]:])
                elif s[pos[3]] != '0' and 0 < int(s[pos[3]:]) <= 255:
                    result.append(s[0:pos[1]] + '.' + s[pos[1]:pos[2]] + '.' + s[pos[2]:pos[3]] + '.' + s[pos[3]:])
                return
            lo = pos[-1]
            if s[lo] == '0':
                pos.append(lo + 1)
                backtrack(pos)
                pos.pop()
            else:
                for i in range(1, 4):
                    if lo + i >= len(s):
                        break
                    if int(s[lo: lo + i]) > 255:
                        break
                    
                    pos.append(lo + i)
                    backtrack(pos)
                    pos.pop()
            return

                


        backtrack([0])
        return result