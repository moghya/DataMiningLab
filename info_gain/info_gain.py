
# coding: utf-8

# In[1]:

import math


# In[2]:

def read_csv_into_dict(file_name):    
    data = {}
    data['_headers_'] = []    
    f = open(file_name)    
    lines = f.readlines()    
    data['_total_tuples_'] = len(lines)-1
    for attrib in lines[0].split(','):
        data[attrib] = []
        data['_headers_'].append(attrib)    
    number_of_attribs = len(data['_headers_'])    
    for i in range(1,len(lines)):
        line  = lines[i].split(',')
        for j in range(0,number_of_attribs):
            data[data['_headers_'][j]].append(line[j])    
    f.close()
    return data


# In[3]:

def get_pi_log_pi(p,q):
    if p==0 or q==0:
        return 0
    return (p/q)*math.log(p/q,2)


# In[4]:

def get_info_gain(data,attribute):
    aux = {}
    target = data['_headers_'][-1]
    unique_values_of_target = set(data[target])
    unique_values_of_attribute = set(data[attribute])    
    of_all_data = 0    
    
    for value_of_target in unique_values_of_target:
        of_all_data+=get_pi_log_pi(data[target].count(value_of_target),len(data[target]))
    
    for value_of_attribute in unique_values_of_attribute:
        aux[value_of_attribute]={}
        for value_of_target in unique_values_of_target:
            aux[value_of_attribute][value_of_target]=0
        aux[value_of_attribute]['_total_']=0
    
    for i in range(0,data['_total_tuples_']):
        value_of_attribute = data[attribute][i]
        value_of_target = data[target][i]
        aux[value_of_attribute][value_of_target]+=1
        aux[value_of_attribute]['_total_']+=1
        
    gain = 0
    
    for value_of_attribute in unique_values_of_attribute:
        temp =0
        for value_of_target in unique_values_of_target:
            temp+=get_pi_log_pi(aux[value_of_attribute][value_of_target],aux[value_of_attribute]['_total_'])
        gain+=(aux[value_of_attribute]['_total_']/len(data[target]))*temp
    
    gain=gain-of_all_data
    return gain


# In[5]:

data = read_csv_into_dict('tennis.csv')
print(get_info_gain(data,'humidity'))
print(get_info_gain(data,'temp'))
print(get_info_gain(data,'windy'))


# In[6]:

data = read_csv_into_dict('laptops.csv')
print(get_info_gain(data,'age'))


# In[7]:

get_pi_log_pi(5,14)+get_pi_log_pi(9,14)

