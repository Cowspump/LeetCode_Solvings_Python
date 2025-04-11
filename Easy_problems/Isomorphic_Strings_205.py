from collections import Counter


class Solution:
    def isisomorphic(self, s: str, t: str):
        ans = ""

        mp = dict()

        a = [i[-1] for i in Counter(s).items()]
        b = [i[-1] for i in Counter(t).items()]

        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = t[i]

        for i in s:
            ans += mp[i]

        return (ans == t) and (a == b)