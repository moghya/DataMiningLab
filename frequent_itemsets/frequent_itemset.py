
# coding: utf-8

# In[1]:

import math
from itertools import combinations


# In[2]:

def read_data_in_dict(filename):
    f = open(filename)
    lines = f.readlines()
    transactions = []
    items = lines[0].split(',')
    for line in lines[1:]:
        transactions.append(list(map(int,line.split(','))))
    data ={
        'items':items,
        'transactions':transactions
    }
    return data


# In[3]:

data=read_data_in_dict('itemsets.csv')


# In[4]:

def get_freq(s,items,transactions):
    freq=0
    for t in transactions:
        temp=1
        for item in s:
            temp*=t[items.index(item)]
        if temp==1:
            freq+=1  
    return freq


# In[5]:

def frequent_itemsets(data,level,min_support):
    items = data['items']
    transactions = data['transactions']
    min_freq = math.ceil(min_support*len(transactions))
    sets = list(combinations(items,level))
    frequent_sets = []
    for s in sets:
        freq=get_freq(s,items,transactions)
        if freq>=min_freq:
            frequent_sets.append(s)
    return frequent_sets
        


# In[6]:

frequent_itemsets(data,2,0.5)


# In[ ]:



