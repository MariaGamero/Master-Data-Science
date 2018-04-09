#2.Write a function 'centenario' that will take _name_ , and _year of birth_ as inputs. Check if year of birth is int and cast it to int if not, and print name together with the text explaining when the person is to have 100 years (hint:use isinstance)

def centenario(name, year_of_birth):
    if not isinstance(year_of_birth, int):
        year_of_birth=int(year_of_birth)
    print('%s will reach 100 years in %d' %(name, year_of_birth +100))

centenario ('Dani',1980)
centenario ('Maria','1980')



