class Solution:
    def isValid(self, s: str) -> bool:
        '''
        while "{}" in s or "()" in s or "[]" in s:
            s = s.replace("{}", "")
            s = s.replace("()", "")
            s = s.replace("[]", "")
        return s == ""
        '''
        # stack
        stack = ['#']
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' and stack.pop() != '(':
                return False
            elif c == ']' and stack.pop() != '[':
                return False
            elif c == '}' and stack.pop() != '{':
                return False
        return stack.pop() == '#'