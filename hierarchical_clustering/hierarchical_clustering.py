
# coding: utf-8

# In[1]:

def read_csv_in_2d_matrix(filename):
    f = open(filename)
    data = {}
    lines = f.readlines()
    data['cols'] = []
    data['rows'] = []
    for name in lines[0].split(','):
        data['cols'].append([name])
        data['rows'].append([name])
        
    data['mat'] = []
    for i in range(1,len(lines)):
        data['mat'].append(list(map(int,lines[i].split(','))))
    return data


# In[2]:

def print_2d_mat(data,complete=True):
    print(' ',end='')
    for name in data['cols']:
        print(name,end=' ')
    print()
    if complete:
        for i in range(0,len(data['rows'])):
            row = data['mat'][i]
            print(data['rows'][i],end=' ')
            for col in row:
                print(col,end=' ')
            print()
        print('_________________________________')


# In[3]:

def find_row_col_of_min_from_2d(data):
    mat = data['mat']
    min_element = min(mat[0])
    min_col = mat[0].index(min_element)
    min_row = 0
    for i in range(1,len(mat)):
        min_in_row = min(mat[i][0:i])
        if min_in_row <min_element or min_element==0:
            min_col = mat[i].index(min_in_row)
            min_row = i
            min_element=min_in_row
            
    return min_row,min_col


# In[4]:

def merge_clusters_and_update_mat(data,min_location):
    new_mat = []    
    
    min_index_of_location = min(min_location)
    max_index_of_location = max(min_location)
    data['cols'][min_index_of_location]+=data['cols'][max_index_of_location]
    data['rows'][min_index_of_location]+=data['rows'][max_index_of_location]
    del data['cols'][max_index_of_location]
    del data['rows'][max_index_of_location]
    mat = data['mat']
    for i in range(1,len(mat)):
        new_row = []
        for j in range(1,len(mat)):
            value = mat[i-1][j-1]
            if i-1==min_index_of_location:
                value=min(value,mat[max_index_of_location][j-1])
            elif j-1==min_index_of_location:
                value=min(value,mat[max_index_of_location][i-1])                
            new_row.append(value)
            
        new_mat.append(new_row)    
    data['mat']=new_mat
    return data


# In[5]:

def clustering(data):
    while len(data['cols'])!=1:
        print_2d_mat(data,False)
        min_location = find_row_col_of_min_from_2d(data)
        data = merge_clusters_and_update_mat(data,min_location)
    print_2d_mat(data,False)


# In[6]:

clustering(read_csv_in_2d_matrix('distances.csv'))


# In[ ]:



