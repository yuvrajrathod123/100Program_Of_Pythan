
# program to transpose the matrics using list comprehension

a = [[1,5,8],
     [7,2,3]]

result = [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]

# print(result)

for r in result:
    print(r)