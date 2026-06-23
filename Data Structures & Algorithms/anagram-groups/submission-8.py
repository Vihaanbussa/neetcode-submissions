class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {} # key : [words]

        for s in strs: 
            key = self.create_key(s)
            if key not in groups: 
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())

    def create_key(self, word): 

        letters = [0] * 26

        for c in word: 
            letters[ord(c) - ord("a")] += 1

        return tuple(letters)