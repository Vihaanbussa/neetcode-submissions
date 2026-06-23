class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for num in range(len(numbers)):
            if numbers[num] in seen.keys():
                return [1+ seen[numbers[num]], 1+ num]
            if target-numbers[num] not in seen.keys():
                seen[target-numbers[num]] = num;
        