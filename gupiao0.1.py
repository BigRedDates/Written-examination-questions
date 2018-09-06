'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。


解题思路一（最好）：
1.始终保存最小的买入价格
2.始终保存最大的利润

'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        profit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            if profit<prices[i]-buy:
                profit=prices[i]-buy


        return profit
prices=[17,1]
print(Solution().maxProfit(prices))


