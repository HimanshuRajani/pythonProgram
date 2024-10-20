string=input("enter the full string you have:- ")
sub_string=input("enter the part of string you want to find:- ")

# if sub_string in string:
#     print("the sub string is found in the main string")
# else:
#     print("string not found")

def find_substring(string,sub_string):
    index =string.find(sub_string)
    return index

print(find_substring(string,sub_string))

