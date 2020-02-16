a= [1,2,[3,4],[5,6]]
# print([a[-1],a[0],a[1]])
sum = 0
for val in a:
    if type(val) == list():
        for i in val:
            sum = sum + i
    else:
        sum = sum + val
    print(sum)
# print(a.__contains__)
# Close opend file fo.close() 