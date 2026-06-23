class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        sets = set()
        for r in range(len(s)):
            while s[r] in sets:
                sets.discard(s[l])
                l += 1
            sets.add(s[r])
            res = max(res, r-l + 1)
        return res
