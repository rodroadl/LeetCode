''' https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
    Valid Mountain Array
    Given an array of integers arr, return true if and only if it is a valid mountain array.

    Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    '''
class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[0] < arr[1]:
            up = True
        else:
            return False
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            if up and arr[i] < arr[i - 1]:
                up = False
            if not up and arr[i] > arr[i - 1]:
                return False
        return True and not up
    
def main():
    test = Solution()
    print(test.validMountainArray([2,1]))
    print(test.validMountainArray([3,5,5]))
    print(test.validMountainArray([0,3,2,1]))

if __name__ == '__main__':
    main()