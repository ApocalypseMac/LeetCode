from collections import deque
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # old method (failed:"54312", "21345")
        '''
        n = len(s)
        freqs = [0] * 10
        freqt = [0] * 10
        for ch in s:
            freqs[ord(ch)-48] += 1
        for ch in t:
            freqt[ord(ch)-48] += 1
        for i in range(10):
            if freqs[i] != freqt[i]:
                return False
            
        sufsums = [[0] * 10 for _ in range(n+1)]
        sufsumt = [[0] * 10 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            indexs = ord(s[i]) - 48
            indext = ord(t[i]) - 48
            for j in range(10):
                if j < indexs:
                    sufsums[i][j] = sufsums[i+1][j] + 1
                else:
                    sufsums[i][j] = sufsums[i+1][j]
                if j < indext:
                    sufsumt[i][j] = sufsumt[i+1][j] + 1
                else:
                    sufsumt[i][j] = sufsumt[i+1][j]
        #print(sufsums)
        #print(sufsumt)
        greaters = [[] for _ in range(10)]
        greatert = [[] for _ in range(10)]
        for i in range(n):
            indexs = ord(s[i]) - 48
            indext = ord(t[i]) - 48
            gs, gt = sufsums[i][indexs], sufsumt[i][indext]
            greaters[indexs].append(gs)
            greatert[indext].append(gt)
        for i in range(10):
            greaters[i].sort()
            greatert[i].sort()
            k = len(greaters[i])
            for j in range(k):
                if greaters[i][j] > greatert[i][j]:
                    return False
        return True
        '''
        # queue
        n = len(s)
        pos = [deque([]) for _ in range(10)]
        for i in range(n):
            pos[ord(s[i]) - 48].append(i)
        for i in range(n):
            indext = ord(t[i]) - 48
            if len(pos[indext]) == 0:
                return False
            for j in range(indext):
                if len(pos[j]) and pos[j][0] < pos[indext][0]:
                    return False
            pos[indext].popleft()
        return True