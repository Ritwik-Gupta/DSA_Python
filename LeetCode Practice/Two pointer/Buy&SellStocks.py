class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #setting up left pointer and right pointer
        leftPtr, rightPtr = 0, 1
        maxProfit = 0

        while rightPtr < len(prices):
            diff = prices[rightPtr] - prices[leftPtr]
            maxProfit = max(maxProfit, diff)
            #if new lowest point detected
            if diff <= 0:
                leftPtr = rightPtr
            rightPtr += 1
        
        return maxProfit


'''
leetcode link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock

Explanation: In this problem we need to find the indices, which will generate the maximum profit when selling a stock

1. We initialise 2 pointers, the first pointer keeps track of the lowest stock price and the 2nd pointer tracks the highest stock price
2. We iterate trough the loop to find the lowest and highest stock price and return the max profit

'''