from typing import List


def Collatz_Sequence(n: int)-> List:
   if n % 2 == 0:
       return [n] + Collatz_Sequence(n//2)
   elif n % 2 == 1 and n != 1:
       return [n] + Collatz_Sequence(3*n + 1)
   else:       return [n]
if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))