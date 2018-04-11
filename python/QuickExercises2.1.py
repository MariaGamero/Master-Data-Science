
#1. Write a function to calculate the number of words, number of lines, and length of a string the same way as the wc command does in the command line

def mycounter(cadena):
    l=len(cadena)
    w=len(cadena.split())
    ls=len(cadena.splitlines())
    print (l,w,ls)

mycounter("Mi nombre es María \n soy sevillana \n y tengo 35 años")


