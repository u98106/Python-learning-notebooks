
# coding: utf-8

# # Classes

# In[ ]:




# ### The class statement

# In[ ]:

class Account(object):
    num_accounts = 0                       # class data
    def __init__(self, name, balance):
        self.name    = name                # public data
        self._balance = balance            # private data
        self.deposited = None
        Account.num_accounts += 1
        #name = name
    def __del__(self):
        Account.num_accounts -= 1
    def deposit(self, amt):
        self.deposited = True
        self._balance += amt
    def withdraw(self, amt):
        self._balance -= amt
    def enquire(self):
        Account.num_accounts
        return self._balance
    @classmethod
    def getNumAccounts(cls):
        return Account.num_accounts


# In[ ]:

Account.getNumAccounts()


# * `__init__` : constructor
# * `__del__` : destructor
#     * not always defined (garbage-collection)
#     * used for closing internal non-reference-counted objects, like open file handles, sockets, etc

# In[ ]:

type(Account)


# ### Instances

# In[ ]:

a = Account('Jay', 1000.00)   # invokes Account.__init__(a, 'Jay', 1000.00)
b = Account('Veeru', 500.00)
#who = a.name
#print Account.num_accounts
a.deposit(200.0)     # deposit(a, 200.0)
a.enquire()
#print Account.getNumAccounts()


# In[ ]:

class Struct:
    pass


# In[ ]:

s = Struct()


# In[ ]:

s.a = 1
s.b = 'hello'


# In[ ]:

s.a, s.b


# ### self

# * very similar to `this`
# * First argument to all instance methods
# * `inst.method(args)`  ==>   `class.method(inst, args)`
# * Also defines instance data : `self.name, self._balance`
# * instance data is added by using it inside an instance method
# * __NOT__ a keyword; just a (very well-followed) convention

# ### Encapsulation

# * No language support for encapsulation
# * Convention: `_names` are taken as class private
# * `__name` taken as private for subclassing
#     * Some versions support name-mangling, but not uniformly supported, can be worked around
# * Respecting Data-hiding conventions programmers responsibility
#   > We're all adults here.

# ### Inheritance

# * Class specialization
# * `derived/sub class` specializes `base/super class`
# * `derived class` inherits all attributes of `base class`
#     * may redifine any of these
#     * may define attributes of its own

# In[ ]:

class TaxedAccount(Account):
    def __init__(self, name, balance):
        #Account.__init__(self, name, balance)
        super(TaxedAccount, self).__init__(name, balance)      # Call base class ctr
        self.tax = 0
        
    def _tax(self):                                            # New private method
        return self._balance * self.tax if self._balance>1000.0 else 0
        
    def enquire(self):
        return super(TaxedAccount, self).enquire(self) - self._tax()


# In[ ]:

class C(B):
    def __init__(self):
        super(B,self)


# In[ ]:

t = TaxedAccount('abc', 1000.0)


# In[ ]:

t.deposit(100.0)   # Account.deposit(t, 100.0)
a.deposit()
t.enquire()


# In[ ]:

type(t)


# In[ ]:




# In[ ]:

get_ipython().magic(u'pinfo super')


# In[ ]:

a = TaxedAccount('Jay', 1000.00)
b = TaxedAccount('Veeru', 500.00)
a.deposit(200.0)
a.enquire()


# In[ ]:

super(TaxedAccount, a).enquire()

#basea = super(TaxedAccount, a)


# In[ ]:




# #### Multiple inheritance

# In[ ]:

class DepositCharge(object):
    fee = 5.00
    def deposit_fee(self):
        self.withdraw(self.fee)

class WithdrawlCharge(object):
    fee = 2.50
    def withdrawl_fee(self):
        self.withdraw(self.fee)

        
#super(self.__class__, self).withdraw(self.fee)


# In[ ]:




# In[ ]:

class EvilAccount(TaxedAccount, DepositCharge, WithdrawlCharge): 
    def __init__(self, *args):
        super(EvilAccount, self).__init__(*args)
    def deposit(self,amt):
        self.deposit_fee()
        super(EvilAccount,self).deposit(amt)
        
    def withdraw(self,amt):
        self.withdrawl_fee()
        super(EvilAccount,self).withdraw(amt)


# In[ ]:

a = EvilAccount('Jay', 1000.00)
a.deposit(200.0)
print a.enquire()
a.withdraw(10.0)
print a.enquire()


# For an excellent article on super:
# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

# ### Method Resolution Order (MRO) and Duck Typing

# * Order in which Methods are resolved
#     * Depth-first, left to right
# * Most specialized class should be left-most, most base right-most
# * Method binding independent of object type
#     * `obj.name` will work for any object that has an attribute `name`
# * This is called **Duck Typing**
# 
# > **"If it looks like a duck, walks like a duck, quacks like a duck .. I'd call it a duck!**

# In[ ]:

EvilAccount.__dict__


# In[ ]:

import inspect
inspect.getmro(EvilAccount)


# ### Static methods

# In[ ]:

def add(x,y)

class Foo(object):
    @staticmethod
    def add(x,y):
        return x + y


# In[ ]:

x = Foo.add(3,4) # x = 7


# In[ ]:

x


# * No `self`
# * decorated with @staticmethod
# * Commonly used for defining custom constructors

# In[ ]:

import time
class Date(object):
    
    def __init__(self,year,month,day):
        self.year = year 
        self.month = month
        self.day = day 
    
    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday) 
            
    @staticmethod
    def tomorrow():
        t = time.localtime(time.time()+86400) 
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


# In[ ]:

# Example of creating some dates
a = Date(1967, 4, 9)
b = Date.now() # Calls static method now()
c = Date.tomorrow() # Calls static method tomorrow()


# In[ ]:

a.month


# In[ ]:




# ### Class methods

# * Operate on the class itself
# * Defined using `@classmethod` decorator
# * Take the class object as the first argument

# In[ ]:

class EuroDate(Date):
    pass
d = EuroDate.now()
type(d)


# In[ ]:

class Date(object):
    def __init__(self,year,month,day):
        self.year = year 
        self.month = month
        self.day = day 
        
    @classmethod
    def now(cls):
        print cls
        t = time.localtime(time.time())
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


# In[ ]:

class EuroDate(Date):
    #
    pass


d = Date.now()
e = EuroDate.now()
type(d), type(e)



# In[ ]:

#dir(list)


# ### Magic Methods & Operator Overloading

# * Methods with __d__ouble-__under__scores are special
#     * __dunder__ or magic methods
# * Implementing classes gain support for a variety of constructs
#     * Arithmetic operators overloading
#     * Comparison operators overloading
#     * Logical operators overloading
#     * Contexts
#     * Object representations
#     * Type casting

# 

# In[ ]:

class Pair(object):
    def __init__(self, a, b):
        self.a, self.b = a,b


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

class Complex(object):
    def __init__(self,real,imag=0):
        self._real = float(real)
        self._imag = float(imag)
#    def __repr__(self):
#        return "Complex(%s,%s)" % (self.real, self.imag)         
#    def __str__(self): 
#        return "(%g+%gj)" % (self.real, self.imag)
    def real(self):
        return self._real
    def __int__(self):
        return int(self.real)
    def __add__(self,other):   # self + other 
        return Complex(self.real + other.real, self.imag + other.imag) 
    def __sub__(self,other):   # self - other 
        return Complex(self.real - other.real, self.imag - other.imag)
    def __lt__(self, other):
        return 


# In[ ]:

l1 = [1,2,3,4]
l2 = [4,5,6,7]
l1 + l2
dir(list)


# In[ ]:

c1 = Complex(1.0,2.0)
c2 = Complex(2.0,5.0)
c3 = c1+c2     # Complex.__add__(c1,c2) called
if c1<c2:
#c3             # Complex.__repr__ called
#print c3


# In[ ]:

Pair(c3)


# In[ ]:

print c1+c2    # Complex.__str__


# In[ ]:




# In[ ]:

str(c1+c2)


# In[ ]:

int(c1)


# #### Dunders for comparison and logic ops
# * `__lt__, __le__, __gt__, __ge__, __eq__, __ne__`
# * Defining any two defines the rest
# * `__and__, __or__, __not__`
# * `__enter__` and `__exit__` for contexts

# In[ ]:

nums = [1,2,3,4]
len(nums)


# 

# 

# ### Properties and Descriptors

# * Normal (public) data attributes readable/writable directly
# * Many classes define getters/setters to hide data 
# * Property is a special attribute that calculates its value when accessed
# * Has a setter equivalent too

# In[ ]:

class Foo(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        print 'Setting to ', name
        self._name = name
    
    
    
    
foo = Foo('xyz')
print foo.name
foo.name = 'abc'
print foo.name


# In[ ]:




# In[ ]:




# In[ ]:

class Foo(object):
    def __init__(self,name): 
        self.__name = name 
    @property
    def name(self): 
        return self.__name 
    @name.setter 
    def name(self,value): 
        if not isinstance(value,str): 
            raise TypeError("Must be a string") 
        self.__name = value 
    @name.deleter 
    def name(self):
        raise TypeError("Can't delete name")


# In[ ]:

g = Foo('Guido')
print g.name
g.name = 'Monty'
print g.name
g.name = 45
del g.name


# * Any object that defines `__get__, __set__ and __dell__` is acceptable as a property
# * This is the `Descriptor` interface
# * Descriptors instantiable only at the class level, not instance level

# In[ ]:

class TypedProperty(object):
    def __init__(self,name,type,default=None):
        self.name = "_" + name
        self.type = type
        self.default = default if default else type()
    def __get__(self,instance,cls): 
        #return getattr(instance,self.name,self.default) 
        return instance.(self.name)
    def __set__(self,instance,value):
        if not isinstance(value,self.type):
            raise TypeError("Must be a %s" % self.type) 
        setattr(instance,self.name,value) 
    def __delete__(self,instance):
        raise AttributeError("Can't delete attribute")
    
class Foo(object):
    name = TypedProperty("xyz",str, 'abc') 
    num = TypedProperty("num",int,42)


# In[ ]:

f = Foo()
a = f.name 
f.name = "Guido" 
#del f.name


# In[ ]:

f._xyz


# In[ ]:

f.name = 42


# In[ ]:

class MyDict(dict):
    __slots__ = ['a','b','c']
    def __init__(self, data):
        super(MyDict, self).__init__(data)
    pass


# In[ ]:

d = MyDict({'a':1, 'b':2, })


# In[ ]:

d['x'] = 10


# In[ ]:

d


# In[ ]:




# In[ ]:

a = dict({'a':1, 'b':2})
b = dict({'a':10, 'b':11})


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



