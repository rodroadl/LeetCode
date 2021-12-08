''' https://leetcode.com/problems/climbing-stairs/
    70. Climbing Stairs
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            one_before = 2
            two_before = 1
            for i in range(2, n):
                total = one_before + two_before
                two_before = one_before
                one_before = total
            return total

def main():
    test = Solution()
    print(test.climbStairs(1))
    print(test.climbStairs(2))
    print(test.climbStairs(3))
    print(test.climbStairs(4))
    print(test.climbStairs(38))

if __name__ == "__main__":
    main()

                
        
        