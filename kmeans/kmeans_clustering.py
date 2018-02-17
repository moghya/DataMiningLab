
# coding: utf-8

# In[1]:

import json
import math
import copy
from random import shuffle


# In[2]:

def read_data_from_csv(filename):
    f = open(filename)
    lines = f.readlines()
    data = {}
    headers = lines[0].split(',')
    points = []
    for  i in range(1,len(lines)):
        ordinates = list(map(float,lines[i].split(',')))
        point = {}
        for j in range(len(headers)):
            point[headers[j]]=ordinates[j]
        points.append(point)
    data['ordinates'] =headers
    data['points']=points
    return data


# In[3]:

def euclidean_distance(a,b,ordinates):
    distance=0
    for i in range(len(ordinates)):
        distance+=(a[ordinates[i]]-b[ordinates[i]])**2
    return distance**0.5


# In[4]:

def update_centroid(cluster,ordinates):
    for ordinate in ordinates:
        temp = 0
        for point in cluster['points']:
            temp+=point[ordinate]
        cluster['centroid'][ordinate]=(temp/len(cluster['points']))
    return cluster


# In[5]:

def add_points_into_clusters(clusters,points,ordinates):
    for cluster in clusters:
        cluster['points']=[]
    
    for point in points:
        min_distance = euclidean_distance(point,clusters[0]['centroid'],ordinates)
        min_index = 0
        for i in range(1,len(clusters)):
            temp = euclidean_distance(point,clusters[i]['centroid'],ordinates)
            if temp<min_distance:
                min_distance=temp
                min_index=i
        clusters[min_index]['points'].append(point)
        clusters[min_index]=update_centroid(clusters[min_index],ordinates)

    return clusters


# In[6]:

def kmeans_clustering(data,k,iterations):
    clusters = []
    points = data['points']
    ordinates = data['ordinates']
    if k >=len(points):
        for point in points:
            clusters[i].append(point)
        return clusters    
    shuffle(points)
    for i in range(k):
        cluster = {
            'centroid':0,
            'points':[]
        }
        cluster['centroid'] = copy.deepcopy(points[i])
        clusters.append(cluster)
        
    iteration=0
    while iteration<iterations:
        clusters = add_points_into_clusters(clusters,points,ordinates)
        iteration+=1
    return clusters


# In[7]:

def print_clusters(clusters):
    for i in range(0,len(clusters)):
        print('Cluster No: ',i+1)
        print('\tCentroid:',str(clusters[i]['centroid']))
        print('\tPoints:',str(clusters[i]['points']))


# In[8]:

c = kmeans_clustering(read_data_from_csv('kmeans_data.csv'),3,1)


# In[9]:

print_clusters(c)

