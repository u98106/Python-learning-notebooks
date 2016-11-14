
# coding: utf-8

# In[1]:

import multiprocessing


# In[ ]:




# In[ ]:




# In[8]:

dir(multiprocessing)


# In[9]:

mgr = multiprocessing.Manager()


# In[ ]:

mgr.


# In[ ]:

'Process',

'Lock',
'RLock',
'Semaphore',

'BoundedSemaphore',
'Condition',
'Event',

'Queue',
'JoinableQueue',

'Manager',
'Pool',


# #### Calling Process directly

# In[ ]:

Process(target=func)


# In[ ]:

Process(target=func, args=(1,2,3))


# #### Subclassing

# In[ ]:

class worker(Process):
    def run(self):
        pass


# In[ ]:




# #### Synchronizing shared resource

# In[ ]:

Lock
.acquire()
.release()


# In[ ]:

RLock


# In[ ]:




# In[ ]:




# In[1]:

import threading/multiprocessing


# In[2]:

def f(a,b):
    print 'hello'


t = multiprocessing.Process(target=f, args=(1,2))
t.start()


# In[ ]:



class Worker(threading.Thread):
    def __init__(self):
        
        self.rlock = threading.Semaphore(5)
        self.wlock = thread.Lock()
        self.fobj = open('dummy.txt')
        
    
    def run(self):
        #self.lock.acquire()
        self.wlock.acquire()
        with self.rlock:
            for line in self.fobj:
                pass
        #self.lock.release()
        
        
    pass

w = Worker()
w.start()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



