
# program to merge the two dictionaries


# merge using union operator
dic1 = {"Yuvraj":89, "manish":90, "niraj":95}
dic2 = {"siddesh":74, "niraj":90}

print(dic1 | dic2)

# merge using ** operator
dic1 = {"Yuvraj":89, "niraj":95}
dic2 = {"siddesh":74, "niraj":90}

print({**dic1,**dic2})
print({**dic2,**dic1})

# using copy() and update()

dic1 = {"Yuvraj":89, "niraj":95}
dic2 = {"siddesh":74, "niraj":90}

dic3= dic2.copy()
dic3.update(dic1)
print(dic3)

