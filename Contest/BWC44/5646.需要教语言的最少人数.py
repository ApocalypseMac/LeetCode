class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        ll = [set() for _ in range(n + 1)]
        for i in range(m):
            for l in languages[i]:
                ll[l].add(i + 1)
        f = set()
        for u, v in friendships:
            flag = False
            for i in range(1, n + 1):
                if u in ll[i] and v in ll[i]:
                    flag = True
                    break
            if flag is False:
                f.add(u)
                f.add(v)
        f = list(f)
        #print(f)
        res = m
        for i in range(1, n + 1):
            cnt = 0
            for u in f:
                if u not in ll[i]:
                    cnt += 1
            res = min(res, cnt)
        return res