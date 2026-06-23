class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = self.createWordMap(s1)
        print(s1Map)
        for r in range(len(s1) - 1, len(s2)):
            l = r - len(s1) + 1
            print('r: ' + str(r))
            print('l: ' + str(l))
            print(s2[l:r+1])
            print(self.createWordMap(s2[l:r+1]))
            if s1Map == self.createWordMap(s2[l:r+1]):
                return True
        return False


    def createWordMap(self, word: str) -> list:
        wordMap = [0] * 26
        for char in word:
            wordMap[ord(char) - ord('a')] += 1
        return wordMap
