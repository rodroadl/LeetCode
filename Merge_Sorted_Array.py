''' https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
    Merge Sorted Array
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
    representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
    and the last n elements are set to 0 and should be ignored. nums2 has a length of n.'''

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1) - m):
            nums1.pop()
        for num in nums2:
            nums1.append(num)
        nums1.sort()

def main():
    test = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    test.merge(nums1, m, nums2, n)
    print("after merge", nums1)
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    test.merge(nums1, m, nums2, n)
    print("after merge", nums1)
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    test.merge(nums1, m, nums2, n)
    print("after merge", nums1)

if __name__ == '__main__':
    main()