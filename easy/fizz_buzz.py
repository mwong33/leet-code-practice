class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
    fizz_buzz_list = []
    
    for number in range(1,n+1):
      if number%3==0 and number%5==0:
        fizz_buzz_list.append("FizzBuzz")
      elif number%3==0:
        fizz_buzz_list.append("Fizz")
      elif number%5==0:
        fizz_buzz_list.append("Buzz")
      else:
        fizz_buzz_list.append(str(number))
            
    return fizz_buzz_list
