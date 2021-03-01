class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            r = 0
        elif ruleKey == "color":
            r = 1
        else:
            r = 2
        res = 0
        for item in items:
            if item[r] == ruleValue:
                res += 1
        return res