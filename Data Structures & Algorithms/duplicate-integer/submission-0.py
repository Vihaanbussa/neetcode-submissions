class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        for i in range(0, len(nums)):
            print("i ", i)
            for j in range(i+1, len(nums)):
                print("j ", j)
                if nums[i] == nums[j]:
                    return True
        return False
