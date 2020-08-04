class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # sliding window
        if s == "" or words == []:
            return []
        m = len(words)
        n = len(words[0])
        length = len(s)
        if len(s) < m * n:
            return []
        wd = {}
        for word in words:
            if word in wd:
                wd[word] += 1
            else:
                wd[word] = 1
        res = []
        for i in range(n): # start at s[i]
            l, r = i, i
            freq = {} # freq in substring
            while l + m * n  <= length:
                while r + n <= length and r < l + m * n:
                    if s[r: r + n] not in wd: # search start
                        r += n
                        l = r
                        freq = {} # reset freq
                    else:
                        if s[r: r + n] in freq:
                            if freq[s[r: r + n]] < wd[s[r: r + n]]:
                                freq[s[r: r + n]] += 1
                                r += n
                            else:
                                while freq[s[r: r + n]] >= wd[s[r: r + n]]:
                                    freq[s[l: l + n]] -= 1
                                    l += n
                                freq[s[r: r + n]] += 1
                                r += n
                        else:
                            freq[s[r: r + n]] = 1
                            r += n
                    
                if r - l == m * n:
                    res.append(l)
                    freq[s[l: l + n]] -= 1 # move left bound
                l += n
                
        return res

                         

                
                
                