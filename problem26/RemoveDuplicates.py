from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for j in range(i, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


a = Solution()
print(a.removeDuplicates([1,1,2]))