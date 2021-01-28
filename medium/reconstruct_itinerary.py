import heapq

class Solution:
    # Heap + Dictionary + stack O(E*logE) O(E) space where E is the number of edges
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights_dict = {}
        for flight in tickets:
            if flight[0] not in flights_dict:
                flights_dict[flight[0]] = [flight[1]]
                heapq.heapify(flights_dict[flight[0]])
            else:
                heapq.heappush(flights_dict[flight[0]], flight[1])
                
        # Start with JFK
        stack = ["JFK"]
        output = []
                
        while len(stack) != 0:
            current_city = stack[-1]
            
            if current_city not in flights_dict or len(flights_dict[current_city]) == 0:
                output.append(stack.pop())
            else:
                stack.append(heapq.heappop(flights_dict[current_city]))
        
        return output[::-1]

"""
1: {"MUC": ["LHR"]}
2: {"MUC": ["LHR"], "JFK": ["MUC"]}
3: {"MUC": ["LHR"], "JFK": ["MUC"], "SFO": ["SJC"]}
4: {"MUC": ["LHR"], "JFK": ["MUC"], "SFO": ["SJC"], "LHR": ["SFO"]}

1: {"JFK": ["SFO"]}
2: {"JFK": ["ATL", "SFO"]}
3: {"JFK": ["ATL", "SFO"], "SFO": ["ATL"]}
4: {"JFK": ["ATL", "SFO"], "SFO": ["ATL"], "ATL": ["JFK"]}
5: {"JFK": ["ATL", "SFO"], "SFO": ["ATL"], "ATL": ["JFK", "SFO"]}

Terminate when either the city is not a key in the dictionary or the heap is empty for that city
"""
