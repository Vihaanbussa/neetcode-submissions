class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = ''
        for c in s:
            if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9')):
                lowerS = lowerS + c
        lowerS = lowerS.lower()
        print(lowerS)
        for i in range(len(lowerS)):
            if lowerS[i] != lowerS[-i - 1]:
                return False
        return True