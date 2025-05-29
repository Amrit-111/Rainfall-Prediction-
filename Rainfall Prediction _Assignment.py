#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd 


# In[4]:


data = pd.read_csv(r"C:\Users\Amrit\Desktop\Assignment & Working Folder\My Portfilo_Projects\Project_Dataset\austin_weather.csv")
data


# In[5]:


data = data.drop(["Events","Date","SeaLevelPressureLowInches"],axis = 1)


# In[6]:


# will replace the unnecessary data 

data = data.replace('T',0.0)
data = data.replace('_',0.0)
data = data.replace('-',0.0)


# In[7]:


data.to_csv("austin_weather_final.csv")


# In[8]:


# Importing the libraries

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from sklearn.linear_model import LinearRegression


# In[59]:


data =pd.read_csv("austin_weather_final.csv")
data


# In[9]:


X = data.drop(['PrecipitationSumInches'], axis =1 )


# In[10]:


Y = data['PrecipitationSumInches']


# In[11]:


#reshaping it into 2nd vector

Y = Y.values.reshape(-1,1)


# In[12]:


Y


# In[32]:


day_index = 798
days= [ i for i in range(Y.size)]


# In[14]:


# Intialize the linear regression classifier 

clf = LinearRegression()


# In[15]:


clf.fit(X,Y)


# In[23]:


Y = Y.astype(float).flatten()


# In[33]:


# plot a graph

print("The Precipitation trend graph:")

plt.scatter(days,Y,color = 'g')
plt.scatter(days[day_index],Y[day_index],color ='r')
plt.title("Precipitation Level")
plt.xlabel("Days")
plt.ylabel("Precipitation in Inches")
plt.show()
x_vis = X.filter(['TempAvgF','DewPointAvgF','HumidityAvgPercent','SeaLevelPressureAvgInches','VisibilityAvgMiles','WindAvgMPH'])


# In[44]:


print('The precipitation vs Attributes trend graph:')

for i in range(x_vis.columns.size):
    plt.subplot(3, 2, i + 1)
    plt.scatter(days[:100], x_vis[x_vis.columns.values[i]][:100], color='g')   # I'm getting error in this line . 
                                #here I have to put days[:100],otherwise it shows x,y must have same size 
                                #but in video you are using -> plt.scatter(days, x_vis[x_vis.columns.values[i]][:100], color='g') 
    
    plt.scatter(days[day_index], x_vis[x_vis.columns.values[i]][day_index], color='r')
    plt.title(x_vis.columns.values[i])


plt.show()


# In[ ]:




