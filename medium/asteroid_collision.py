class Solution:
    # Space O(n) Time O(n)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroid_stack = [asteroids[0]]
        
        index = 1
        
        while index < len(asteroids):                
            current = asteroids[index]
            increment = True
            
            if len(asteroid_stack) == 0:
                asteroid_stack.append(current)
            elif asteroid_stack[len(asteroid_stack) - 1] < 0:
                asteroid_stack.append(current)
            elif asteroid_stack[len(asteroid_stack) - 1] > 0:
                if current > 0:
                    asteroid_stack.append(current)
                else:
                    if abs(current) > asteroid_stack[len(asteroid_stack) - 1]:
                        asteroid_stack.pop()
                        increment = False
                    elif abs(current) == asteroid_stack[len(asteroid_stack) - 1]:
                        asteroid_stack.pop()

            if increment:
                index += 1
            
        return asteroid_stack
