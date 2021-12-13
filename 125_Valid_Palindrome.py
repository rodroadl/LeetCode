''' https://leetcode.com/problems/valid-palindrome/
    125. Valid Palindrome
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
    it reads the same forward and backward. 
    Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        return new_s == new_s[::-1]

def main():
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
    print(sol.isPalindrome(" "))

if __name__ == '__main__':
    main()