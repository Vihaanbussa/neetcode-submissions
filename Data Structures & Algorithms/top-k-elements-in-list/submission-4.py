import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        final = []
        if len(nums) == 0:
            return []
        for i in nums:
            if i not in seen:
                seen[i] = 0 #num : cnt
            seen[i] += 1
        print(seen)
        if len(seen.keys()) == 1:
            return list(seen.keys())
        newseen = []
        for key, value in seen.items():
            newseen.append((-value,key))
        heapq.heapify(newseen)
        print(newseen)
        for i in range(k):
            final.append(newseen[0][1])
            heapq.heappop(newseen)
        return final

        
        # if flipfreq[0] * -1 in seen.values():
        #     final.append()
        return []



