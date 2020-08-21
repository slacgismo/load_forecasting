#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import csv
import os 
import scipy.stats
import time
from datetime import datetime as dt
from datetime import timedelta


# In[40]:


input_dir= 'C:/Users/veronikalubeck/Desktop/Census'

os.chdir('/Users/veronikalubeck/Desktop/Census')


# In[37]:


os.chdir('/Users/veronikalubeck/Desktop/Census')
data=pd.read_csv('demand_1.csv', header=0, names=['Timestamp', 'Demand'])
newtimestamp=[]
newdemand=[]

for i in range(data.shape[0]):
    newtimestamp.append(time.strftime('%m/%d/%Y %H:%M',time.strptime(data.Timestamp[i][0:19],'%Y-%m-%d %H:%M:%S')))
    newdemand.append(float(data.Demand[i].replace(' kW','')))


newtimestamp2=pd.DatetimeIndex(newtimestamp)

plt.figure(figsize=(10,6))
plt.plot(newtimestamp2,newdemand)
ax=plt.gca()
formatter = matplotlib.dates.DateFormatter("%m-%d %H:%M")
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30,labelsize=14)

ax.tick_params(axis='both', which = 'major', labelsize=14)
plt.ylabel('Demand (W)', fontsize=14)
plt.grid()


# In[41]:


os.chdir('/Users/veronikalubeck/Desktop/Census')

plt.figure(figsize=(10,6))

demand_matrix=np.zeros((1,1440))

for j in range(1):
    data=pd.read_csv('demand_'+str(j+1)+'.csv',header=0,names=['Timestamp','Demand'])
    
    newtimestamp=[]
    newdemand=[]
                   
    for i in range(data.shape[0]):
        newtimestamp.append(time.strftime('%m/%d/%Y %H:%M',time.strptime(data.Timestamp[i][0:19],'%Y-%m-%d %H:%M:%S')))
        newdemand.append(float(data.Demand[i].replace(' kW','')))
    newtimestamp2=pd.DatetimeIndex(newtimestamp)
    demand_matrix[j,:]=np.array(newdemand)/1000

mean_profile=np.mean(demand_matrix,axis=0)
                        
plt.plot(newtimestamp2,mean_profile)

ax=plt.gca()
formatter = matplotlib.dates.DateFormatter("%m-%d %H:%M")
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30,labelsize=14)

ax.tick_params(axis='both', which = 'major', labelsize=14)
plt.ylabel('Demand (kW)', fontsize=14)
plt.grid()


# In[52]:


print(data.Demand[0])


# In[53]:


print(data.Timestamp[0])


# In[12]:


os.chdir('/Users/veronikalubeck/Desktop/Census')

plt.figure(figsize=(10,6))

demand_matrix=np.zeros((1,1440))

for j in range(1):
    data=pd.read_csv('demand_'+str(j+1)+'.csv',header=0,names=['Timestamp','Demand'])
    
    newtimestamp=[]
    newdemand=[]
                   
    for i in range(data.shape[0]):
        newtimestamp.append(time.strftime('%m/%d/%Y %H:%M',time.strptime(data.Timestamp[i][0:19],'%Y-%m-%d %H:%M:%S')))
        newdemand.append(float(data.Demand[i].replace(' kW','')))
    newtimestamp2=pd.DatetimeIndex(newtimestamp)
    demand_matrix[j,:]=np.array(newdemand)/1000

mean_profile=np.mean(demand_matrix,axis=0)
                        
plt.plot(newtimestamp2,mean_profile)

ax=plt.gca()
formatter = matplotlib.dates.DateFormatter("%m-%d %H:%M")
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30,labelsize=14)

ax.tick_params(axis='both', which = 'major', labelsize=14)
plt.ylabel('Demand (kW)', fontsize=14)
plt.grid()


# In[ ]:




