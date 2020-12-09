class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        n = len(command)
        for i in range(n):
            if command[i] == ')':
                if i > 0 and command[i-1] == '(':
                    res += 'o'
            elif command[i] == '(':
                continue
            else:
                res += command[i]
        return res