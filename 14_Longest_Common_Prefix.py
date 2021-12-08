''' https://leetcode.com/problems/longest-common-prefix/
    14. Longest Common Prefix
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".'''

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        result = ''
        ref = strs[0]
        done = False
        i = 0
        j = 0
        while i < len(ref) and not done:
            add = False
            while j < len(strs) and not done:
                if i == len(strs[j]):
                    done = True
                    add = False
                elif ref[i] != strs[j][i]:
                    done = True
                j += 1
                add = True
                
            if not done and add:
                result += ref[i]
                i += 1
                j = 1
        return result

    def test(self):
        print(self.longestCommonPrefix(["flower","flow","flight"]))
        print(self.longestCommonPrefix(["dog","racecar","car"]))
        print(self.longestCommonPrefix(["ab","a"]))
        print(self.longestCommonPrefix(["abab","aba", ""]))
        print(self.longestCommonPrefix(["a"]))

test = Solution()
test.test()