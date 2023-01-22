print("Hello, World!")

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev_x = int(str(x)[::-1])

        while x > 0 and rev_x > 0:
            if x%10 != rev_x%10:
                return False
            x = x//10
            rev_x = rev_x//10

        return True