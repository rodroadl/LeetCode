''' https://leetcode.com/problems/plus-one/
    You are given a large integer represented as an integer array digits, 
    where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. 
    The large integer does not contain any leading 0's.
    Increment the large integer by one and return the resulting array of digits.'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        adder = 1
        for i in range(len(digits)-1, -1, -1):
            if adder:
                digits[i] = (digits[i] + 1) % 10
                adder = 0
                if digits[i] is 0:
                    adder = 1
        if digits[0] is 0:
            digits.insert(0, 1)
        return digits
            
def main():
    test = Solution()
    print(test.plusOne([1,2,3]))
    print(test.plusOne([4,3,2,1]))
    print(test.plusOne([0]))
    print(test.plusOne([9]))

if __name__ == '__main__':
    main()