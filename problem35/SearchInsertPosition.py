from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        esquerda = 0
        direita = len(nums) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2

            if target == nums[meio]:
                return meio
            elif nums[meio] < target:
                esquerda = meio + 1
            else:
                direita = meio - 1

        return esquerda 


                        

        

a = Solution()

print(a.searchInsert([-1,3,5,6],0))