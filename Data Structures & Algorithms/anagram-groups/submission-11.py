class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def createWordIndex(word: str) -> str:

            final = [0] * 26

            for letter in word:
                final[ord(letter) - ord('a')] += 1
            
            return str(final)
    
        seen = {}

        for word in strs:
            if createWordIndex(word) not in seen:
                seen[createWordIndex(word)] = []
            seen[createWordIndex(word)].append(word)
        
        finalList = []
        
        for value in seen.values():
            finalList.append(value)
            
        return finalList

