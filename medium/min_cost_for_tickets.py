class Solution:
    # Bottom Up Table - 
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return self.mincostTicketsMemo(days, costs, 0, {})
        
    def mincostTicketsMemo(self, days, costs, index, cache):
        if index in cache:
            return cache[index]
        
        # Base cases
        if index == None:
            return 0
        
        if index == len(days) - 1:
            return min(costs)
        
        # Consider 1 day option
        day_limit = days[index] + 1
        next_day_index = self.dayLimit(days, index, day_limit)
        one_day_cost = costs[0] + self.mincostTicketsMemo(days, costs, next_day_index, cache)
        
        # Consider 7 day option
        day_limit = days[index] + 7
        next_day_index = self.dayLimit(days, index, day_limit)
        seven_day_cost = costs[1] + self.mincostTicketsMemo(days, costs, next_day_index, cache)
        
        # Consider 30 day option
        day_limit = days[index] + 30
        next_day_index = self.dayLimit(days, index, day_limit)
        thirty_day_cost = costs[2] + self.mincostTicketsMemo(days, costs, next_day_index, cache)
        
        result = min(one_day_cost, seven_day_cost, thirty_day_cost)
        cache[index] = result
        
        return result
    
    def dayLimit(self, days, index, day_limit):
        for i in range(index+1, len(days)):
            if days[i] >= day_limit:
                return i
        
"""
If you are on day 1

1-day pass: 1 + 1 = 2. Covered for days < 2
7-day pass: 1 + 7 = 8. Covered for days < 8
30-day pass: 1 + 30 = 31. Covered for days < 31

"""
