class apple():
    color=""
    taste=""
    size=""

kashmiri=apple()
kashmiri.color="chatak lal rang"
kashmiri.taste="sweet"
kashmiri.size="extra-extra large"

ask = input("enter what you want to know about  kashmiri apple: ")

if ask=="color":
    print("the color of the apple is ",kashmiri.color)
elif ask == "tasteTASTE":
    print("the taste of the apple is ",kashmiri.taste)
elif ask == "sizeSIZE":
    print("the size of the apple is ",kashmiri.size)
else:
    print("OUT OF KNOWLEDGE!!!")


# print(dir("")) #to check the methods in the python
