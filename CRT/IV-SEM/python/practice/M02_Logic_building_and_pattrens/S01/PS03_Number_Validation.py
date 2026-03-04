'''
#1) write a pyhton code for the factorial of a number

n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

#2) write a python code check wheather a number is Armstrong or not?
ex: 153-->1,5,3-->(1 ** 3) + (5 ** 3) + (3 ** 3) = 153

n = int(input())
temp = n
sum = 0
while temp > 0:
    rem = temp % 10
    sum += rem ** 3
    temp //= 10
if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")

# 3) write a python code to check whether a number is prime or not?
n = int(input())
if n < 2:   
    print("Not Prime") 

else:
    for i in range(2,n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# 4) print the prime numbers with a range?
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:  
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#5) monotonic of a Array?
def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing
arr = [1, 2, 3, 4, 5]
print(is_monotonic(arr))  # Output: True
arr = [5, 4, 3, 2, 1]
print(is_monotonic(arr))  # Output: True
arr = [1, 2, 2, 3]
print(is_monotonic(arr))  # Output: True
arr = [1, 3, 2]
print(is_monotonic(arr))  # Output: False

#6)given a signed 32-bit integer x, when x is reversed, if the result is out of the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
x = int(input("Enter an integer: "))
sign = 1
if x < 0:
    sign = -1
    x = -x
rev = 0
while x > 0:
    digit = x % 10
    rev = rev * 10 + digit
    x //= 10
rev *= sign
if rev < -2**31 or rev > 2**31 - 1:
    print(0)
else:
    print("Reversed integer:", rev)

#7) ROMAN TO INTEGER
roman = input("Enter a Roman numerical:").upper()
values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
total = 0
prev = 0
for ch in reversed(roman):
    if values[ch] < prev:
        total -= values[ch]
    else:
        total += values[ch]
        prev = values[ch]
print("Integer value:", total)
'''
