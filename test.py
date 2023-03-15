class Solution:
    def __init__(self, api):
        self.api = api
        print("Press run code to see this in the console!")
        # You can initiate and calculate things here

    def get_buy_day(self):
        """
        Return the day which you buy silver. The first day has number zero.
        This method is called first, and only once.
        
        
        :rtype: int
        """
        # Write your code here
        num_days = self.api.get_num_days()
        min_price = self.api.get_price_on_day(0)
        buy_day = 0
        for i in range(1, num_days):
            price = self.api.get_price_on_day(i)
            if price < min_price:
                min_price = price
                buy_day = i
        return buy_day

    def get_sell_day(self):
        """
        Return the day to sell silver on. This day has to be after (greater
        than) the buy day. The first day has number zero (although this is not
        a valid sell day). This method is called second, and only once.
        
        
        :rtype: int
        """
        # Write your code here
        num_days = self.api.get_num_days()
        max_profit = 0
        buy_day = self.get_buy_day()
        sell_day = buy_day
        for i in range(buy_day + 1, num_days):
            price = self.api.get_price_on_day(i)
            if price - self.api.get_price_on_day(buy_day) > max_profit:
                max_profit = price - self.api.get_price_on_day(buy_day)
                sell_day = i
        if max_profit == 0:
            return buy_day
        return sell_day

    def get_profit(self):
        """
        Return the maximum profit that can be achieved. This method is called
        last, and only once.
        
        
        :rtype: int
        """
        # Write your code here
        buy_day = self.get_buy_day()
        sell_day = self.get_sell_day()
        return self.api.get_price_on_day(sell_day) - self.api.get_price_on_day(buy_day)
