def fizz_buzz(n):
     if type(n) == int:
         if n % 3 == 0 and n % 5 != 0:
             return 'Fizz'
         elif n % 3 != 0 and n % 5 == 0:
             return 'Buzz'
         elif n % 3 == 0 and n % 5 == 0:
             return 'FizzBuzz'
         else:
             return n
     else:
         return "Incorrect input"
