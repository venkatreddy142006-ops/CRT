'''
#1. Square Star Pattern 

n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

#2. Right Angle Triangle

n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

#3. Inverted Triangle

n = int(input())
for i in range(0,n+1):
    for j in range(n-i):
        print("*",end=" ")
    print()

n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

 #4. Number Triangle
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()

#5. Repeated Number Patterns
n = int(input())
for i in range(1,n+1):
    print(i,end=" ")
    for j in range(i-1):
        print(i,end=" ")
    print()   
    
#6. Alphabet Triangle
n = int(input())
for i in range(1,n+1):
    ch = 65
    for j in range(i):
        print(chr(ch+j),end=" ")
    print()
    '''
#7. Floyd Triangle
n = int(input())
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print()