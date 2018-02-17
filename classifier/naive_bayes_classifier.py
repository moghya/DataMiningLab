
# coding: utf-8

# In[23]:

from random import *
import math


# In[24]:

def read_csv_data(filename):
    f = open(filename)
    lines = f.readlines()
    dataset = []
    for l in lines:
        dataset.append(list(map(float,l.split(','))))
    return dataset


# In[25]:

def split_dataset(dataset, split_ratio):
    train_size = int(len(dataset) * split_ratio)
    shuffle(dataset)
    train = dataset[0:train_size]
    test = dataset[train_size:]
    return [train, test]


# In[26]:

def mean(dataset):
    return sum(dataset)/float(len(dataset))

def std(dataset):
    avg = mean(dataset)
    variance = sum([pow(x-avg,2) for x in dataset])/float(len(dataset)-1)
    return math.sqrt(variance)


# In[27]:

def divide_on_class(dataset):
    divided = {}
    for i in range(len(dataset)):
        row = dataset[i]
        if (row[-1] not in divided):
            divided[row[-1]] = []
        divided[row[-1]].append(row)
    return divided


# In[28]:

def get_summary(rows_by_class):
    summary = [(mean(attribute), std(attribute)) for attribute in zip(*rows_by_class)]
    del summary[-1]
    return summary


# In[29]:

def summarize_by_class(dataset):
    separated = divide_on_class(dataset)
    summaries = {}
    for class_value in separated:
        instances = separated[class_value]
        summaries[class_value] = get_summary(instances)
    return summaries


# In[30]:

def probability(x, mean, std):
    e = math.exp(-(math.pow(x-mean,2)/(2*math.pow(std,2))))
    return (1 / (math.sqrt(2*math.pi) * std)) * e


# In[31]:

def get_class_probablities(summaries,row):
    probabs = {}
    for class_value, class_summary in summaries.items():
        probabs[class_value] = 1
        for i in range(len(class_summary)):
            mean, std = class_summary[i]
            x = row[i]
            probabs[class_value] *= probability(x, mean, std)
    return probabs


# In[32]:

def predict(summaries, row):
    probabs = get_class_probablities(summaries, row)
    l, p = None, -1
    for class_value, probab in probabs.items():
        if l is None or probab > p:
            p = probab
            l = class_value
    return l


# In[33]:

def get_predications(summaries,dataset):
    predictions = []
    for i in range(len(dataset)):
        result = predict(summaries, dataset[i])
        predictions.append(result)
    return predictions
    


# In[34]:

def accuracy(dataset, predictions):
    correct_predictions = 0
    for i in range(len(dataset)):
        if dataset[i][-1] == predictions[i]:
            correct_predictions += 1
    return (correct_predictions/float(len(dataset))) * 100.0


# In[35]:

def demo(filename,split_ratio):
    dataset = read_csv_data(filename)
    train,test = split_dataset(dataset,split_ratio)
    summaries = summarize_by_class(train)
    predictions = get_predications(summaries,test)
    print('Accuracy: ',accuracy(test,predictions))


# In[36]:

demo('diabetes.csv',0.5)


# In[ ]:




# In[ ]:



