def count_vowel(string):
    vowel = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowel:
            count += 1
    return count

print("Total number of vowels in Hello  World: ", count_vowel("Hello World"))
