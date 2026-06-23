class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        l,r = 0,0

        for i in range(len(nums)):
            currnum = nums[i]
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + currnum < 0:
                    l+=1
                elif nums[l] + nums[r] + currnum > 0:
                    r-=1
                else:
                    result.add((currnum, nums[l], nums[r]))
                    l+=1
        return [list(i) for i in result]
