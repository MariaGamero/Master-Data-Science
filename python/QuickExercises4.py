 1/1: import sklearn
 2/1: sc
 2/2: sc.parallelize([1,2,3])
 2/3: Out[2].map(lambda x: x ** 2)
 4/1:

c = "sdfdfs"

kj = "ni me acuerdo de lo que es esto"
 4/2: %whos
 4/3:
def f(x, y, *args, **kwargs):
    return x + y
 4/4: f(1)
 4/5:
x = -1

if x < 0:
    x = x * (-1)
    
def absolute(n):
    if n <= 0: 
        n = n * (-1)
        
    return n

absolute(-3)
 4/6:
def absolute_or_square(n):
    if n <= 0: 
        n = n * (-1)
    else:
        n = n ** 2
    return n
 4/7:
# A esto ya aprenderemos: Me permite plotear mi funcion rapidamente:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline

X = np.linspace(-3, 3, 200)
Y = map(absolute_or_square, X)

plt.plot(X, Y)
 4/8:
# A esto ya aprenderemos: Me permite plotear mi funcion rapidamente:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline

X = np.linspace(-3, 3, 200)
Y = map(absolute_or_square, X)

plt.plot(X, Y)
 4/9:
# A esto ya aprenderemos: Me permite plotear mi funcion rapidamente:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline

X = np.linspace(-3, 3, 200)
Y = map(absolute_or_square, X)

plt.plot(list(X), Y)
4/10:
# A esto ya aprenderemos: Me permite plotear mi funcion rapidamente:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline

X = np.linspace(-3, 3, 200)
Y = map(absolute_or_square, X)
4/11: plt.plot(X, Y)
4/12: plt.plot([1,3,45,2], [1,5,2,6])
4/13: Y
4/14:
# A esto ya aprenderemos: Me permite plotear mi funcion rapidamente:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline

X = np.linspace(-3, 3, 200)
Y = map(absolute_or_square, X)

plt.plot(X, list(Y))
4/15:
# break 

for letter in abc:
    print "un paso del bucle"
    if letter == "b":
        break

    print letter
print "termine"
4/16:
# continue 

for letter in abc:
    print "un paso del bucle"
    if letter == "b":
        continue

    print letter
print "termine"
4/17:
import time

today = "Monday"

while today != "Friday":
    print "ooooh"
    time.sleep(.5) #This is for the loop to not hog all resources
4/18:
while today != "Friday":
    print "ooooh"
    today = "Friday"
4/19:
def main_loop():
    while True:
        check_world_state()
        accept_user_input()
        respond_to_input()
        render_world()
        if game_over:
            break
        time.sleep(0.16666)
4/20:
def f_to_be_implemented():
    pass # TODO
4/21: !cd /home/dani/repos/master-data-science/data/opentraveldata/; ls
4/22: %cd /home/dani/repos/master-data-science/data/opentraveldata/
4/23: %dhist
4/24:
for directory in _dh:
    !ls -l $directory
4/25:
def maximum(a, b, c):
    assert type(a) == int
    assert type(b) == int
    assert type(c) == int
    
    if a > b:
        max_for_now = a
    else: 
        max_for_now = b
        
    if c > max_for_now:
        max_for_now = c
        
    return max_for_now

assert maximum(3,6,10) == 10, "max is not correct"
4/26: maximum(1,2,"x")
4/27:
def is_in_list(value, collection):
    if value in collection:
        return value
    else:
        return False
    
assert is_in_list(2, [1,2,3]) == 2
assert is_in_list(4, [1,2,3]) == False
assert is_in_list(4, []) == False
assert is_in_list("x", "asdaxlkj") == "x"
4/28:
seq = [1,2,3,4,5,6,7,8]

squares = map(lambda n: n ** 2, seq)
squares
4/29:
def centenario(name, year):
    if type(year) != int:
        year = int(year)
    print name + " will be 100 in " + str(year + 100)
    
centenario("Antonio", 1967)
4/30: %quickref
4/31: _ih
4/32:
def in_hist(search_term):
    count = 0
    
    for command in _ih:
        if search_term in command:
            count += 1 
    return count
4/33: in_hist("search")
4/34: _ih[-10:]
4/35:
origin = _dh[0]
%cd $origin
4/36: !curl -s http://www.gutenberg.org/cache/epub/76/pg76.txt > Finn.txt
4/37:
origin = _dh[0]
%cd $origin
4/38: !curl -s http://www.gutenberg.org/cache/epub/76/pg76.txt > Finn.txt
4/39: !head Finn.txt
4/40: help(open)
4/41: myfile = open('Finn.txt')
4/42:
n = 0

for line in myfile:
    print line
    n += 1
    if n == 10:
        break
4/43: myfile
4/44:
n = 0

for line in myfile:
    print (line)
    n += 1
    if n == 10:
        break
 8/1:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')
%matplotlib inline
 8/2: plt.plot([1,2,3], [4,5,7])
 8/3:
X = np.linspace(-np.pi, np.pi, 25, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)
plt.show()
 8/4:
plt.scatter(X, C)
plt.scatter(X, S)
plt.show()
 8/5: np.version.version
 8/6:
a_list = [1, 2.0,3.1,4.2,-1,8.92]
a = np.array(a_list)
a.dtype
 8/7: a.shape
 8/8: a.ndim
 8/9: np.array( [ [1,2], [3,4] ], dtype=complex )
8/10:
a2 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a2)

print(a.shape, a2.shape)
print(a.size,a2.size)
8/11:
print(np.zeros(10))
print(np.ones((2,3)))
print(np.ones_like(a2))
print(np.eye(4))
print(np.empty((2,3,2)))
8/12:
print(np.arange(10))
print(np.arange( 10, 30, 5 ))
print(np.arange( 0, 2 * np.math.pi, 0.3 ))
print(np.linspace( 0, 2 * np.math.pi, 15 ))
8/13:
narray = np.arange(100000)
plist = range(100000)
8/14: import math
8/15:
%%timeit
[math.sqrt(n) for n in plist]
8/16:
%%timeit
np.sqrt(narray)
8/17: np.arange(10000).reshape(100,100)
8/18: help(np.random.randn)
8/19: np.random.randn(10)
8/20: np.random.rand(10)
8/21:
X = np.random.rand(20)
Y = 2.5 * X + 20

plt.plot(X, Y)
plt.scatter(X, Y, c='blue')
plt.show()
8/22:
def sigmoid(array):   
    result = 1 / (1 + np.exp(-array))
    return result

X = np.linspace(-10, 10, 100)
plt.plot(X, sigmoid(X))
plt.show()
8/23:
print(a)
print(a2)
8/24: print(a[0],a2[0])
8/25: a2[1][0]
8/26: a2[1,0]
8/27: a[1:3]
8/28: a2[:]
8/29: a2[:2,:2]
8/30: a2 > 3
8/31:
from scipy.optimize import fmin

fmin(J, [0,0])
8/32:
df4 = pd.DataFrame(np.random.randn(4,3) * 17 + 15, columns=list('bde'), index=list('BMPZ'))
df4
 5/1:
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
from pandas import DataFrame, Series
import requests
 7/1:
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
from pandas import Series, DataFrame
import pandas as pd
np.set_printoptions(precision=4)
 9/1:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')
%matplotlib inline
12/1:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')
%matplotlib inline
12/2:
figure, axeses = plt.subplots(2,2)

X_2 = np.linspace(-50, 200, 200)
Y_2 = 1 / (1 + np.exp(-X_2))

axeses[0,0].plot(X_2, Y_2)
axeses[0,1].scatter(X, Y_randomized)
axeses[0,1].plot(X2, Y2, c='blue')
axeses[1,0].plot(X_2, X_2 ** 2)
axeses[1,1].plot(X2, X2)

figure.set_size_inches(10,6)
axeses[0,0].legend(['Logistic Function'])
12/3: sns.barplot(data=titanic, x='pclass',y='fare', hue='sex', order=[1, 2, 3]);
12/4: import seaborn as sns
10/1:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
11/1:
import requests

resp = requests.get('http://www.elpais.com/')
resp.content[:500]
11/2:
import json 

pos = json.loads(r.content)
pos
11/3:
import pandas as pd

pd.read_json('http://api.open-notify.org/iss-now.json')
11/4:
from IPython.display import IFrame

IFrame('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts', 800, 600)
11/5:
from bs4 import BeautifulSoup

r = requests.get('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts')

page = r.content
page[:1000]
13/1:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
%matplotlib inline
13/2:
from sklearn.datasets import load_digits
data = load_digits()
13/3: print data['DESCR']
14/1: lines = sc.textFile("data/coupon150720.csv")
14/2: lines.first()
14/3: lines.take(5)
14/4: channels = sc.textFile('data/transm150720.csv').map(getChannel)
14/5: channels.take(5)
14/6:
## Exercise for the students
## PAX per channel

def getChannel(l):
    elems = l.split(",")
    tcn = elems[0]
    channel = elems[8]
    return (tcn, channel)
14/7: channels = sc.textFile('data/transm150720.csv').map(getChannel)
14/8: channels.take(5)
14/9: channels.map(lambda x: (x[1], 1)).reduceByKey(lambda x,y: x+y).take(15)
14/10:
## Exercise for the students
## Total revenue per channel
def getTCNAndAmount(l):
    elems  = l.split(",")
    tcn    = elems[0]
    amount = float(elems[6])
    
    return (tcn, amount)
14/11: tcn_rev = lines.map(getTCNAndAmount)
14/12: tcn_rev.take(5)
15/1: %ls data
15/2:
import os

folder = os.path.join('data')
fileName = os.path.join(folder, 'coupon150720.csv')
15/3: fileName
15/4: couponsFile = sc.textFile(fileName)
15/5: couponsFile
15/6: couponsFile.take(5)
16/1:
from pyspark import SparkContext
sc = SparkContext()
16/2: sc
20/1: sc
21/1: a=5
21/2: ipython ./helloworld.py
21/3: print ("hello")
21/4: a=5
21/5: type(a)
21/6: b=4
21/7: type(b)
21/8: dir (a)
21/9: a.numerator
21/10: a.denominator
21/11: isinstance (a,int)
21/12: isinstance (a, float)
21/13: a.denominator
21/14: a.numerator
21/15: a
21/16: hasattr (a,'split)
21/17: hasattr (a,'split)
21/18: hasattr (a,'split')
21/19: c="hello"
21/20: a+c
21/21: a = [1,2,3]
21/22: b=a
21/23: a.ppend(5)
21/24: a.append(5)
21/25: a
21/26: b
21/27: c=5
21/28: d=c
21/29: c=7
21/30: d
21/31: x=-1
21/32:
if x<0:
    print('It\s negative')
elif x==0:
    print ('Equal to zero')
elif 0<x<5:
    print('positive but smaller than 5')
else
21/33:
if x<0:
    print('It\s negative')
elif x==0:
    print ('Equal to zero')
elif 0<x<5:
    print('positive but smaller than 5')
else: 
    print('positive and larguer or equal to 5')
21/34: a=5;b=7
21/35: c=8;d=4
21/36: if a<b or c>d
21/37:
if a<b or c>d:
    print('thats it')
21/38: a
21/39: a=[1,2,3,5]
21/40: for e in a
21/41:
for e in a:
    print (element)
21/42:
for e in a:
    print (e)
21/43: total = 0
21/44:
for e in a:
    total +=a
21/45: a
21/46:
for e in a:
    if value is none
21/47:
for e in a:
    if e is none:
        continue
    total+=e
21/48:
for e in a:
    if e is None:
        continue
    total+=e
21/49: for e in a
21/50:
for e in a:
    print(a)
21/51: a
21/52: a=[1,2,3,4,5]
21/53:
for e in a:
    print(a)
21/54: total = 0
21/55: for e i a:
21/56:
for e in a:
    if e is None:
        continue
    total += e
        print(total)
21/57:
for e in a:
    if e is None:
        continue
    total += e
21/58: total = 0
21/59:
for e in a:
    if e is None:
        continue
    total += e
21/60:
def hola():
    print("holla")
21/61: hola()
21/62:
def hola():
    print("hola")
21/63: hola()
21/64: import math
21/65: math.sqrt(4)
21/66: math.pi
21/67: from math import sqrt
21/68: sqrt(8)
22/1: import test
22/2: test.hello()
23/1: import test
23/2: test.hello-world()
24/1: import test
25/1: import test
25/2: test.hello-world
25/3: import math
25/4: import panda as pd
25/5: def f(x, y, z)
25/6:
def f(x, y, z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
25/7: f(8,4,6)
25/8: f(3,6,9)
25/9: f(8,4,6)
25/10:
def f(x, y=9, z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
25/11:
def f(x, y=9, z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
25/12: f(2,y,5)
25/13:
def f(x, y, z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
25/14: f(4,9,7)
25/15:
def f(x, 9, z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
25/16:
def f(x, y, z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
25/17: y=9
25/18: f(2,8)
25/19: f(2,8,6)
25/20: def centenario(name,year_of_birth)
25/21: def centenario (name,year_of_birth)
25/22:
def centenario (name,year_of_birth):
    if name isinstance:
25/23:
def centenario (name,year_of_birth):
    if year_of birt isinstance:
25/24:
def centenario (name,year_of_birth):
    if year_of birth isinstance:
25/25:
def centenario (name,year_of_birth):
    if year_of birth isinstance=int:
25/26:
def centenario (name,year_of_birth):
    if year_of birth isinstance = int:
25/27:
def f(x, y, z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
25/28:
def centenario(name, birth):
    return isinstance(year,int)
25/29: centenario ("maca","200")
25/30:
def centenario(name, birth):
    return isinstance(birth,int)
25/31: centenario ("maca","200")
25/32:
def centenario(name, birth):
    if not isinstance(birth,int):
        year=int(year)
    return year +100
25/33: centenario ("maca","200")
25/34: centenario("macario",1920)
25/35:
def centenario(name, year):
    if not isinstance(year,int):
        year=int(year)
    print(name,"llega a cien años en ", year+100)
25/36: centenario("María",1920)
25/37:
def centenario(name, year):
    if not isinstance(year,int):
        year=int(year)
    print ("%s llegara a cien años en %d" %(name, str(year+100)))
25/38: centenario("maría",1980)
25/39: centenario("María",1920)git status
26/1: a=3
26/2: type(a)
26/3: a**120
26/4: 1+3j
26/5: type(1+3j)
26/6: r.real
26/7: r=1+3j
26/8: r.real
26/9: r..image
26/10: r.image
26/11: r.imag
26/12: r +5.5
26/13:
s= """ 
oerjoj eo
oewk rr
"""
26/14: s
26/15: print(s)
26/16: s2 = "owejoijeirjij\noekojrej\noeko"
26/17: print(s2)
26/18: s3 = "owejoijeirjij\toekojrej\toeko"
26/19: print(s3)
26/20: print(s)
26/21: s.replace("asd","123")
26/22: s.replace("noe","123")
26/23: s
26/24: s.replace("noe","123")
26/25: s[3]
26/26: s.find("noe")
26/27: s.find("eo")
26/28: s.index("eo")
26/29: name = 'pepe'
26/30: 'hola' +'pepe'
26/31: 'hola' + name
26/32: 'hola ' + name
26/33: a=5
26/34: a<5
26/35: a<7
26/36:
def count(cadena):
    if cadena is not isinstance (str):
        cadena =str(cadena)
    print(len(cadena))
26/37: count ("mjeriejirh")
26/38:
def count(cadena):
    if not isinstance (str):
        cadena =str(cadena)
    print(len(cadena))
26/39: count("owekojri")
26/40:
def count_fx("cadena"):
    if not isinstance (str):
        cadena =str(cadena)
    print(len(cadena))
26/41:
def count_fx(cadena):
    if not isinstance (str):
        cadena =str(cadena)
    print(len(cadena))
26/42:
def count_fx(cadena):
    for chr in cadena:
        cadena.find("\")print(len(cadena))
26/43:
def count_fx(cadena):
    for chr in cadena:
        cadena.find("\")print (len(cadena))
26/44:
def count_fx(cadena):
    for chr in cadena:
        print(len(cadena))
26/45: count_fx("ijeijeir")
26/46:
def count_fx(cadena):
    for chr in cadena:
       if print(len(chr))
26/47:
def count_fx(cadena):
    if cadena.find("\n");
26/48:
def count_fx(cadena):
    if cadena.find("\n")
26/49:
def count_fx(cadena):
    print len(cadena)
26/50:
def count_fx(cadena):
    print (len(cadena))
26/51: count_fx(cadena)
26/52: count_fx("iejrie")
26/53: s="HolaMundo.\n Como estamos hoy ?\n espero que bien"
26/54: len (s)
26/55: s.plit("\n")
26/56: s.split("\n")
26/57: s.splitlines("\n")
26/58: s.splitlines()
26/59: len(s.splitlines())
26/60: len(s.split(" "))
26/61: len(s.split())
26/62:
def count_fx(cadena):
    l= len(cadena)
    w= len(cadena.split(" "))
    ll= len(cadena.splitlines())
    return l,w,ll
26/63: count_fx(s)
26/64: s.find(a)
26/65: s.find("a")
26/66:
def remove_n(cadena,n):
    if n<=len(cadena);
26/67:
def remove_n(cadena,n):
    if len(cadena)==0:
        print("cadena vacia")

    if n<=len(cadena) and n!=0:
        print (cadena[0:n]) + (cadena[n+1:])
26/68: remove_n(s,6)
26/69: remove_n("s",6)
26/70: s
26/71: remove_n(s,6)
26/72:
def remove_n(cadena,n):
    if len(cadena)==0:
        print("cadena vacia")

    else:
        print (cadena[0:n]) + (cadena[n+1:])
26/73: remove_n(s,6)
26/74:
def remove_n(cadena,n):
    if len(cadena)==0:
        return ""
    else:
        return (cadena[:n]) + (cadena[n+1:])
26/75: remove_n(s,4)
26/76: remove_n(s,100)
26/77: !pwd
26/78: !ll -s
26/79: !ls -s
26/80: !ll -a
26/81: !python helloworld.py
26/82: %cd Downloads/
26/83: !pwd
26/84: %cd ..
26/85: %dhist
26/86: _dh
26/87: %who
26/88: %whos
26/89: %who_ls
26/90: !ls
26/91: !ls =a
26/92: a=!ls
26/93: a
26/94: type(a)
26/95: a.l
26/96: type(a.l)
26/97: path
26/98: %cd Data/opentraveldata/
26/99: !ls
26/100: !pwd
26/101: %cd ..
26/102: %cd us_dot/otp/
26/103: !ls
26/104: !ls -s
26/105: !ls -a
26/106: !ls -l
26/107: %cd ..
26/108: %cd traffic/
26/109: !ls -l
26/110: %history -g
26/111: %history
26/112: %hist
26/113: %hist
26/114: %dhist
26/115: !pwd
26/116: !ls -l
26/117: !ls
26/118: _dh
26/119: !ls /home/dsc/Data/opentraveldata/
26/120: p="/home/dsc/Data/opentraveldata/"
26/121: !ls$p
26/122: !ls $p
26/123:
for d in _dh:
    print(d)
26/124:
for d in _dh:
    a=!ls %d
    print(d," ",len(a))
26/125: !pwd
26/126:
for d in _dh:
    a=!ls $d
    print(d," ",len(a))
26/127: %cd ..
26/128: %cd ..
26/129: %cd..
26/130: %cd ..
26/131: !ls -l
26/132: cd Downloads/
26/133: !ls -l
26/134: f=open(finn.txt)
26/135: f=open"(finn.txt")
26/136: f=open("finn.txt")
26/137: f.read()
26/138: f.closed()
26/139: f.read()
26/140: f.read ()
26/141: !pwd
26/142: !ls -l
26/143: f.read()
26/144: f=open("finn.txt", encoding="latin-1")
26/145: f=open("finn.txt",encoding="latin-1")
26/146: f.read()
26/147: a=f.read()
26/148: a.count("\n")
26/149: a.find("\n")
26/150: a.count("of")
26/151: f=open("finn.txt",encoding="latin-1")
26/152: a=f.read()
26/153: f.read()
26/154: f=open("finn.txt",encoding="latin-1")
26/155: f.read()
26/156: a=f.read()
26/157: a.count("Reader")
26/158: f.read()
26/159: f=open("finn.txt",encoding="latin-1")
26/160: a=f.read()
26/161: a.count("Reader")
26/162:
def find_it(file_name,word):
    f4=ope(file_name),encoding="latin-1")
26/163:
def find_it(file_name,word):
    f4=open(file_name,encoding="latin-1")
    content =f4.read().lower()
    return content.count(word).lower())
26/164:
def find_it(file_name,word):
    f4=open(file_name,encoding="latin-1")
    content =f4.read().lower()
    return content.count(word.lower())
26/165: find_it("finn.txt","Reader")
27/1: !pwd
27/2: f=open("/home/dsc/Downloads/finn.txt",encoding="latin-1")
27/3: f.read()
27/4: f-strip()
27/5: f.strip()
27/6: f.read()
27/7: f=open("/home/dsc/Downloads/finn.txt",encoding="latin-1")
27/8: f.read()
27/9: f=open("/home/dsc/Downloads/finn.txt",encoding="latin-1")
27/10: texto=f.read()
27/11: texto.read()
27/12: texto.strip()
27/13: texto.strip(" ")
27/14: texto.splitlines()
27/15: texto.split([])
27/16: texto.split(" ")
27/17: texto.read()
27/18: f.read()
27/19: texto.split(" ")
27/20: texto.splitlines()
27/21: texto.read()
27/22: texto.readlines()
27/23: texto.splitlines()
27/24: lineas=texto.splitlines()
27/25: lineas
27/26: texto
27/27:
for linea in lineas:
    print linea.strip()
27/28:
for linea in lineas:
    print (linea.strip())
27/29:
final =""
for linea in lineas:
    if len(linea.strip()) !=0:
        final=final+"\n"+linea.strip()
27/30: final
27/31: len(lineas)
27/32: len(final.splitlines())
27/33: l=[0,1,2,3]
27/34: l.append(5)
27/35: l
27/36: l.append(l)
27/37: l
27/38: list(l)
27/39: l=[0,1,2,3],[4,5,6]
27/40: l
27/41: l=[[1,2,3][4,5,6]]
27/42: l
27/43: l[0]
27/44: l[1]
27/45: l[2]
27/46: l[-1]
27/47: l[-2]
27/48: l.append("text")
27/49: l=[0,1,2,3]
27/50: l.append("TEXT")
27/51: L
27/52: L
27/53: L
27/54: l
27/55: lineas
27/56: trial in lines
27/57: l
27/58: 4 in l
27/59: 1 in text
27/60: 1 in l
27/61: trial in lineas.plitlines()
27/62: print(l)
27/63: list(l)
27/64: list(lineas)
27/65: him in list(lineas)
27/66: l=[1,2,3,4,5,6,7,8]
27/67: l
27/68: cuadrado=lambda x:l*2
27/69: list(map(cuadrado,a))
27/70: list(map(cuadrado,l))
27/71: cuadrado
27/72: list(cuadrado)
27/73: map(cuadrado,l)
27/74: list(map(cuadrado,l))
27/75: cuadrado=lambda x:l**2
27/76: list(map(cuadrado,l))
27/77: cuadrado=lambda x:l**2
27/78: list(map(cuadrado,l))
27/79: cuadrado=lambda x:l**2
27/80: map(cuadrado,l)
27/81: list(map(cuadrado,l))
27/82: l
27/83: cuadrado
27/84: map(cuadrado,l)
27/85: list(map(cuadrado,l))
27/86: l
27/87: Cuadrado=(lambda x:x**2)
27/88: map(Cuadrado,l)
27/89: list(map(Cuadrado,l))
27/90: names=["Maria","Antonio","Diego","Daniel","Maribel","Eduardo","Irene","Rosa","Jose","Lucia"]
27/91: names
27/92:
def ponMayus(nombre):
    res=""
    for char in nombre:
        if char in ["a","e","i","o","u"]:
            res=res+char.upper()
        else:
            res=res+char.lower()
    return res
27/93: ponMayus(names)
27/94:
def ponMayus(nombre):
    res=""
    for char in nombre:
        if char in "aeiou":
            res+=char.upper()
        else:
            res+=char.lower()
    return res
27/95: ponMayus
27/96: n
27/97: n="maria"
27/98: n
27/99: list(n)
27/100: nl=list(m)
27/101: nl=list(n)
27/102: list(map(lambda char: char.upper() if char in "aeiou" else char.lower(),nl))
27/103: r=list(map(lambda char: char.upper() if char in "aeiou" else char.lower(),nl))
27/104: "".join(r)
27/105: names
27/106: list(names)
27/107: names.split(",")
27/108: list(list(names))
27/109: names.filter(r)
27/110: list((filter(lambda e:e=r,names)))
27/111: list(map((filter(lambda e:e=r,names))))
27/112: list(map(filter(lambda e:e=r,names))))
27/113: list(filter(lambda e:e=r,"María"))
27/114: list(filter(lambda e: e=r,"María"))
27/115: list(filter(lambda e: e="r","María"))
27/116: "a" in "María"
27/117: list(filter(lambda e: e=="r","María"))
27/118: "r" in "María"
27/119: names
27/120: list(filter(lambda e: "r" in e,names))
27/121: for e in [1,2,3]
27/122:
for e in [1,2,3]:
    print(e)
27/123: counter=0
27/124:
for i,ve in enumerate ([1,2,3]):
    print(i,e)
27/125:
for i,v in enumerate ([1,2,3]):
    print(i,e)
27/126:
for i,v in enumerate ([1,2,3]):
    print(i,v)
27/127:
for i,v in enumerate in range(1,5):
    print(i,v)
27/128:
for i,v enumerate in range(1,5):
    print(i,v)
27/129:
for i,v in enumerate ([1,2,3]):
    print(i,v)
27/130: a=["hello","Seville","collection","hi"]
27/131: sorted(a,key=lamda e:len(set(a)),reverse=False)
27/132: sorted(a,key=lambda e:len(set(a)),reverse=False)
27/133: sorted(a,key=lambda e:len(set(a)),reverse=True)
27/134: sorted(a,key=lambda e:len(set(a)),reverse=True)
27/135: set (a)
27/136: sorted(a,key=lambda e:len(set(for e in elements in a)),reverse=True)
27/137: sorted(a,key=lambda e:len(set(for e in a)),reverse=True)
27/138: list(map(lambda e: set(e),a))
27/139: sorted(a,key=lambda e:len(set(e.lower())),reverse=True)
27/140: sorted(a,key=lambda e:len(set(e.lower())),reverse=False)
28/1:
import numpy as np
import pandas as pd
import matloblib.pyplot as plt
28/2: %matplotlib inline
28/3:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
28/4: %matplotlib inline
28/5:
plt.plot([1,2,3],[4,5,6])
plt.show()
28/6:
plt.figure(figsize=(10,10))
plt.plot([1,2,3],[4,5,6])
plt.show()
28/7:
plt.figure(figsize=(5,15))
plt.plot([1,2,3],[4,5,6])
plt.show()
28/8:
plt.figure(figsize=(5,2))
plt.plot([1,2,3],[4,5,6])
plt.show()
28/9:
plt.figure(figsize=(5,2))
plt.scatter([1,2,3],[4,5,6])
plt.show()
28/10: list(x in range (1-20))
28/11: x=[1,2,3,4,5,6,7,8,9,10,11,12,13,15,15,16,17,18,19,20]
28/12: y=list[x**2]
28/13: y=list(map(lambda e: e**2,x)
28/14: y=list(map(lambda e: e**2,x))
28/15: y=list(map(lambda e: e**2,x))
28/16:
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,15,15,16,17,18,19,20]
y=list(map(lambda e: e**2,x))
28/17:
x=list(range(-20,20))
y=list(map(lambda e: e**2,x))
28/18:
plt.figure(figsize=(5,2))
plt.scatter(x,y)
plt.show()
28/19:
plt.figure(figsize=(5,2))
plt.plot(x,y)
plt.show()
28/20: ## Ejercicio
28/21: ## Numpy
28/22: l = list(range(0,20))
28/23: l
28/24: a=np.array(l)
28/25: a
28/26: a.dtype
28/27: a.shape
28/28: np.array([0,1],[1,2])
28/29: np.array([[0,1],[1,2]])
28/30: m=np.array([0,1,2,3])
28/31: m.reshape(2,2)
28/32: list(range(1,10))
28/33: np.arrange(1,10)
28/34: np.arange(1,10)
28/35: np.arange(1,10,0.5)
28/36: np.ones(20)
28/37: np.zeros(20).reshape(10,2)
28/38: np.eye(3)
28/39: X=np.array(x)
28/40: X=np.array(x)
28/41: x=list(range(0,20))
28/42: x
28/43: x=list(range(-20,20))
28/44: x
28/45:

plt.figure(figsize=(5,2))
plt.scatter([1,2,3],[4,5,6])
plt.show()

x=list(range(-20,20))
y=list(map(lambda e: e**2,x))
28/46:
plt.figure(figsize=(5,2))
plt.plot(x,y)
plt.show()
29/1:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
29/2: %matplotlib inline
29/3:
plt.plot([1,2,3],[4,5,6])
plt.show()
29/4:
plt.figure(figsize=(5,2))
plt.plot([1,2,3],[4,5,6])
plt.show()
29/5: ## Ejercicio
29/6:

plt.figure(figsize=(5,2))
plt.scatter([1,2,3],[4,5,6])
plt.show()

x=list(range(-20,20))
y=list(map(lambda e: e**2,x))
29/7:
plt.figure(figsize=(5,2))
plt.plot(x,y)
plt.show()
29/8: l = list(range(0,20))
29/9: l
29/10: a=np.array(l)
29/11: a
29/12: a.dtype
29/13: a.shape
29/14: np.array([[0,1],[1,2]]) #una forma de crear matrices/listas
29/15: m=np.array([0,1,2,3]) #esta forma es más rápida
29/16: m.reshape(2,2)
29/17: list(range(1,10) #una forma de crear
29/18: list(range(1,10)
29/19: list(range(1,10))
29/20: np.arange(1,10) #lo mismo con np
29/21: np.arange(1,10,0.5)
29/22: np.ones(20)
29/23: np.zeros(20).reshape(10,2)
29/24: np.eye(3)
29/25: X
29/26: x
29/27: x**2
29/28: X=np.array(x)
29/29: X
29/30: X**2
29/31:
plt.figure(figsize=(5,2))
plt.plot(X,X**2)
plt.show()
29/32: X%2==0
29/33: mini=np.array([0,1,2,3])
29/34: mini[[True,False]] #otra forma de seleccionar elementos de una lista a través de booleanos
29/35: mini[[mini%2==0] #otra forma de seleccionar elementos de una lista a través de booleanos
29/36: mini[[mini%2==0]] #otra forma de seleccionar elementos de una lista a través de booleanos
29/37: X[X%2==0]
29/38: mini[[True,False]]
29/39:
plist = list(range(100000))
narray=np.arange(1000000)
29/40: import math
29/41:
%%timeit
np.sqrt(narray)
29/42:
%%timeit
[math.sqrt(n) for n in plist]
29/43: X2=X.copy() #para copiar
29/44: X2
29/45: [1,2,3]+[3,4,5]
29/46: np.array[1,2,3] + np.array[3,4,5]
29/47: np.array([1,2,3]) + np.array([3,4,5])
29/48: A= np.array([1,2,3]) + np.array([3,4,5])
29/49:
A= np.array([1,2,3]) + np.array([3,4,5])
A
29/50: np.concatenate([a,[3,4,7]])
29/51: np.concatenate([A,[3,4,7]])
29/52: np.concatenate?
29/53: np.arange(1,5,0.5)
29/54: np.linspace(0,5,100)
30/1: a=5
30/2: type(a)
30/3: printa
30/4: print(a)
30/5: echo "print ('Hello world from my python')">hello_world.py
30/6: echo "print ('Hello world from my python')"> hello_world.py
30/7: echo "print ('Hello world from my python')" > hello_world.py
30/8: %echo "print ('Hello world from my python')" > hello_world.py
30/9: % echo "print ('Hello world from python')" > hello_world.py
32/1: %run hello_world.py
32/2: %iphython hello_world.py
32/3: %phython hello_world.py
32/4: %python hello_world.py
32/5: %ipython hello_world.py
32/6: %run hello_world.py
32/7: cd
33/1: a=5
33/2: type(a)
33/3: isinstance(a)
33/4: isinstance(a,int)
33/5: isinstance(a,(int,float))
33/6: isinstance(a,float)
34/1: x=-1
34/2:
if x<8:
print('it/s negative')
34/3:
if x<8:
    print('it/s negative')
34/4: sequence=[1,2,None,4,None,5]
34/5: total =0
34/6:
for value in sequence:
    if value is None:
        continue
    total*=value
34/7: total
34/8:
for value in sequence:
    if value is None:
        continue
    total+=value
34/9: total
34/10: sequence=[1,2,0,4,6,5,2,11]
34/11: total_until_5=0
34/12:
for value in sequence:
    if value ==5:
        break
    total_until_5+=value
34/13: totaL_until_5
34/14: total_until_5
34/15: x=256
34/16: total = 0
34/17:
while x>0:
    if total>500:
        break
    total+=x
    x=x//2
34/18: x
34/19: total
34/20: def max_three(x,y,z)
34/21:
def max_three(x,y,z):
    if x>x and x>y:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
34/22: max_three(5,6,10)
34/23: max_three(15,6,10)
34/24: max_three(15,6,10)
34/25:
def max_three(x,y,z):
    if x>z and x>y:
        return x
    if y>x and y>z:
        return y
    if z>x and z>y:
        return z
34/26: max_three(14,6,9)
34/27: max_three(14,16,9)
34/28: max_three(14,16,29)
34/29: max_var=x
34/30:
if max_var<b:
    max_var=b
if max_var<c:
    max_var=c
return max_var
34/31: max_var=0
34/32: max_var=x
34/33:
if max_var<b:
    max_var=b
if max_var<c:
    max_var=c
return max_var
34/34:
def centenario(name, year_of_birth):
    if not isinstance(year_of_birth,int):
        year_of_birth=int(year_of_birth)
    print('%s will reach 100 years in %d+100'%(name, year_of_birth))
34/35: centenario ('Maria'. 1980)
34/36: centenario ('Maria',1980)
34/37:
def centenario(name, year_of_birth):
    if not isinstance(year_of_birth,int):
        year_of_birth=int(year_of_birth)
    print('%s will reach 100 years in %d'+100 %(name, year_of_birth))
34/38: centenario ('Maria',1980)
34/39:
def centenario(name, year_of_birth):
    if not isinstance(year_of_birth,int):
        year_of_birth=int(year_of_birth)
    print('%s will reach 100 years in %d')  %(name, year_of_birth+100))
34/40:
def centenario(name, year_of_birth):
    if not isinstance(year_of_birth,int):
        year_of_birth=int(year_of_birth)
    print('%s will reach 100 years in %d' %(name, year_of_birth+100))
34/41: centenario('Dani',1980)
34/42:
def centenario(name, year_of_birth):
    if not isinstance(year_of_birth,int):
        year_of_birth=int(year_of_birth)
    print('%s will reach 100 years in %d' %(name, year_of_birth+100))> Quickexercises1.py
35/1:
def centenario(name, year_of_birth):
    if not isinstance(year_of_birth, int):
        year_of_birth=int(year_of_birth)
    print('%s will reach 100 years in %d' %(name, year_of_birth))
35/2: centenario('Dani',1980)
35/3:
def centenario(name, year_of_birth):
    if not isinstance(year_of_birth, int):
        year_of_birth=int(year_of_birth)
    print('%s will reach 100 years in %d' %(name, year_of_birth+100))
35/4: centenario('Dani',1980)
35/5: centenario('Dani','1980')
36/1: a="Hola Me llamo María \ny tengo 38 años."
36/2: a
36/3: a="Hola Me llamo María /ny tengo 38 años."
36/4: a
36/5: a="Hola Me llamo María /n y tengo 38 años."
36/6: a
36/7: a="Hola Me llamo María \n y tengo 38 años."
36/8: a
36/9:
a="""Hola Me llamo María 
y tengo 38 años."""
36/10: a
36/11:
a="""Hola Me llamo María 
y tengo 38 años."""
36/12: a
36/13: a="Hola Me llamo María y tengo 38 años."
36/14: a
36/15: len(a)
36/16: a.split("/n")
36/17: a.split("\n")
36/18: a="Hola Me llamo María \ny tengo 38 años."
36/19: a
36/20: "Hola Me llamo María \ny tengo 38 años."
36/21: "Hola Me llamo María \n y tengo 38 años."
36/22: Hola Me llamo María \n y tengo 38 años
36/23: a.splitlines()
36/24: l=len(a)
36/25: z="first line \n continues the second\n which might not be seen\n"
36/26: z
36/27: z.splitlines()
36/28: z.split(',')
36/29: a=",".join(a)
36/30: a=",".join(z)
36/31: a="^".join(z)
36/32: z
36/33: "^".join(z)
36/34: ",".join(z)
36/35: z.split()
36/36: len(z.split())
36/37: z.split()
36/38: a.split()
36/39: z.split()
36/40: len(z.split())
36/41: len(z)
36/42: z.splitlines()
36/43: len.(z.splitlines())
36/44: len(z.splitlines())
36/45: z.split()
36/46: z.splitline()
36/47: z.splitlines()
36/48: len(z.splitlines())
36/49:
def myaccounter(cadena):
    l=len(cadena)
    w=len(cadena.split())
    ll=len(cadena.splitlines())
    return l, w, ll
36/50: myccounter(z)
36/51: myaccounter(z)
37/1:
def mycounter(cadena):
    l=len(cadena)
    w=len(cadena.split())
    ls=len(cadena.splitlines())
    return l,w,ls
37/2: mycounter("Me llamo María \n tengo 35 años y \n soy sevillana")
37/3: mycounter[8,8,5,3,3,3,5,555,5,5,5,5,5]
37/4: mycounter([8,8,5,3,3,3,5,555,5,5,5,5,5])
37/5: mycounter("Me llamo María \n tengo 35 años y \n soy sevillana")
38/1: a
38/2: a="Hola mundo"
38/3: a
38/4: a.strip('o')
38/5: a.rstrip('o')
38/6: a.rstrip('a')
38/7: a.rstrip('a')
38/8: a
38/9:
def myfunction(cadena,n):
    if len(cadena)==0:
        print("ya te vale")
    else:
        print(cadena[:n]+cadena[n+1:])
38/10: myfunction ("hola que ase, oejireh wejfriorhioh ",7)
38/11: myfunction ("1,2,3,4,5,6,7,8,9,10",7)
38/12: myfunction ("12345678910",7)
39/1: !pwd
39/2: open("./Downloads/finn.txt"encoding="latin-1")
39/3: open("./Downloads/finn.txt",encoding="latin-1")
39/4: %cd Downloads/
39/5: % ll
39/6: f1=open("finn.txt",encoding"latin-1")
39/7: f1=open("finn.txt", encoding"latin-1")
39/8: f1=open("finn.txt", encoding="latin-1")
40/1: f1=open("finn.txt", encoding="latin-1")
40/2: f1=open("./Downloads/finn.txt", encoding="latin-1")
40/3: f1.read()
40/4: f1.seek(0)
40/5: f1.strip()
40/6: f1=open("./Downloads/finn.txt", encoding="latin-1")
40/7: f2=f1.strip()
40/8: f2=f1.read()
40/9: f2.strip()
40/10: f2.striplines()
40/11: f2.splitlines()
40/12:
for linea in lines:
    print(linea.strip())
40/13:
for linea in f2:
    print(linea.strip())
41/1: %cd Downloads/
41/2: %ll
41/3: f=open("finn.txt",encoding="latin-1")
41/4: f.read()
41/5: f=open("finn.txt",encoding="latin-1")
41/6: f1=f.read()
41/7: f1.strip()
41/8: f1.striplines()
41/9: f1.split()
41/10: f1.splitlines()
41/11: f1.splitlines(",")
41/12: f1.splitlines()
41/13: f1.closed
41/14: f1.closed()
41/15: closed
41/16: closed(f1)
41/17: f1.close()
41/18: f1.splitlines()
41/19: f.close
41/20: f.close()
41/21: closed(f)
41/22: f.closed
41/23: %cd ..
41/24: %cd Data/opentraveldata/
41/25: %ll
41/26: %cd ..
41/27: %cd us_dot/otp/
41/28: %ll
41/29: %pwd
41/30: %cd ..
41/31: %cd ..
41/32: %cd us_dot/traffic/
41/33: %ll
41/34: %d_hist
41/35: _dh
41/36:
for i in _dh:
    (ls -l$i|wc -l)
41/37:
for i in _dh:
    (ls -l$i|wc -l):
41/38:
for i in _dh:
    (ls -l$i|wc -l)
41/39:
for i in _dh:
    (ls -l $i|wc -l)
41/40:
for i in _dh:
    (ls -l $i|wc -l)
41/41: %pwd
41/42: %cd..
41/43: %cd..
41/44: %pwd
41/45: %cd ..
41/46: Cd..
41/47: %cd..
41/48: %pwd
41/49: %cd ..
41/50: %cd ..
41/51: % ls- s
41/52: %ll
41/53: %cd Downloads/
41/54: %cd ..
41/55: f=open("./Downloads/finn.txt", encoding="latin-1")
41/56: lines=[]
41/57:
for line in f:
    lines.append(line)
f.close()
41/58: len(lines)
41/59: %cd Downloads/
41/60: !wc -l finn.txt
41/61: f.splitlines()
41/62: f=open("./Downloads/finn.txt", encoding="latin-1")
41/63: f=open("./Downloads/finn.txt", encoding="latin-1")
41/64: f=open("finn.txt", encoding="latin-1")
41/65: f.splitliness()
41/66: f=open("finn.txt", encoding="latin-1")
41/67: f1=f.read()
41/68: f1.splitlines
41/69: f1.splitlines()
41/70: wc -l f1.splitlines()
41/71: wc -l finn.txt
41/72: !wc -l f1.splitliness()
41/73: !wc -l finn.txt
41/74: lines=[]
41/75: f=open("finn.txt", encoding="latin-1")
41/76: f1=f.read
41/77: f1.strip()
41/78: f1=f.read()
41/79: f1.strip()
41/80: f1.splitlines()
41/81: f2=f1.strip()
41/82: f2.splitlines()
41/83: lineas=f2.splitlines()
41/84:
for linea in lineas:
    print(linea.strip())
41/85: f
41/86: texto=f.read()
41/87: testo.strip()
41/88: texto.strip()
41/89: texto
41/90: f=open("finn.txt,encoding="latin-1")
41/91: f=open("finn.txt",encoding="latin-1")
41/92: texto=f.read()
41/93: texto.strip()
41/94: texto.splitlines()
41/95: texto.strip()
41/96: texto2=texto.strip()
41/97: texto2.splitlines()
41/98: texto2=texto.strip()
41/99: texto.strip()
41/100: texto.splitlines()
41/101: texto.strip()
41/102: lines=[]
41/103:
for linea in lines:
    print(linea.strip())
41/104: len(lines)
41/105: f=open("finn.txt",encoding="latin-1")
41/106: texto=f.read()
41/107: texto.splitlines(texto.strip())
41/108: texto.splitlines()
41/109: lines=[]
41/110:
for line in f:
    lines.append(line):
41/111:
for line in f:
    lines.append(line)
41/112: len(lines)
41/113: f.close()
41/114: len(lines)
41/115: f=open("finn.txt",encoding="latin-1")
41/116: lines=[]
41/117:
for line in f:
    lines.append(line)
41/118: f.close()
41/119: len(lines)
41/120: !wc -l finn.txt
41/121: final=[]
41/122:
for line in lines:
    final.append(line.strip())
41/123: len(final)
41/124: final.splitliness()
41/125:
final = " "
for line in lines:
    if len(line.strip())==0:
        final+="n\"+ linea.split()
41/126: x=list(range(1-9))
41/127: x
41/128: x=list(range(1,9))
41/129: x
41/130: range(1,9)
41/131: list(range(1,9))
41/132: x=list(range(1,9))
41/133: list(map(lambda a:a**2,x)))
41/134: list(map(lambda a:a**2,x))
41/135: names=["María","Daniel","Eduardo","Irene","Joni","Maribel","Lola","Cris"]
41/136:
new_names=[]
for name in names:
    name=" "
for letter in name:
    if letter in "aeiouAEIOU"
41/137:
new_names=[]
for name in names:
    name=" "
for letter in name:
    if letter in "aeiouAEIOU":
        new_name+=letter.upper()
    else:
        new_name+=letter.lower()
new_names.append(new_name)
41/138: names
41/139: new_names=[]
41/140:
for name in names:
    new_name=" #this is empty string
41/141:
for name in names:
    new_name=" "#this is empty string
41/142: new_names
41/143: new_name
41/144: names
41/145: names[10]
41/146: names[5]
41/147:
for name in names:
    print (name)
41/148:
for letter in name:
    if letter in "aeiouAEIOU":
        print letter.capitalize()
41/149:
for letter in name:
    if letter in "aeiouAEIOU":
        print letter.capitalize
41/150:
for letter in name:
    if letter in "aeiouAEIOU":
        print (letter.capitalize)
41/151:
for letter in name:
    if letter in "aeiouAEIOU":
        print (letter.capitalize())
41/152:
for name in names:
    for letter in name:
        if letter in "aeiouAEIOU":
            print (letter.capitalize())
41/153:
for name in names:
    for letter in name:
        if letter in "aeiouAEIOU":
            print (letter.capitalize())
        else:
            print(letter.lower())
42/1:
for name in names:
    for letter in name:
        new_name=""
        if letter in "aeiouAEIOU":
            new_name+=letter.capitalize()
        else:
            new_name+=letter.lower()
    print(new_name)
42/2: names
42/3: names=["Dani","Maria"]
42/4:
for name in names:
    for letter in name:
        new_name=""
        if letter in "aeiouAEIOU":
            new_name+=letter.capitalize()
        else:
            new_name+=letter.lower()
    print(new_name)
42/5:
new_name=""
for name in names:
    for letter in name:
        if letter in "aeiouAEIOU":
            new_name+=letter.capitalize()
        else:
            new_name+=letter.lower()
    print(new_name)
42/6:
for name in names:
    new_name=""
    for letter in name:
        if letter in "aeiouAEIOU":
            new_name+=letter.capitalize()
        else:
            new_name+=letter.lower()
    print(new_name)
42/7:
def select(cadena,n):
    for elements in cadena:
        for char in elements:
            if char ==n:
                print elements
42/8:
def select(cadena,n):
    for elements in cadena:
        for char in elements:
            if char ==n:
                print (elements)
42/9: select(names,a)
42/10: select(names,"a")
42/11: names
42/12:
def select(cadena,n):
    for elements in cadena:
        if n in elements:
            print (elements)
42/13: select(names,"a")
42/14: select(names,"i")
42/15: select(names,"r")
42/16:
def select(cadena,n):
    for elements in cadena:
        if n in elements:
            print list((elements))
42/17:
def select(cadena,n):
    for elements in cadena:
        if n in elements:
            return (elements)
42/18: select(names,"r")
42/19: select(names,"a")
42/20:
def select(cadena,n):
    for elements in cadena:
        if n in elements:
    return elements
42/21:
def select(cadena,n):
    for elements in cadena:
        if n in elements:
     return elements
42/22:
def select(cadena,n):
    for elements in cadena:
        if n in elements:
return elements
42/23:
def select(cadena,n):
    for elements in cadena:
        if n in elements:
    return elements
42/24:
def select(cadena,n):
    new_list=""
    for elements in cadena:
        if n in elements:
            new_list+=elements
    return new_list
42/25: select(names,"a")
42/26:
def select(cadena,n):
    new_list=[]
    for elements in cadena:
        if n in elements:
            new_list+=elements
    return new_list
42/27: select(names,"a")
42/28:
def select(cadena,n):
    new_list=[]
    for elements in cadena:
        if n in elements:
            new_list.appednd(elements)
    return new_list
42/29: select(names,"a")
42/30:
def select(cadena,n):
    new_list=[]
    for elements in cadena:
        if n in elements:
            new_list.append(elements)
    return new_list
42/31: select(names,"a")
42/32: names
42/33: cadena= "Hola me llamo María"
42/34: cadena.split()
42/35: cadena.split()[:-1]
42/36: cadena.split()[::-1]
42/37: .join(cadena.split()[::-1])
42/38: "".join(cadena.split()[::-1])
42/39: " ".join(cadena.split()[::-1])
42/40:
def myreverse(cadena):
    x=cadena.split()
    y=x.reseverse()
    return " ".join(y)
42/41: myreverse(cadena)
42/42: myreverse("Hola me llamo María y tengo 38 añoscadena)
42/43: myreverse("hola me llamo maría y tengo 38 años")
42/44:
def myreverse(cadena):
    x=cadena.split()
    y=x.reverse()
    return " ".join(y)
42/45: myreverse ("hola me llamo maria")
42/46:
def myreverse(cadena):
    return " ".join(cadena.split()[::-1])
42/47: myreverse("hola hola hola me llam María")
43/1: jupiter-notebook
46/1: %dhist
46/2: %_dh
46/3: %history
46/4: %history -g
46/5: %pwd
46/6: %history-g > /home/dsc/Master-Data-Science/python/Quickexercises4.py
   1: %history -g
   2: %history -g > QuickExercises4.py
   3: % ll
   4: %ls
   5: %ls -al
   6: %history -g
   7: %history -g > QuickExercises4.py
   8: %ls
   9: %history -g > QuickExercises4.txt
  10: %ls
  11: %history -g >> QuickExercises4.txt
  12: %ls
  13: %history -g -f QuickExercises4.py
