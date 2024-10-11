dict = {"name":'himanshu',"age":24,"city":"mh30"}
print(dict["name"])

print("before changing the city",dict["city"])
dict["city"] = "akola"
print(dict["city"])

dict.pop("name")
print(dict)

dict["work"] = "study"
print(dict)
