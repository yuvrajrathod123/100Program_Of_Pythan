
# python program to remove the punctuations from the string

# punctuation => (), {}, -, _ , ?, "", ! ,%

punc = '''!(){}[]-;:'"\,<>.?/@#$%^&*~_'''

string = input("Enter anthing here:")

empt_string = ""

for i in string:
    if i not in punc:
        empt_string = empt_string + i

print(empt_string)