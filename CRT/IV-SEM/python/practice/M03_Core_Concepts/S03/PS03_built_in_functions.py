'''
#1. Find Largest Number (Using max()) --> largest value in a list
numbers = [10, 20, 5, 15]
largest = max(numbers)
print("Largest number:", largest) # Output: Largest number: 20

#2 Check Palindrome (Using reversed() and join()) --> check if a string is the same forwards and backwards
word = 'madam'
if word == "".join(reversed(word)):
    print("Palindrome")
else:
    print("Not a Palindrome.") # Output: Palindrome

#3. count even numbers (USing filter())
arr=[10,23,54,85,10,25]
res=list(filter(lambda x:x%2==0,arr))
print(res)
'''
