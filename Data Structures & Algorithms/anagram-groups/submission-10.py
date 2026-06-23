class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        allword = {}
        index = 0
        for i in range(len(strs)):
            currseen = [0] * 26
            for c in strs[i]:
                currseen[ord(c) - ord('a')] += 1
            tuplecs = tuple(currseen)
            if tuplecs not in allword:
                allword[tuplecs] = []
            allword[tuplecs].append(strs[i])
        return list(allword.values())
