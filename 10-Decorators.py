
# coding: utf-8

# # Decorators

# 

# ### The Concept

# Adding functionality to a function
# 
# _Without_ modifying the function

# >func(func) -> func

# Function that takes a function (as arg) and returns another function (usually with functionality added)

# 

# ### Function arg

# In[ ]:

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def apply(f,x,y):
    return f(x,y)


# In[ ]:

apply(add,2,3)


# In[ ]:

apply(sub,5,2)


# Other common functions that take functions?
# * map
# * reduce
# * filter

# In[ ]:




# ### Function return
# 
# or, function in a function

# In[ ]:

def outer():
    x = 1
    def inner():
        print x        
    return inner

foo = outer()
foo()


# In[ ]:


def outer(x):
    def inner():
        print x
    return inner

print1 = outer(1)
print2 = outer(2)


# In[ ]:

print1()


# In[ ]:

print2()


# In[ ]:




# In[4]:

def outer(func):
    def inner():
        print "Before"
        func()
        print "After"
    return inner

--------------

@outer
def foo():
    print 'hello'

#foo = outer(foo)
foo()


# ### Decorator!

# In[53]:

def italics(fn):
    def fn2():
        return '<i>' + fn() + '</i>'
    return fn2

@bold
@italics
def msg():
    return "Hello"

#msg = italics(msg)

msg()


# In[ ]:

def bold(fn):
    def fn2():
        return '<b>' + fn() + '</b>'
    return fn2

def tag(tagtype):
    
    return None

#@italics
whichtag='b'
@tag(whichtag)
def msg():
    return "Hello"

msg()
whichtag='i'
msg()

#msg = bold(italics(msg))

msg()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

def debug(fn):
    def fn2(*args, **kwargs):
        print 'called with ', args, kwargs
        return fn(*args, **kwargs)
    return fn2

class A:
    def a():
        pass
    def b():
        pass


# ### `*args` and `**kwargs`

# In[ ]:

def fn(x,y,*args):
    print x,y,args
    
fn(1,2)


# In[ ]:

fn(1,2,3,4,5)


# In[ ]:

def f():
    print "Hello"
    
def f(x):
    print "Hello"+x


# In[ ]:

f()


# In[ ]:

def fn2(**kwargs):
    print kwargs
    
fn2(x=1,y=2)


# In[ ]:




# In[54]:

def debug(fn):
    def inner(*args, **kwargs):
        print "Args were " + str(args) + str(kwargs)
        return fn(*args, **kwargs)
    return inner


# In[57]:

@debug
def msg(x):
    return "Hello"+x

@debug
def msg2(x,y):
    return x,':',y

msg('MrX')


# In[58]:

msg2("hi",5)


# In[ ]:




# In[ ]:




# ### Class Decorators

# In[ ]:

class Foo(object):
    def fn1(*args):
        pass
    def fn2(*args):
        pass


# In[ ]:

a = Foo()
a.fn1(1,2)
a.fn2(3,4)


# In[ ]:

Foo.__name__


# In[ ]:

from inspect import isfunction

def debugclass(klass):
    name  = klass.__name__
    bases = klass.__bases__
    kdict = {}
    for name,attrib in klass.__dict__.items():
        kdict[name] = debug(attrib) if isfunction(attrib) else attrib
    newklass = type(name, bases, kdict)
    return newklass



# In[ ]:

#@debugclass
class Foo(object):
    def fn1(*args):
        pass
    def fn2(*args):
        pass


# In[ ]:

a = Foo()
a.fn1(1,2)
a.fn2(3,4)


# In[ ]:

registry = { }

def register(cls):
    registry[cls.__clsid__] = cls
    return cls


# In[ ]:




# In[ ]:

@register
class Foo(object):
    __clsid__ = "123-456" 
    def bar(self):
        pass


# In[ ]:

f = Foo()


# In[ ]:

registry


# In[ ]:

class Foo(object):
    __clsid__ = "123-456" 
    def bar(self):
        pass

register(Foo)


# Both are exactly the same
# 
# Decorator is just syntactic sugar

# In[ ]:




# #### Singletons

# In[64]:

def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        
        print instances
        return instances[cls]
        
    return get_instance


# In[65]:

@singleton
class Foo(object):
    pass

@singleton
class Bar(object):
    pass

x=Foo()
y=Foo()
#id(x), id(y)

x = Bar()
y = Bar()
#id(x), id(y)


# In[66]:




# In[ ]:




# #### Avoid!

# In[ ]:

def modify(cls):
    class newclass(cls):
        def newmeth(): print "hello"
    return newclass


# In[ ]:




# ### Decorators taking arguments

# In[ ]:

@decorator
def foo(*args, **kwargs):
    pass

foo = decorator(foo)


# In[ ]:

@decorator_with_args(arg)
def foo(*args, **kwargs):
    pass

foo = decorator_with_args(arg)(foo)


# In[ ]:

def decorator(argument):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            funny_stuff()
            something_with_argument(argument)
            function(*args, **kwargs)
            more_funny_stuff()
        return wrapper
     return real_decorator
    
@decorator(1)
def f(*args):
    pass


# In[ ]:

from functools import partial

def _pseudo_decor(fun, argument):
    def ret_fun(*args, **kwargs):
        #do stuff here, for eg.
        print "decorator arg is %s" % str(argument)
        return fun(*args, **kwargs)
    return ret_fun

real_decorator = partial(_pseudo_decor, argument=arg)

@real_decorator
def foo(*args, **kwargs):
    pass


# In[ ]:




# In[ ]:




# In[ ]:




# ### Metaclasses

# In[ ]:

class DocMeta(type):

    def __init__(self, name, bases, attrs):
        for key, value in attrs.items():
            # skip special and private methods
            if key.startswith("__"): continue
            # skip any non-callable
            if not hasattr(value, "__call__"): continue
            # check for a doc string. a better way may be to store 
            # all methods without a docstring then throw an error showing
            # all of them rather than stopping on first encounter
            if not getattr(value, '__doc__'):
                raise TypeError("%s must have a docstring" % key)
        type.__init__(self, name, bases, attrs)


# In[ ]:

class Car(object):

    __metaclass__ = DocMeta

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def change_gear(self):
        print("Changing gear")

    def start_engine(self):
        print("Changing engine")

car = Car()


# In[ ]:

class final(type):
    def __init__(cls, name, bases, namespace):
        super(final, cls).__init__(name, bases, namespace)
        for klass in bases:
            if isinstance(klass, final):
                raise TypeError(str(klass.__name__) + " is final")


# In[ ]:

class B(object):
    __metaclass__ = final
    
class C(B):
    pass


# In[ ]:



