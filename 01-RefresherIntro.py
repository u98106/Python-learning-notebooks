
# coding: utf-8

# # Introduction to Python

# ### What and why

#   - interpreted (not compiled)
#   - object-oriented
#   - high-level
#   - dynamic semantics (aka execution semantics)
#   - fully dynamic typing
#   - dynamic binding
# 
# 
#   - quick development
#   - simple, readable, easy to learn syntax
#   - general purpose
#   - low program maintenance cost
#   - modularity and code reuse
#   - no licensing costs
#   - extensive standard library, "batteries included"
#   - imperative and functional programming
#   - automatic memory management (garbage-collected)

# ### History, versioning
# 
# * Around 25 years old
# * Versioning:
#     * 2 parallel version streams
#     * 2.x is fully-backward compatible
#     * 3.x fixes some design, performance flaws
#     * ... but breaks backward-compatibility
# 
# 
# * **We'll be using 2.7.10+ for the training**

# In[2]:

import sys
print sys.version


# #### Expressions

# In[2]:

3 + 5
3 + (5*4)
3 ** 2
'Hello' + 'World'


# In[3]:

"Jog's Label"


# #### Variables

# In[3]:

a = 4 << 3
b = a * 4.5
c = (a+b)/2.5
a = "Hello World"


# In[8]:

type(1L)


# In[5]:

a+1


# In[8]:

2 + int('123') 


# In[10]:

type(5.2)


# * Variables are dynamically typed (No explicit typing)
# * Variables are just names for an object. Not tied to a memory location like in C

# #### Types and methods

# In[9]:

type(4)


# In[10]:

type('hi')


# In[11]:

type(str)


# In[12]:

type(type)


# In[ ]:

type(object)


# 

# In[ ]:




# In[ ]:




# #### Numbers

# In[11]:

a = 3              # Integer
b = 4.5            # Floating point
c = 517288833333L  # Long integer (arbitrary precision)
d = 4 + 3j         # Complex (imaginary) number
e = 5 - 1j


# In[13]:

c = 1L
c
type(c)


# In[ ]:

i = 80981
big = 809830983409897098734
i, big


# In[ ]:

type(big)


# In[ ]:

d + e


# In[ ]:

print int


# In[ ]:




# In[13]:

from IPython.core.display import HTML
css = open('table.css').read()
HTML("<style>{}</style>".format(css))


# In[14]:

from methods import methods


# In[ ]:




# #### Strings

# In[17]:

a = 'Hello'
b = u"World"
c = "Bob said \"hey there.\""  # A mix of both
d = u'''A tr∆∆¬…˚…¬˚∆iple quoted string
can span multiple lines
like this'''
e = """Also works for double quotes"""
f = r'^hello.*$'   # raw string
g = unicode(e)


# In[18]:

print g
print e
type(g)


# In[ ]:




# In[19]:

dir(str)


# In[20]:

help(str.strip)


# In[22]:

s = '     ... hi...    '
r = s.strip(' .\t\n')
r


# In[24]:

name = 'Mr 55'
name.isalpha()    # 'method' of the str class


# In[25]:

len(name)         # (global) function


# In[29]:

help(''.split)


# In[21]:

help(str.strip)  


# In[26]:

help(str.split)


# In[ ]:




# In[ ]:




# In[27]:

names = '   a,b,c,d,e   '
names = names.strip()
lnames = names.split(',')
lnames
type(lnames)


# In[28]:

lnames


# In[32]:

nums = [1,2,3,4]
collect = [1,2,'a',10.123, [1,2,3]]
collect


# In[36]:

empty = []
nums + collect


# In[38]:

dir(nums)


# In[52]:

nums.extend([2,3,4,5])
nums


# In[54]:

nums.remove(2)
nums


# In[56]:

nums.insert(2,3)
nums


# In[51]:

a = 1
nums = ['a',2,3,4]
del a
nums


# In[63]:

nums[-1]


# In[65]:

nums[2:4+1]


# In[71]:

nums += [1,2,3,4]


# In[72]:

for elem in nums:
    el2 = elem*elem
    print el2


# In[ ]:

nums = [1,2,3,4]


# In[73]:

nums


# In[ ]:

21%2 == 1


# In[32]:

one = 1
if one > 1:
    print 'Greater'
    print 'xxx'
elif:
        pass  
        print 'Lesser or equal'
        
        
        
def f():
    pass

def g(a , b , c):
    f()


# In[35]:

i = 0
while i<10:
    i += 1
    print 'The value is %d' % i
print 'done'


# In[ ]:




# In[ ]:




# In[ ]:




# In[37]:

'hi'*3


# In[38]:

'-'*40


# #### Lists

# In[36]:

a = [2, 3, 4, 5 ,6, 7]               # A list of integers
b = [2, 7, 3.5, "Hello"]    # A mixed list
c = []                      # An empty list
d = [2, [a,b]]              # A list containing a list
e = a + b                   # Join two lists


# In[51]:

e = e+[1,2,3]


# In[52]:

e[len(e)-1]
e[-1] 


# * slices
# * len
# * range
# * other methods

# In[53]:

e[1:-2+1] 


# In[ ]:

e[1:3] + e[4:7]    # slice


# In[ ]:

e[:]


# In[54]:

e[:4]+e[5:]


# In[55]:

d


# In[59]:

d[-1][-1][-1]


# In[81]:

methods(list)


# In[62]:

nums = range(10,20+1)
nums


# In[64]:

nums.append(21)
nums


# In[66]:

elem = nums.pop()
nums, elem


# In[67]:

nums.pop(0)
nums


# In[77]:

sum = 0
for num in nums:
    sum += num*num
print sum


# In[ ]:




# In[ ]:




# In[69]:

nums.remove(12)
nums


# In[70]:

nums.extend(range(23,30))
nums


# In[72]:

nums=nums+range(23,30)
nums
pass


# In[76]:

nums[2:5] = [] 


# In[78]:

nums[0:1] = []
nums


# In[82]:

lol = [range(0,5), range(5,10), range(10,15)]
lol


# In[80]:

lol[1].pop(1)


# In[81]:

lol


# In[ ]:

methods(list)


# In[ ]:

e.append(10)


# In[ ]:

help(list.remove)


# In[ ]:

e.extend([1,2,3])


# In[ ]:

e += [1,2,3]
e


# In[ ]:

help(e.sort)


# In[ ]:

e.sort(reverse=True)


# In[80]:

'abcd'.endswith('e')


# In[84]:

names = 'jai viru dhanno basanti thakur gabbar mausi'.split()
names


# In[85]:

for name in names:
    print 'Hi ' + name


# In[86]:

for num in range(1,6+1):
    print num*num


# In[89]:

name= 'ghi'
if name.endswith('i'):
    print name


# In[90]:

help(list.remove)


# In[ ]:




# In[ ]:

for name in names:
    if name.endswith('i'): print name


# In[92]:

Names = []
for name in names:
    Names.append(name.capitalize())
Names


# In[ ]:

for name in Names:
    if name[0].isupper():
        print name


# In[ ]:

for char in 'abcd':
    print char


# In[94]:

if 'jai' in names:
    print 'present'


# In[ ]:




# In[ ]:

help(range)


# In[ ]:

e = range(6,20)
e


# #### for loop

# In[ ]:

i = 0
for elem in e:
    i += 1
    if i%2 == 0:
        print elem*elem


# In[ ]:

# foreach loop
for i in [3, 4, 10, 25]:
    print i

# Print characters one at a time
for c in "Hello World":
    print c
    
# Loop over a range of numbers
for i in range(0,100):
    print i


# In[ ]:

nums = [100, 200, 300]
numsi = range(len(nums)-1, 0-1, -1)

for i in numsi:
    print nums[i]


# In[ ]:

for num in reversed(nums):
    print num


# No `for (i=0; i<10; i++)` loop!

# In[ ]:

nums = range(10)


# In[ ]:

for i in range(len(e)):
    if i%2 == 0:
        print e[i]


# In[ ]:




# In[ ]:

nums = range(10)


# In[ ]:

for i in range(len(nums)-1,-1,-1):
    print nums[i]


# In[ ]:

for num in reversed(nums):
    print num


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# #### Tuples

# In[ ]:

# immutable

exp = (1)
nums = [2,3,4,5]
f = (2,3,4,5)                # A tuple of integers
g = ()                       # An empty tuple
h = (1,)                     # A single-element tuple
h = (2, [3,4], (10,11,12))   # A tuple containing mixed objects


# In[ ]:

type(g)


# In[ ]:

a,b = 1,2
a,b = b,a


# #### Dict

# What if you
# * wanted to lookup a value corresponding to another value (a key)
# * wanted to store key-value pairs efficiently

# In[ ]:




# In[ ]:

a = { }                 # An empty dictionary
b = { 'x': 3, 'y': 4 }
c = { 'uid': 106, 
     'login': 'ash',
     'name' : 'Ashish Gulati',
    }
d = {1:1, 2:2}
type(d)


# In[ ]:

c['name'] = 'xxxx'


# In[ ]:

c['desig'] = 'fac'


# In[ ]:

c['depts'] = ['admin']


# In[ ]:

c['depts'].append('dev')


# In[ ]:

c


# In[ ]:

c['name'], c['desig']


# In[ ]:

del c['login']


# In[ ]:

'name' in c


# In[ ]:

for key in c.keys():
    print key, c[key]


# In[ ]:

methods(dict)


# In[ ]:

c.values()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

for k,v in c.items():
    print k, v


# In[ ]:




# In[ ]:

d = {1:1, 2:2, 3:3}
d[4] = 4
d['hello'] = 5
d[(1,'world')] = 6


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# #### Custom Sorting

# In[ ]:

lot = [[10,2], [5,8], [6,6], [10,10]]
def greater(x,y):
    if x>y:
        return -1
    elif x<y:
        return 1
    else:
        return 0
    
def tup2(tup):
    return tup[1]

def add(tup):
    return tup[0]+tup[1]
    
sorted(lot, reverse=True, key=add)


# In[ ]:

sorted(lot, key=tup[1], reverse=True)


# In[ ]:

empdata = [
    [1, 'z', 'SE', 10],
    [2, 'b', 'SSE', 20],
    [3, 'x', 'VP', 2000],
]


# In[ ]:

def name(emp):
    return emp[1]

def sal(emp):
    return emp[-1]

def name_sal(emp):
    return [emp[1], emp[-1]]

sorted(empdata, cmp=name_sal)


# In[ ]:

help(list.sort)


# In[ ]:

a == range(10)


# In[ ]:

nums1 = range(10)
nums2 = range(10,20)


# In[ ]:

nums1


# In[ ]:

nums2


# In[ ]:

zip(nums1, nums2)


# #### References

# In[ ]:

nums = range(10)
ints = nums
ints.append(10)
print nums


# In[ ]:

print id(nums)
print id(ints)


# In[ ]:

i = 0
print id(i)
i += 1
print id(i)


# In[ ]:

nums = [1,2,3,4,5]
print id(nums)
nums.append(6)
print id(nums)


# #### while loop

# In[ ]:

a=1; b=10
while a < b:
    # Do something
    a = a + 1


# In[ ]:




# In[ ]:




# In[ ]:




# #### Conditionals

# In[ ]:

# Compute maximum (z) of a and b
if a < b:
    z = b
else:
    z = a
    
# empty body-block
if a < b:
    pass       # Do nothing
else: 
    z = a
    


# In[ ]:

if b >= a and b <= c:
    print "b is between a and c"
if not (b < a or b > c):
    print "b is still between a and c"


# In[ ]:

PLUS = 0
MULTIPLY = 1

if a == '+':
    op = PLUS
elif a == '-':
    op = MINUS
elif a == '*':
    op = MULTIPLY
else:
    op = UNKNOWN


# * Indentation used to denote bodies. 
# * pass used to denote an empty body.
# * ** There is no ’?:’ operator. **
# * ** There's no switch statement  ! **

# In[ ]:




# In[ ]:




# #### Functions

# In[ ]:

# Return the remainder of a/b
def remainder(a,b):
    q = a/b
    r = a - q*b
    return r

# Now use it
a = remainder(42,5)        # a = 2
a


# #### Returning multiple values

# In[ ]:

def divide(a,b):
    q = a/b
    r = a - q*b
    return q,r

x,y = divide(42,5)       # x = 8, y = 2
x,y


# #### File I/O

# In[ ]:

f = open("foo","w")       # Open a file for writing
g = open("sop.py","r")       # Open a file for reading


# In[ ]:

g.read()


# In[ ]:

g.seek(0,0)


# In[ ]:

for line in g:
    print line


# In[ ]:




# In[ ]:

methods(f)


# In[ ]:

g.seek(0,0)
g.readline()


# In[ ]:




# In[ ]:

f.write("Hello World")
data = g.read()              # Read all data
line = g.readline()          # Read a single line
lines = g.readlines()        # Read data as a list of lines


# In[ ]:




# In[ ]:




# #### Formatted output

# In[ ]:

for i in range(0,10):
    f.write("2 times %d = %d\n" % (i, 2*i))    # C printf-like formatting


# In[ ]:




# In[ ]:




# In[ ]:




# #### Classes

# In[ ]:

class Account:
    def __init__(self, initial):
        self.balance = initial
    def deposit(self, amt):
        self.balance = self.balance + amt
    def withdraw(self,amt):
        self.balance = self.balance - amt
    def getbalance(self):
        return self.balance


# #### Creating instances

# In[ ]:

a = Account(1000.00)
b = Account(100.0)
a.deposit(550.23)
a.deposit(100)
a.withdraw(50)
print a.getbalance()


# #### Exceptions

# In[ ]:

try:
    f = open("foo")
except IOError,e:
    print "Couldn’t open ’foo’. Sorry."
else:
    pass
finally:
    pass


# #### Raising exceptions

# In[ ]:

def factorial(n):
    if n < 0:
        raise ValueError,"Expected non-negative number"
    if (n <= 1):
        return 1
    else:
        return n*factorial(n-1)


# In[ ]:

try:
    factorial(-1)
except ValueError, e:
    print 'Something broke: ', e


# #### Modules

# In[ ]:

import sys


# In[ ]:

sys.path.append('.')


# Large programs can be broken into modules

# In[ ]:

# numbers.py
def divide(a,b):
    q = a/b
    r = a - q*b
    return q,r

def gcd(x,y): g= y
    while x > 0: 
        g = x
        x = y%x
        y = g 
    return g


# In[ ]:

import numbers
x,y = numbers.divide(42,5)
n = numbers.gcd(7291823, 5683)


# * `import` statment creates a namespace and executes a file in it
# * all names accessible via `modulename.funcname`
# * could be _unwrapped_ to current namespace using `from .. import ..`

# #### Standard modules

# * Python comes pre-packaged with a large number of installed modules (Batteries Included)
# * Other modules can be downloaded/installed to be used by programs

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# | name | age |
# |------|-----|
# | ash | 10 |
# | bash | 20 |

# In[ ]:



