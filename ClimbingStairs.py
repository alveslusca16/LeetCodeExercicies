class Solution:
    def climbStairs(self, n: int) -> int:
        i = 1
        first_term = 1
        second_term = 1
        aux = first_term + second_term
        while i < n:
            first_term = second_term
            second_term = aux
            aux = first_term + second_term
            i += 1

        return second_term




a = Solution()
print(a.climbStairs(45))