s1 = "hello!! my name is ram"
def capi(sent):
    words = sent.split()

    capitalised = [word.capitalize() for  word in words]

    return " ".join(capitalised)

print(capi(s1))