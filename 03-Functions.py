
# coding: utf-8

# # Functions

# * Created with def
# * Possibly empty list of arguments
# * May return a value

# In[ ]:

def add(a,b):
    return a+b


# Positional arguments: should be specified in correct order

# In[ ]:

add(2)


# ### Variable args

# How do we support variable number of positional args?

# In[ ]:




# In[ ]:

def f(a,b,*args):
    print 'a,b:',a,b
    print 'Rest', args
    for arg in args:
        pass
    #arg1, arg2, arg3 = args


# In[ ]:

f(1,b=2)


# * `*args` 'absorbs' rest of the arguments
# * 'args' not a keyword; just a (very well-followed) convention; could be `*rest`, `*z`, ..
# * received as a tuple
# * Should be the last argument (why?)

# In[ ]:




# ### Default values

# In[ ]:

def f(a,b=2,*args):
    print 'a,b:',a,b
    print 'Rest', args


# In[ ]:

f(a=1, b=2)


# In[ ]:

f()


# * Default value args should be last
# * Before `*args` (why?)

# 

# In[ ]:

f(1)


# In[ ]:

f(1,2,3)


# In[ ]:




# #### Exercise: implementing range() function

# In[ ]:

range(5,10,2,3)


# In[ ]:

range(stop)
range(start, stop)
range(start, stop, step)


# In[ ]:

def myrange(stop,*args):
    start=0
    step=1
    if len(args)==0:
        pass
    elif len(args)==1:
        start=stop
        stop=args[0]
    elif len(args)==2:
        start=stop
        stop,step = args
#        stop=args[0]
#        step=args[1]
    else:
        raise TypeError, 'Too many args!'
    print 'start: {0}, stop: {1}, step: {2}'.format(start, stop, step)


# In[ ]:

myrange(1, 10, 5)


# In[ ]:




# ### Keyword Args

# * Large functions may have a large number of optional args: positional args not a good approach
# * Better approach : `f(config='cfg.py', log='app.log')`

# * `**kwargs` defines keyword args
# * should be the last arg in arglist, after any `*args` if present
# * kwargs received as a dict
# * allows support for arbitrary keywords as arguments
# * again: kwargs not a keyword; could be `**d`, ..

# In[ ]:

def f(a,b,*args,**kwargs):
    '''
    
    '''
    print 'a,b', a,b
    print 'Rest', args
    #open(kwargs['config'])
    print 'Keyword args', kwargs
    config = kwargs['config']
    


# In[ ]:

f(1,2,config='cfg.py', log='app.log', mult=10)


# In[ ]:




# ### Unfolding args when calling

# In[ ]:

vals = [1,2,3,4]
keyvals = {'key': 1, 'cmp': None}
f(*vals, **keyvals)


# In[ ]:

keypos = {'b':1, 'a':2}
f(**keypos)


# But, how about..

# In[ ]:




# In[ ]:

f(*range(5))


# In[ ]:

f(*xrange(5))


# ### Receiving and passing fwd arbitrary args

# In[ ]:

def wrap(func, *args, **kwargs):
    # Do something
    ret = func(*args, **kwargs)
    # Do something else
    return ret


# * Supports any kind of function signature
# * Reliably passes fwd received args
# * A very commonly seen pattern

# ### Rules

# * Mandatory args must be specified exactly once (positionally, or keyword-ly)
# * positional args need to be in order
# * keyword args may be specified in any order
# * `*args` can be the last positional parameter
# * Default value args should be last, but before `*args`
# * `**kwargs` can be the very last parameter
# * `*lval` to unfold list (iterable) arg
# * `**dval` to unfold dict arg
# * positional parameters not valid after `*args`, `**kwargs`; raise a SyntaxError exception

# 

# Is **def** the only way to define functions?

# ### Lambda functions

# Adopted from formal mathematics
# $$\lambda x \rightarrow x^2$$
# 
# * Convenient way for creating functions on the fly
# * For passing functions around (as args)
# * Does not support code-block; just single line code
# * no return needed
# * a functional programming feature ==> python supports functional paradigm
# 

# 

# In[ ]:

def sum(a,b): return a+b


# In[ ]:

sum = lambda a,b: a+b
sum


# In[ ]:

sum(1,2)


# This is saying exactly the same thing as:

# In[ ]:

def sum(a,b):
    return a+b


# In[ ]:

tuplist = [(9,2), (6,3), (1,-1), (2,1)]


# In[ ]:

sorted(tuplist)


# In[ ]:

get_ipython().magic(u'pinfo sorted')


# In[ ]:

def getone(x): return x[1]


# In[ ]:

sorted(tuplist, key=getone)


# In[ ]:

sorted(tuplist, key=lambda x:x[1])


# In[ ]:




# In[ ]:

f = lambda:42


# In[ ]:

f()


# ### Other functions that take/return functions

# #### map

# In[ ]:

nums = range(10)
nums


# In[ ]:

sq = []
for num in nums:
    sq.append(num*num)
sq


# In[ ]:

len(nums)


# In[ ]:

len(sq)


# In[ ]:

[x*x for x in nums]


# In[ ]:

get_ipython().magic(u'pinfo map')


# In[ ]:

min(nums)


# In[ ]:

map(lambda x:x**2, nums)


# In[ ]:

map(lambda s:s.upper(), 'a string in all lowers'.split())


# In[ ]:

import inspect


# In[ ]:

def mymap(func, mylist):
    ret = []
    for elem in mylist:
        ret.append(func(elem))
    return ret


# In[ ]:




# In[ ]:




# In[ ]:

mymap(lambda s:s.upper(), 'a string in all lowers'.split())


# In[ ]:




# #### reduce

# In[ ]:

reduce(lambda x,y:x+y, range(10))


# In[ ]:

def greater(x,y):
    if x>y:
        return x
    else:
        return y

max = x if x>y else y


# In[ ]:

reduce(lambda x,y: x if x>y else y,  [1,10,9, -10])


# In[ ]:




# In[ ]:




# In[ ]:

reduce(lambda x,y: x if x>y else y, [1,8,9,-1])


# #### filter

# In[ ]:

filter(lambda x:x.isalpha(), 'all sorts of !@# things that a 5 year old does'.split())


# In[ ]:

out = _


# ### Callables

# Q: So, only functions can be called thus: f()  ?
# 
# A: No. Any object with an attribute/method `__call__`
# 
# More under **`class`**

# 

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# 

# ### Mandatory keyword-only args?

# https://www.python.org/dev/peps/pep-3102/ [PEP3102]

# Supported only in 3.5+

# In[ ]:




# In[ ]:




# In[ ]:

z = xrange(10,20,2)


# In[ ]:

a = [1,2,3,4]
b = a[:]
a += [5]
b


# In[ ]:

for i in z:
    print i

