class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i in range(len(nums)):
            newval = target - nums[i]
            if newval in seen:
                return [seen[newval], i]
            
            seen[nums[i]] = i #key = num, val = index




    # basically do target - nums[i] or smth and check if its in the list