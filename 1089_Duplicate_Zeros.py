''' https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
    Duplicate Zeors
    Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
    Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.'''
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        length = len(arr)
        while i < length:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 2
            else:
                i += 1
    
def main():
    test = Solution()
    arr = [1,0,2,3,0,4,5,0]
    test.duplicateZeros(arr)
    print(arr)
    arr = [1,2,3]
    test.duplicateZeros(arr)
    print(arr)

if __name__ == '__main__':
    main()