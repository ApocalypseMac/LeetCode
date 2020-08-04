class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        res = []
        row = [words[0]]
        length = len(words[0]) # length including necessary space
        lenwd = len(words[0]) # length of words in this row
        numwd = 1 # number of words in this row
        def postprocess(row, lenwd, numwd):
            res = ""
            if numwd > 1:
                numspace = maxWidth - lenwd
                spaces = [numspace // (numwd - 1)] * (numwd - 1)
                for i in range(numspace % (numwd - 1)):
                    spaces[i] += 1
                for i in range(numwd - 1):
                    res += row[i] + ' ' * spaces[i]
                res += row[-1]
            else:
                res = row[0] + ' ' * (maxWidth - lenwd)
            return res

        
        for i in range(1, n):
            l = len(words[i]) + 1
            if l + length > maxWidth:
                res.append(postprocess(row, lenwd, numwd))
                row = [words[i]]
                numwd = 1
                length = len(words[i])
                lenwd = len(words[i])
            else:
                row.append(words[i])
                numwd += 1
                lenwd += l - 1
                length += l
        res.append(' '.join(row) + ' ' * (maxWidth - length)) # last row
        return res


