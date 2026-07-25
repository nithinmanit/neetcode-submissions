class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        l = []
        for i in strs:
            s = [0] * 26
            for j in i:
                s[ord(j)-ord('a')] += 1
            key = tuple(s)
            if key not in h:
                h[key] = []
            h[key].append(i)
        return list(h.values())