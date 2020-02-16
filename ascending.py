numb = int(input('Enter number of elements:'))
list_numb = []
for i in range (1,numb+1):
    list_numb.append(int(input("enter {} number:".format(i))))
print('before sorting', list_numb)

swapped = True

while swapped:
    swapped = False
    for i in range(len(list_numb)-1):
        # print(i, list_numb)
        if list_numb[i] > list_numb[i+1]:
            list_numb[i], list_numb[i+1] = list_numb[i+1], list_numb[i]
            swapped = True
print('after sorting', list_numb)