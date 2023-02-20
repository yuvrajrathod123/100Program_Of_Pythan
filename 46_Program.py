
# program to transpose the matric using for loop

# solution 1

a = [[1,5,8],
     [7,2,3]]

result = [[0,0],
        [0,0],
        [0,0]]   



for i in range(len(a)):
    for j in range(len(a[0])):
        result[j][i]=a[i][j]

for r in result:
    print(r)
