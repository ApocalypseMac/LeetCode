class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        rts = [0] + releaseTimes
        max_ = -1
        ch = '#'
        n = len(keysPressed)
        for i in range(n):
            if max_ < rts[i+1] - rts[i] or (max_ == rts[i+1] - rts[i] and ord(keysPressed[i]) > ord(ch)):
                max_ = rts[i+1] - rts[i]
                ch = keysPressed[i]
        return ch
            