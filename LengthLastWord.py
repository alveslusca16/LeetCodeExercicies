class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = list(map(str, s.strip("[]").split(" ")))
        changed = True
        while changed:
            if words[-1] == "":
                words.pop()
            else:
                return len(words[-1])
        

a = Solution()
print(a.lengthOfLastWord("   fly me   to   the moon  "))