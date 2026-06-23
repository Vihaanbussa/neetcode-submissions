class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        heapq.heapify(nums)
        print(nums)
        currentrun = 1
        longestrun = 0

        count = 0;

        while len(nums) > 1:
            currentval = nums[0]
            heapq.heappop(nums)
            print(nums)
            nextval = nums[0]

            if nextval - currentval == 1:
                currentrun += 1
                print('currentrun = ' + str(currentrun))
            if nextval - currentval >= 2:
                if currentrun > longestrun:
                    longestrun = currentrun
                currentrun = 1

        if currentrun > longestrun:
                longestrun = currentrun
        return longestrun

