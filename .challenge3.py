class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=''.join(c for c in s if c.isalnum())
        if newstr.lower() == newstr[::-1].lower():
            return True
        else:
            return False

obj=Solution()
print(obj.isPalindrome("a."))