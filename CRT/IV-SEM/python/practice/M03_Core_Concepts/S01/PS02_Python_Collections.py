#1480. running sum of 1d array
nums = [1,2,3,4]
res = []
s = 0
for ele in nums:
    s = s+ele
    res.append(s)
print(res)
ans = []
for i in range(1,len(nums)+1):
    ans.append(sum(nums[:i]))   
print(ans)

res1 = [sum(nums[:i]) for i in range(1,len(nums)+1)]
print(res1)