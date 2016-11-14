
# coding: utf-8

# # Collections

# In[2]:

from IPython.core.display import HTML
css = "table td:nth-child(1) {font-weight:bold; background-color: #fec; }"
HTML('<style>{}</style>'.format(css))


# ### Containers

# * Objects that 'contain' other objects
# * Generic: type of contained object not fixed
# * Inbuilt: list, dict, set, tuple
# 
# 
# * More specialized uses?
# * User-defined containers?
# * ==> Collections

# | Type | Description | Version
# |------|-------------|----------
# | Counter | dict subclass for counting hashable objects | New in version 2.7.
# | defaultdict | dict subclass that calls a factory function to supply missing values | New in version 2.5.
# | OrderedDict | dict subclass that remembers the order entries were added | New in version 2.7.
# | namedtuple() | factory function for creating tuple subclasses with named fields | New in version 2.6.
# | deque	| list-like container with fast appends and pops on either end | New in version 2.4.
# 
# 

# In[55]:

words = "a an the an a the an".split()


# In[57]:

from collections import Counter
c = Counter(words)
c.most_common(1)


# In[ ]:




# In[74]:

di = collections.defaultdict(lambda:42)
di[1] = 100
di['a']


# In[72]:

di[2].append(2)


# In[71]:

di[1].append(1)


# In[ ]:




# In[ ]:




# In[ ]:




# In[1]:

nums = [1,2,3,4]
for i in nums:
    print i


# In[3]:

for line in open('Collections.py'):
    #print line
    pass


# In[3]:

nums  = [1,2,3,4,5]
numsi = iter(nums)
numsi


# In[9]:

next(numsi)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[19]:

import collections


# In[20]:

collections.Counter('abcdaabbccd')


# In[23]:

collections.Counter({'a':3, 'b':4})


# In[1]:

nums = range(10)


# In[2]:

for i in nums:
    print i


# In[7]:

f = open("00-Intro.ipynb")


# In[8]:

for line in f:
    #print line
    pass


# In[7]:

ni = iter(nums)


# In[28]:

ni


# In[19]:

next(ni)


# In[26]:

next(f) is None


# In[1]:

class Nums(object):
    limit = 10
    def __init__(self):
        self.val = 0
        #self.vals = vals
        #pass
    
    def __next__(self):
        self.val += 1
        if self.val >= Nums.limit: raise StopIteration
        return self.val
    
    def next(self):
        return self.__next__()

    def __iter__(self): return self


# In[2]:

nums = Nums()


# In[3]:

for i in nums:
    print i


# In[ ]:




# In[ ]:

def for(i, obj):
    try:
        while True:
            i = next(obj)
        except StopIteration:
            break


# In[65]:

class A(object): pass
class B(A):
    def f(): pass
    def g(): pass


# In[62]:

B.__dict__


# In[78]:




# In[67]:

def f(): pass
def g(): pass


name = 'C'
bases = (A,)
Bdict = {'f': f, 'g':g }

C1 = type(name, bases, Bdict)


# In[69]:

C1.__dict__


# In[74]:

C1.__bases__


# In[79]:

import abc
import types
types.


# In[80]:


def abstractclass(cls):
    name = cls.__name__
    bases = cls.__bases__
    mdict = cls.__dict__
    absdict = { }
    
    for mname, method in mdict.items():
        if isinstance(method, types.FunctionType):
            absdict[mname] = abc.abstractmethod(method)
        else:
            absdict[mname] = method

    abclass = type(name, bases, absdict)
    abclass
    
    return abclass


# In[87]:

@abstractclass
class allabstract(object):
    __metaclass__ = abc.ABCMeta
    def f(): pass
    def g(): pass
    
class derived(allabstract):
    def f(): pass
    # def g(): pass


# In[86]:

allabstract.__dict__


# In[56]:

class AbstractNum(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def f(): pass
    @abc.abstractmethod
    def g(): pass
    
class Int(AbstractNum):
    def f(self): print "f"
    def g(self): print "g"
        


# In[82]:

AbstractNum.__dict__


# In[ ]:




# In[57]:

i = Int()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# ### User defined containers

# ABC's/interfaces defined for user to implement custom Containers

# **Abstract Base Classes**
# * At least one @abstractmethod
# * Can't be instantiated: only inherited and implemented

# 

# In[91]:

import collections


# In[93]:




# In[9]:

#help(collections.Counter)


# In[98]:

c = collections.Counter({'a':1, 'b':2})


# In[111]:

d = collections.defaultdict(list)
d[2].append('a')


# In[113]:

d[1]


# In[ ]:

struct = (name, age, salary)
NAME = 0
AGE = 1
SALARY = 2
struct[2]


# In[114]:

PersInfo = collections.namedtuple('PersInfo', ['name', 'age', 'salary'])


# In[116]:

p = PersInfo(name='abc', age=21, salary=1000)


# In[117]:

p.name


# ### 'Real' collection example

# In[42]:

class A(Iterable):
    pass
#a = A()
import collections
dir(collections)


# In[5]:

class Card(object):
    def __init__(self, rank, suit):
        FACE_CARD = {11: 'J', 12: 'Q', 13: 'K'}
        self.suit = suit
        self.rank = rank if rank <=10 else FACE_CARD[rank]
    def __str__(self):
        return "%s%s" % (self.rank, self.suit)
    def __repr__(self):
        return self.__str__()
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit<other.suit
        else:
            return self.rank<other.rank
    
class Deck(object):
    def __init__(self):
        self.current = 0
        self.total = 13*4
        self.cards = []
        for s in ['S', 'D', 'C', 'H']:
            for r in range(1, 14):
                self.cards.append(Card(r, s))
    def __iter__(self): return self
    def __next__(self): return self.next()
    def next(self):
        if self.current >= self.total:
            self.current = 0
            raise StopIteration
        ret = self.cards[self.current]
        self.current += 1
        return ret
        


# In[7]:

d = Deck()
min(d)


# In[ ]:




# In[ ]:




# In[ ]:




# In[53]:

import abc


# In[ ]:

collections.


# In[37]:

deck = Deck()
#dir(deck)


# In[18]:

for c in deck:
    print c


# In[34]:

sorted(deck, reverse=True)


# In[31]:

type(_)


# In[ ]:




# In[26]:

min([1,2,9,1,-1])


# In[27]:

min('a b z y s b'.split())


# In[38]:

print min(deck)


# ### map(), reduce(), filter()

# In[47]:

#def add2(a,b): return a+b
reduce(lambda x,y: x if x>y else y, [1,2,3,4,5])


# In[46]:

sum([1,2,3,4,5])


# In[48]:

map(lambda x:x**2, [1,2,3,4])


# ### Custom Collections

# In[49]:

from collections import Counter


# In[52]:

words = 'a and the the and a a and the the'.split()
counts = Counter(words)
counts.most_common(1)


# In[ ]:




# In[48]:

from abc import ABCMeta, abstractmethod

class myclass(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def f(a,b,c):
        pass
    
    def g():
        pass
    
class derived(myclass):
    def f(a,b,c):
        pass
    pass


# In[49]:

d = myclass()


# In[47]:

d.f(1,2)


# In[ ]:




# In[75]:

xr = xrange(10,20)
xr


# In[77]:

for i in xr:
    print i


# In[79]:

def inf():
    i = 0
    while True:
        yield i
        i += 1
        


# In[88]:

class genclass(object):
    def gen1(self):
        i = 0
        while True:
            yield i
            i += 1
            


# In[89]:

a = genclass()
gen1 = a.gen1()
gen2 = a.gen1()


# In[91]:

i1 = iter(gen1)
i2 = iter(gen2)


# In[97]:

#print next(i1)
print next(i2)


# In[ ]:




# In[80]:

infseq = inf()
infseq1 = inf()


# In[81]:

infseq = iter(infseq)


# In[87]:

next(infseq)


# In[ ]:



