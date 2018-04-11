
#2. Write a python program to remove the nth index character from a string. If the input string is empty print warning.

def myfunction(cadena,n):
    if len(cadena)==0:
        print("warning!! Str is empty")
    else:
        print(cadena[:n]+cadena[n+1:])


myfunction("0123456789",4)


