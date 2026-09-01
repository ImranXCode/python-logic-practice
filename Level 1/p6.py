nums = [4, 8, 15, 16]
target = 15
found = False

for i in nums:
    if i == target:
        found = True

if found:
    print("Found")
else:
    print("Not Found")