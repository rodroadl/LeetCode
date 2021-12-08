''' https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
    Check If N and Its Double Exist
    Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
    More formally check if there exists two indices i and j such that :
    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]
    '''
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for num in arr:
            if 2 * num in arr and (num != 0 or arr.count(0) == 2):
                return True
        return False

def main():
    test = Solution()
    print(test.checkIfExist([10, 2, 5, 3]))
    print(test.checkIfExist([7,1,14,11]))
    print(test.checkIfExist([3,1,7,11]))
    print(test.checkIfExist([-2,0,10,-19,4,6,-8]))

if __name__ == '__main__':
    main()