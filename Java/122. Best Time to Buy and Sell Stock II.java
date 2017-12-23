'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) {
            return 0;
        }
        
        int max_profit = 0;
        
        for (int i = 0; i < (prices.length-1); i++) {
            int price = prices[i+1] - prices[i];
            if (price > 0) {
                max_profit+=price;
            }
        }
        return max_profit;
    }
}
