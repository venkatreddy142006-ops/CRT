'''
#.List
li = [1,2,3,4,5]
res = []
for ele in li:
    res.append(ele*2)
print(res)

# printing even numbers
li = [1,2,3,4,5]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)

li1 = ['a','b','c']
res = " "
for ch in li1:
    res = res + ch + " "
print(res)
print(" ".join(li1))

#1. Pyramid 
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
    
#2. Inverted Pyramid
n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
    # output
    #  * * * * 
    #   * * *
    #    * *
    #     *
    
#3. Diamond
n = int(input())
for i in range(n+1):
    print(" "*(n-i)+"* "*i)
for j in range(n-1,0,-1):
    print(" "*(n-j)+"* "*j)
#output
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
'''
#4. Palindrome Pattren
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()
    