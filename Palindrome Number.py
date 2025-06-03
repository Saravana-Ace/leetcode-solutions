class Solution:
    def isPalindrome(self, x: int) -> bool:
        check = str(x)
        l, r = 0, len(check)-1
        while l <= r:
            if check[l] != check[r]: return False
            l, r = l+1, r-1
        return True