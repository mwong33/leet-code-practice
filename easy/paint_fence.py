class Solution:
    def numWaysNaive(self, n: int, k: int) -> int:
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
