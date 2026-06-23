class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(t[i]) - ord('a')] -= 1
        
        for val in cnt:
            if val != 0:
                return False
        return True