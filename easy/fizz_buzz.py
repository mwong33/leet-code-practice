class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzzList = []
        
        for number in range(1,n+1):
            if number%3==0 and number%5==0:
                fizzBuzzList.append("FizzBuzz")
            elif number%3==0:
                fizzBuzzList.append("Fizz")
            elif number%5==0:
                fizzBuzzList.append("Buzz")
            else:
                fizzBuzzList.append(str(number))
                
        return fizzBuzzList