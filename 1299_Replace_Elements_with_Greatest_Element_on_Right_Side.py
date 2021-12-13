''' https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
    Replace Elements with Greatest Element on Right Side
    Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
    After doing so, return the array.'''

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i+1:])
        arr[len(arr) - 1] = -1
        return arr

def main():
    test = Solution()
    arr = [17,18,5,4,6,1]
    print(test.replaceElements(arr))
    arr = [400]
    print(test.replaceElements(arr))

if __name__ == '__main__':
    main()