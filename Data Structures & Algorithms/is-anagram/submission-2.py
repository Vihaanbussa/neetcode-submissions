class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for c in s:
            if c not in hashS:
                hashS[c] = 1
            else:
               hashS[c] +=1 
        print(hashS)
        for c in t:
            if c not in hashT:
                hashT[c] = 1
            else:
               hashT[c] +=1 
        print(hashT)
        return hashS == hashT
        