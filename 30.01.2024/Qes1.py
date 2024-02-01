 You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
Seen this question in a real interview before?  YesNo
Subscribe to see which companies asked this question.

Related Topics 
ArrayDynamic Programming
Similar Questions 
Maximum SubarrayBest Time to Buy and Sell Stock IIBest Time to Buy and Sell Stock IIIBest Time to Buy and Sell Stock IVBest Time to Buy and Sell Stock with CooldownSum of Beauty in the ArrayMaximum Difference Between Increasing ElementsMaximum Profit From Trading Stocks
Py3	



1
class Solution(object):
2
    def maxProfit(self, prices):
3
        """
4
        :type prices: List[int]
5
        :rtype: int
6
        """
7
        if not prices or len(prices) < 2:
8
            return 0    
9
        max_profit = 0
10
        min_price = prices[0]      
11
        for price in prices[1:]:
12
            min_price = min(min_price, price)
13
            max_profit = max(max_profit, price - min_price)
14
        return max_profit

​



   
