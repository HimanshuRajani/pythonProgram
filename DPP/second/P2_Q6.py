string = "hie i am here i am there i will be everywhere"
replace ='m'
replace_with = "you"

# for replace in string:
#     new_string = string.replace(replace,replace_with)

# print(new_string)
def replace_word(string, replace, replace_with):
    new_string = string.replace(replace, replace_with)
    print (new_string)

replace_word(string, replace, replace_with)
