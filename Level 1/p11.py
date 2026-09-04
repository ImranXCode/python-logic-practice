nums=[10,5,8,20,3]
largest=0
second_largest=0
for i in nums:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest:
        second_largest=i
print(second_largest)