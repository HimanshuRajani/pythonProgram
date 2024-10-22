pi = 3.1416

def circle_area(radius):
    return pi * radius ** 2

rad=int(input("enter the radius of circle:- "))
print("Area of Circle is :-",format(circle_area(rad),".2f"),"unit sq")
