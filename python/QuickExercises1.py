
#1. Implement a function that takes as imput three variables, and returns the largues of the three. Do this without using the python max() function!.Make one version without any local variable and another with one local variable.(hint:it might be easier to use edit)

#without local variable

def max_of_three(x,y,z):
    if x>y and x>z:
        print(x)
    if y>x and y>z:
        print(y)
    if z>x and z>y:
        print(z)

max_of_three(3,5,9)
max_of_three(9,35,2)

