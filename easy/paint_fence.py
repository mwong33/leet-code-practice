# O(n) time O(n) space
class SolutionMemo:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0
        
        return self.numWaysMemo({}, n, k)
    
    def numWaysMemo(self, cache, n, k):
        if n == 1:
            return k
        if n == 2:
            return k*k
        
        last = 0
        second_last = 0
        
        if n - 1 not in cache:
            last = self.numWaysMemo(cache, n-1, k)
            cache[n-1] = last
        else:
            last = cache[n-1]
        if n - 2 not in cache:
            second_last = self.numWaysMemo(cache, n-2, k)
            cache[n-2] = second_last
        else:
            second_last = cache[n-2]
            
        return (k-1) * last + (k-1) * second_last

class SolutionNaive:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0
        
        # Keep a 2D Array that holds all of the ways we can paint the fence for 1 post
        # Loop over n posts starting at index = 2
        # See if we can add each color K to the end of each result of our prevous 2D Array
        # Replace the 2D array with our new 2D array at the end of a single loop
        # return the length of the 2D Array when we are done with our entire loop
        
        paint_array = []
        
        # Create our paint_array for post 1
        for i in range(k):
            paint_array.append([i])
                        
        # Create our paint_array for post 2 to n
        for i in range(2, n+1):
            new_paint_array = []
            # Iterate through each previous answer for i - 1 posts
            for j in range(len(paint_array)):
                # Try each paint option for each type of paint
                for paint in range(k):
                    if paint != paint_array[j][-1] or len(paint_array[j]) == 1:
                        new_paint_array.append(paint_array[j] + [paint])
                    elif paint_array[j][-2] != paint_array[j][-1]:
                        new_paint_array.append(paint_array[j] + [paint])
                    elif paint_array[j][-1] == paint_array[j][-2] and paint != paint_array[j][-1]:
                        new_paint_array.append(paint_array[j] + [paint])
            paint_array = new_paint_array
     
        return len(paint_array)
