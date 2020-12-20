class Solution:
    def reformatNumber(self, number: str) -> str:
        temp = ""
        for ch in number:
            if ch.isdigit():
                temp += ch
        #print(temp)
        n = len(temp)
        res = ""
        i = 0
        while n - i > 4:
            res += temp[i:i+3]
            i += 3
            res += '-'
        if n - i == 4:
            res += temp[i:i+2] + '-' + temp[i+2:] + '-'
        else:
            res += temp[i:] + '-'
        return res[:-1]