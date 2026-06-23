class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        final = []
        zcount = 0;
        ztotal = 1;
        for num in nums:
            if num == 0:
                zcount += 1
            else:
                ztotal *= num
            total *= num
        for num in nums:
            if zcount != 1:
                if num == 0:
                    final.append(int(total));
                else:
                    final.append(int(total/num));
            else:
                if num == 0:
                    final.append(ztotal)
                else:
                    final.append(0)

        return final

