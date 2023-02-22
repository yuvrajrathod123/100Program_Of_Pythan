
# program to multiply the matrices

a = [[1,5,8],
     [4,6,7],
     [7,2,3]]

b = [[1,5,6,1],
     [1,9,1,1], 
     [1,5,6,1]] 

result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]     


for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]

for i in result:
    print(i)


