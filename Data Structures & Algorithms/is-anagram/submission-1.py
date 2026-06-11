class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        d = {}
        for n in s:
            h[n] = h.get(n, 0) + 1
        for n in t:
            d[n] = d.get(n, 0) + 1
        if d == h:
            return True
        return False