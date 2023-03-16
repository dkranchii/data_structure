nums = [1,7,3,6,5,6]
s = sum(nums)
leftsum = 0
for i, x in enumerate(nums):
    temp = (s - leftsum - x)
    if leftsum == temp:
        print(i)
    leftsum += x
print(-1)



