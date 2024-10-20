def count_vowel(str):
    vowel = "aeiouAEIOU"
    count = 0
    for i in range (0,len(str)):
        if str[i] in vowel :
            count += 1
    return count

string = input("enter the string:- ")
print(count_vowel(string))