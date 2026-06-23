class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        currword = {}
        allword = {}
        finalresult = []
        indexcnt = 0
        for wordindex in range(len(strs)):
            for char in strs[wordindex]: # tracks how many times each char is in each word
                if char not in currword:
                    currword[char] = 0
                currword[char] += 1 
            sortcurrword = str((sorted(currword), currword.values())) #sorts the character counts
            if sortcurrword not in allword: #checks if character counts in allwords
                allword[sortcurrword] = indexcnt
                indexcnt+=1
                finalresult.append([strs[wordindex]])
            else:
                finalresult[allword[sortcurrword]].append(strs[wordindex])
            
            print(currword)
            currword.clear()

        
    
        print(allword)
       
            
        return finalresult
