class Solution:
    def isValid(self, s: str) -> bool:
        self.parentheses = {"}":"{", "]":"[",")":"("}
        self.pile = []
        for c in s:
  
            if c in "({[":
                self.pile.append(c)
            elif self.pile and self.pile[-1] == self.parentheses[c]:
                self.pile.pop()
            else:
                return False
  
        return not self.pile
    
sol = Solution()
print(sol.isValid("(g)"))