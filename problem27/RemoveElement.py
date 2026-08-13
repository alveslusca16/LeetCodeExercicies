from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for j in nums:
            if j != val:
                nums[k] = j
                k+= 1
        return k
            




a = Solution()
print(a.removeElement([0,1,2,2,3,0,4,2], 2))
            