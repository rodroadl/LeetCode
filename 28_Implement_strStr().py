''' https://leetcode.com/problems/implement-strstr/
    28. Implement strStr()
    Implement strStr().
    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    Clarification:
    What should we return when needle is an empty string? This is a great question to ask during an interview.
    For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

def main():
    test = Solution()
    print(test.strStr("hello", "ll"))
    print(test.strStr("aaaaa", "bba"))
    print(test.strStr("", ""))


if __name__ == '__main__':
    main()