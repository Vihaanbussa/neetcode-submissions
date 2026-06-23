class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = [[] for i in range(len(nums))]
        seen = {}
        final = []
        print(len(cnts))
        
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 0
            seen[nums[i]] += 1
        for key, value in seen.items():
            print(key, value)
            cnts[value - 1].append(key)
        for i in range(len(cnts) - 1, -1, -1):
            if len(final) == k:
                break
            for n in cnts[i]:
                final.append(n)

        print(final)

        print(cnts)
        return final