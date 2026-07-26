#Minha Resposta
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

num = list(map(int, input().strip("[]").split(",")))
target = int(input())
resp = Solution()

print(resp.twoSum(num,target))


#Resposta esperada - Exercício de complexidade O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vistos = {}

        for i in range(len(nums)):
            complemento = target - nums[i]

            if complemento in vistos:
                return [vistos[complemento], i]

            vistos[nums[i]] = i