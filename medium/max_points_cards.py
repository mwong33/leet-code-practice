# O(n) time O(n) space
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Slow naive way:
        # Get the total score (sum of the array)
        # Get the difference = card number - k
        # Difference is the number of cards we have to give up
        # Create a window of size difference and slide it starting from position 0
        """
        total = sum(cardPoints)
        difference = len(cardPoints) - k
        
        if difference == 0:
            return total
        
        # Slide the window
        rolling_max = 0
        for start in range(len(cardPoints) - difference + 1):
            current_total = total - sum(cardPoints[start:start+difference])
            if rolling_max < current_total:
                rolling_max = current_total
        
        return rolling_max
        """
        
        # Faster way:
        # Same as above but create an array with cumulative sums. This will help us speed up the summation process for each sliding window
        
        # Create the cumulative_total array
        cumulative_total_array = [0] * len(cardPoints)
        
        rolling_sum = 0
        for index in range(len(cardPoints)):
            cumulative_total_array[index] = rolling_sum + cardPoints[index]
            rolling_sum = cumulative_total_array[index]
            
        # Determine the maximum number of points by sliding our window
        window_size = len(cardPoints) - k
        rolling_max = 0
        for start in range(len(cardPoints) - window_size + 1):
            window_total = 0
            if start == 0:
                window_total = cumulative_total_array[start + window_size - 1]
            else:
                window_total = cumulative_total_array[start + window_size - 1] - cumulative_total_array[start-1]
                
            potential_max = cumulative_total_array[-1] - window_total
            
            if potential_max > rolling_max:
                rolling_max = potential_max
        
        return rolling_max
