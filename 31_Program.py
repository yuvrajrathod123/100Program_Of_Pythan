
# program to convert two given list into dictionary

# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']

# def list_to_dict(a,b):
#     dict = {}
#     for i in a:
#         for j in b:
#            dict[i] = j
#            list2.remove(j)
#            break
# print("Dictionary from lists :\n ", dict)

# list_to_dict(list1,list2)

listK = ["Mon", "Tue", "Wed"]
listV = [3, 6, 5]
# Given lists
print("List of K : ", listK)
print("list of V : ", listV)
# Empty dictionary
res = {}
# COnvert to dictionary
for key in listK:
   for value in listV:
      res[key] = value
      listV.remove(value)
      break
print("Dictionary from lists :\n ",res)


print()
print()
print()


listK = ["Mon", "Tue", "Wed"]
listV = [3, 6, 5]
# Given lists
print("List of K : ", listK)
print("list of V : ", listV)
# COnvert to dictionary
res = {listK[i]: listV[i] for i in range(len(listK))}
    
print("Dictionary from lists :\n ",res)