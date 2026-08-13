class Solution:
    def mySqrt(self, x: int) -> int:
        esquerda = 0
        direita = x
        
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if meio * meio == x:
                return meio
            elif meio * meio < x:
                esquerda = meio + 1            
            else:
                direita = meio - 1
        
        return direita

a = Solution()
print(a.mySqrt(2147395599))
 

