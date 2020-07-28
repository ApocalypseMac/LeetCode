class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        n = len(path)
        i = 0
        while i < n:
            while i < n and path[i] == '/':
                i += 1
            curr = ""
            while i < n and path[i] != '/':
                curr += path[i]
                i += 1
            if curr == '.' or curr == '':
                continue
            elif curr == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(curr)
        #print(stack)
        return ('/' + '/'.join(stack))