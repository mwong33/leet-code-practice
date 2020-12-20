import queue
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    # O(n) space O(n) time
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        visit_queue = queue.Queue()
        employee_map = {}
        
        # Add employees to the hash table
        for employee in employees:
            employee_map[employee.id] = employee
        
        visit_queue.put(employee_map[id])
                
        total_value = 0
        
        # Remove items from the queue, add their value to the total and then add subordinates to the queue
        while not visit_queue.empty():
            current_employee = visit_queue.get()
            total_value += current_employee.importance
            
            for employee_id in current_employee.subordinates:
                visit_queue.put(employee_map[employee_id])
                
        return total_value
