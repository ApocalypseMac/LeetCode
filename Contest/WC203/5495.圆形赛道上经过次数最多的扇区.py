class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        iscycle = False
        start = rounds[0]
        for i in range(1, len(rounds)):
            if rounds[i] <= rounds[i - 1]:
                iscycle = True
                break
        if iscycle:
            a1, a2 = rounds[0], n + 1
            a3, a4 = 1, rounds[-1] + 1
            if a1 < a4:
                return list(range(a1, a4))
            else:
                return list(range(a3, a4)) + list(range(a1, a2))
        else:
            return list(range(rounds[0], rounds[-1] + 1))