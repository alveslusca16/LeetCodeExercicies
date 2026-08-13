class Solution:
    def addBinary(self, a: str, b: str) -> str:
        f_binary = a.zfill(max(len(a), len(b)))
        s_binary = b.zfill(max(len(a), len(b)))
        carry = 0
        resp = []
         
        for i in range(len(s_binary)-1, -1, -1):
            sum = int(s_binary[i]) + int(f_binary[i]) + carry
            if sum == 0:
                resp.append('0')
                carry = 0
            elif sum == 1:
                resp.append('1')
                carry = 0
            elif sum == 2:
                resp.append('0')
                carry = 1
            elif sum == 3:
                resp.append('1')
                carry = 1
                
        if carry:
            resp.append('1')

        resp.reverse()

        return "".join(resp)

a = Solution()

print(a.addBinary("11","1"))