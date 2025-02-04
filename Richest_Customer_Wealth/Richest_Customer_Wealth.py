class Solution:
    def maximumWealth(self, accounts: list[list[int]])-> int:
        maximumWealthSofar=0
        for customer in accounts:
            currentCustomerWealth=0
            for bank in customer:
                currentCustomerWealth+=bank
            maximumWealthSofar=max(maximumWealthSofar, currentCustomerWealth)
        return maximumWealthSofar