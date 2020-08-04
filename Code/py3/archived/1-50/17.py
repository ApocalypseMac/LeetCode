class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dic = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        result = []
        n = len(digits)
        def backtrack(s, digit):
            if digit == n:
                result.append(s)
                return
            letters = dic[int(digits[digit])]
            for ch in letters:
                backtrack(s + ch, digit + 1)
            return
        backtrack("", 0)
        return result