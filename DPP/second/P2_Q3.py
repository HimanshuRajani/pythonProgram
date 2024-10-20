def str_len(string):
    count=0
    for char in string:
        count=count+1
    return count

str=input("enter the word : ")
print("the length of word is ",str_len(str)) 
