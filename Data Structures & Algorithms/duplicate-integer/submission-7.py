class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numList = set()
        for num in nums:
            if num in numList:
                return True
            numList.add(num)
        return False
