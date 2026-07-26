#Minha solução
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        lista = []
        lista = list(map(int, str(x)))

        lista_reverse = list(reversed(lista))

        if lista == lista_reverse:
            return True
        
        return False        

s = Solution()
s.isPalindrome(10)


#Solução esperada
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertido = 0

        while x > revertido:
            ultimo = x % 10
            revertido = revertido * 10 + ultimo
            x //= 10

        return x == revertido or x == revertido // 10