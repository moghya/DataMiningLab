
# coding: utf-8

# In[18]:

import math


# In[19]:

def read_data(filename):
    f = open(filename)
    lines = f.readlines()
    data = []
    for l in lines:
        data.append(float(l.strip()))
    return data


# In[20]:

data=read_data('five_point_data.csv')


# In[21]:

def median(data):
    l = len(data)
    if l%2!=0:
        return data[math.ceil(l/2)]
    return (data[l//2]+data[(l//2)-1])/2


# In[22]:

def five_point_summary(data):
    l = len(data)
    data.sort()
    s= {}
    s['min_value'] = min(data)
    s['q1']=median(data[0:l//2])
    s['median_value']= median(data)
    s['q2']=median(data[l//2:])
    s['max_value'] = max(data)
    return s


# In[23]:

five_point_summary(data)


# In[ ]:



