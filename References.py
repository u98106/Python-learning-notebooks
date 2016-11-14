
# coding: utf-8

# ## What is a reference?

# Very similar to a pointer in C
# 
# ### A different var name pointing to the same data

# In[ ]:




# In[ ]:




# Let's look at the following code:

# In[1]:

x = [1,2,3,4,5]


# In[2]:

x


# In[3]:

y = x


# In[4]:

x.pop()


# In[5]:

x


# In[6]:

y


# In[7]:

id(x)


# In[8]:

id(y)


# How do we fix this?

# In[9]:

y = x[:]


# In[10]:

x.pop()


# In[11]:

x


# In[12]:

y


# In[13]:

id(y)


# In[ ]:



