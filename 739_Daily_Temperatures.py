''' https://leetcode.com/problems/daily-temperatures/
    739. Daily Temperatures
    Given an array of integers temperatures represents the daily temperatures, 
    return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
    If there is no future day for which this is possible, keep answer[i] == 0 instead.'''

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = [(temperatures[0], 0)]
        temperatures[0] = 1
        i = 1

        while stack and i < len(temperatures):
            
            while stack and temperatures[i] > stack[-1][0]:
                stack.pop()

            if stack and temperatures[i] <= stack[-1][0]:
                for item in stack:
                    temperatures[item[1]] += 1
                
            stack.append((temperatures[i], i))
            temperatures[i] = 1
            i += 1

        for item in stack:
            temperatures[item[1]] = 0

        return temperatures

def main():
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(sol.dailyTemperatures([30,40,50,60]))
    print(sol.dailyTemperatures([30,60,90]))
    print(sol.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))

if __name__ == '__main__':
    main()