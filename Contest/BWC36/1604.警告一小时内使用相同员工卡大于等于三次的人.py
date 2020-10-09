class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyTime)
        times = dict()
        for i in range(n):
            time = 60 * int(keyTime[i][:2]) + int(keyTime[i][3:])
            name = keyName[i]
            if name in times:
                times[name].append(time)
            else:
                times[name] = [time]
        print(times)
        res = []
        for name in times:
            t = times[name]
            t.sort()
            for i in range(len(t) - 2):
                if t[i+2] - t[i] <= 60:
                    res.append(name)
                    break
        res.sort()
        return res
        