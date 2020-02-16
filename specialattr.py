X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
    print(i)
    for j in range(len(X[0])):
        print(j)
        result[i][j] = X[i][j] + Y[i][j]
        # print(i,j)

# print(len(X))
# print(len(X[0]))
# for r in result:
    # print(r)