class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        stack = []
        if not digits:
            return []
        
        def backtrack(i):
            if i == len(digits):
                res.append("".join(stack))
                return
            
            for c in hashmap[digits[i]]:
                stack.append(c)
                backtrack(i+1)
                stack.pop()
        
        backtrack(0)
        return res

