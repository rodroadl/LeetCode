''' https://leetcode.com/problems/roman-to-integer/
    13. Roman to Integer
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, 2 is written as II in Roman numeral, just two one's added together. 
    12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. 
    However, the numeral for four is not IIII. Instead, the number four is written as IV.
     Because the one is before the five we subtract it making four. 
     The same principle applies to the number nine, which is written as IX. 
     There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.
    
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        last = ''
        result = 0
        for c in s:
            if c is 'M': 
                result += 1000
                if last is 'C':
                    result -= 200
            elif c is 'D': 
                result += 500
                if last is 'C':
                    result -= 200
            elif c is 'C': 
                result += 100
                if last is 'X':
                    result -= 20
            elif c is 'L': 
                result += 50
                if last is 'X':
                    result -= 20
            elif c is 'X': 
                result += 10
                if last is 'I':
                    result -= 2
            elif c is 'V': 
                result += 5
                if last is 'I':
                    result -= 2
            elif c is 'I':
                result += 1
            last = c
        return result