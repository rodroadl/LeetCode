''' https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    121. Best Time to Buy and Sell Stock
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        largest_total = 0
        curr_total = 0
        min = 10 ** 4
        for i in range(len(prices)):
            curr_total = prices[i] - min
            if curr_total > largest_total:
                largest_total = curr_total
            if prices[i] <= min:
                min = prices[i]
        return largest_total

def main():
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))
            
if __name__ == '__main__':
    main()            
            