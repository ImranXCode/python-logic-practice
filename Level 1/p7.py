nums=[1,2,2,3,4,4,5]
output = []
for i in nums:
    found = False
    for j in output:
        if i == j:
            found = True
    if not found:
        output.append(i)
print(output)