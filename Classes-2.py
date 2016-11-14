
# coding: utf-8

# In[1]:

def sayHello(greeting, name):
    print '%s, %s!' % (greeting, name)


# In[2]:

sayHello('Hi', 'Mickey')


# In[3]:

sayHello('Heil', 'Hitler')


# In[16]:

class Hello:
    def __init__(self, greeting, name):
        self.greeting = greeting
        self.name = name
    def sayHello(self):
        print '%s, %s!' % (self.greeting, self.name)


# In[17]:

h = Hello('Hello', 'world')


# In[18]:

h.sayHello()
#sayHello(h, 'Hello', 'world') 


# In[20]:

h.name


# In[21]:

g = Hello('Heil', 'Hitler')
g.sayHello()


# In[22]:

g.name


# In[ ]:




# In[ ]:




# In[ ]:




# In[23]:

class BankAccount:
    def __init__(self, num, name, balance):
        self.num = num
        self.name = name
        self.balance = balance
        #self.priority = False
        
    def deposit(self, amt):
        self.balance += amt
        
    def withdraw(self, amt):
        self.balance -= amt
        
    def close(self):
        self.balance = 0


# In[24]:

g = BankAccount(1, 'gabbar', 1000)
j = BankAccount(1, 'jay', 10000)
v = BankAccount(1, 'veeru', 100)


# In[28]:

accounts = [g,j,v]


# In[29]:

for account in accounts:
    print account.balance


# In[32]:

f = open('accounts.txt')
accounts = []
for line in f:
    fields = line.split(',')
    a = BankAccount(*fields)
    accounts.append(a)



# In[34]:

nameLookup = {}

for ac in accounts:
    nameLookup[ac.name] = ac

while True:
    name = raw_input()
    print nameLookup[name].balance


# In[43]:

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)





# In[44]:

a = Complex(1,2)
b = Complex(3,4)


# In[45]:

c = a+b      # a.add(b)


# In[46]:

c.imag


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



