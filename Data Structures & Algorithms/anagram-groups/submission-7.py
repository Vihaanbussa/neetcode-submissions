class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        currseen = [0] * 26
        allword = {}
        index = 0
        finalresult = []
        for i in range(len(strs)):
            for c in strs[i]:
                currseen[ord(c) - ord('a')] += 1
            tuplecs = tuple(currseen)
            if tuplecs not in allword:
                allword[tuplecs] = index
                finalresult.append([strs[i]])
                index += 1
            else:
                 finalresult[allword[tuplecs]].append(strs[i])
            currseen = [0] * 26
        return finalresult
