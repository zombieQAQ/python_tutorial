class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        reward = 0
        buy = prices[0]

        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy:
                reward = max(reward, prices[i] - buy)
        return reward
            