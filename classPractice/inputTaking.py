class first():
    name=""
    age=""
    city=""

first.name=input("enter the name of user:- ")
first.age=input("enter the user age :- ")
first.city=input("enter the city where the user leave:- ")

print("name:-",first.name,"|| age :-",first.age,"|| city:-",first.city)


class second():
    name=""
    dob=""
    gender=""
    def  __init__(self,name,dob,gender):
        self.name=name
        self.dob=dob
        self.gendr=gender

mine=second("sakshi","14-Aug-2001","female")

print(mine.name,mine.dob,mine.gender)

