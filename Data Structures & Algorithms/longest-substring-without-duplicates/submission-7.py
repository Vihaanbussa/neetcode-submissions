class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        sets = {}
        maxcounter = 0;
        counter = 0;
        while r < len(s):
            lval = s[l]
            rval = s[r]
            if rval not in sets:
                sets[rval] = r
                r+=1
            else:
                l = max(sets[rval] + 1, l)
                sets[rval] = r
                r+=1
            counter = r-l
            if counter > maxcounter:
                    maxcounter = counter
        return maxcounter

