class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        
        stack = []
        
        for i in s:
            if i in parentheses:
                stack.append(i)
            elif not stack:
                return False
            else:
                if parentheses[stack.pop()] != i:
                    return False
        return True if not stack else False

foo = Solution()
print(foo.isValid("()"))
print(foo.isValid("()[]{}"))
print(foo.isValid("(]"))
print(foo.isValid("([)]"))
print(foo.isValid("{[]}"))
