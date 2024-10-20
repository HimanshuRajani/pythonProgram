string = "hie i am here i am there i will be everywhere"
replace = "m"
replace_with = "you"

for replace in string:
    new_string = string.replace(replace,replace_with)

print(new_string)