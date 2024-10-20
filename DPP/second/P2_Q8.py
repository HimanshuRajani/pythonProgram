s1 = input("enter the first word:- ")
s2  = input("enter the second word:- ")

# print(sorted(s1))
if sorted(s1) == sorted(s2):
    print("the words are anagrams")
else:
    print("the words are not anagrams")

