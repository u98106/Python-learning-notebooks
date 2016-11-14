
# coding: utf-8

# In[1]:

a = 10
print a*a
f(a)


# In[ ]:

def f(a):
    pass

f(10)


# In[ ]:

class Shape(object):
    def __init__(self):
        pass
    def area(self):
        pass
    def peri(self):
        pass


# In[26]:

class Rectangle(object):
    def __init__(self, length, width=None):
        self.length = length
        if width is not None:
            self.width = width
        else:
            self.width = self.length
        self.color = 'black'
    def area(self):
        super().area()
        return self.length * self.width
    def peri(self):
        return 2*(self.length+self.width)


# In[27]:

rect = Rectangle(10,20)
print rect.area()
print rect.peri()


# In[24]:

rect.area()


# In[25]:

Rectangle.area(rect)


# In[39]:

'Magic functions or dunders  (Double-under)'

class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        self.real += other.real
        self.imag += other.imag
        return self
    def _update(self,)
    


# In[40]:

cmp1 = Complex(1, 2)
cmp2 = Complex(3, 4)
res = cmp1+cmp2


# In[36]:

res


# In[41]:

res.real, res.imag


# In[55]:

class Card(object):
    def __init__(self, rank, suite):
        self.rank   = rank
        self.suite  = suite
    def __str__(self):
        return '(%2d %10s)' % (self.rank, self.suite)
    def __repr__(self):
        return self.__str__()
    def __lt__(self, other):
        return self.rank<other.rank


# In[56]:

ac = Card(1, 'Club')
kd = Card(13, 'Diamond')


# In[57]:

print ac
print kd


# In[58]:

ac<kd


# In[59]:

ranks = [3,1,7,13,2,4,9,8,5,6,10,12,11]
cards = []
for rank in ranks:
    cards += [Card(rank, 'Club')]


# In[60]:

cards


# In[62]:

cards.sort()
cards


# In[63]:

print cards


# In[ ]:



