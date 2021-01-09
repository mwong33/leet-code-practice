# O(1) for push, pop, top and O(n) for peekMax and popMax. O(n) space.
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def peekMax(self) -> int:
        return max(self.stack)
        
    def popMax(self) -> int:
        max_value = max(self.stack)   
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] == max_value:
                self.stack.pop(i)
                break
                                
        return max_value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

# O(1) for push, pop, top, peekMax and O(n) for popMax. O(n) space.
class MaxStackImproved:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:        
            self.stack.append((x, x))
        else:
            current_max = self.stack[-1][1]
            self.stack.append((x, max(current_max, x)))
        
    def pop(self) -> int:
        if len(self.stack) == 0:
            return None
                
        return self.stack.pop()[0]

    def top(self) -> int:
        if len(self.stack) == 0:
            return None    
    
        return self.stack[-1][0]

    def peekMax(self) -> int:
        if len(self.stack) == 0:
            return None 
        
        return self.stack[-1][1]
        
    def popMax(self) -> int:
        max_value = self.stack[-1][1]
        
        temp = []
        top = self.stack[-1]
        
        while top[0] != top[1]:
            temp.append(self.stack.pop()[0])
            top = self.stack[-1]
            
        self.stack.pop()
        
        for element in temp[::-1]:
            self.push(element)
                                
        return max_value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
