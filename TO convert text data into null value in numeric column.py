#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[15]:


df=pd.read_csv('F:\salary.csv')


# In[16]:


df.head()


# In[17]:


print(df)


# In[18]:


type(df)


# In[19]:


# TO convert text data into null value in numeric column
import re


# In[22]:


df['Salary'].replace(regex=True,inplace=True,to_replace=r'\D',value=r' ')


# In[23]:


print(df)


# In[27]:


df.isnull().sum()


# In[ ]:




