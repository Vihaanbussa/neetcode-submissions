class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # lists
            # l = [0, 2, 2, 4]
            # append and pop, access via [1, 2, 3, 4]
        # hashmaps/dictionaries 
            # stores key value paires 
            # d = {k : v, k : v}
            # d[k] = v
            # k in d
        # queues
            # like lists but you pop from the left and then add to the right
        # heaps
        # sets
        # Linked Lists 
        # Trees 
        d = {}
        for i in range (0, len(nums)):
            if nums[i] in d:
                return True
            d[nums[i]] = i
        return False


