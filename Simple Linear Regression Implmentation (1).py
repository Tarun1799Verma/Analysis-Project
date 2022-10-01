#!/usr/bin/env python
# coding: utf-8

# In[78]:


# importing all needed library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[81]:


df = pd.read_csv('Salary_Data.csv')


# In[82]:


df.head(2)


# In[83]:


# checking for null or mising values
df.isnull().sum()


# In[84]:


# getting genral information about the data
df.info()


# In[85]:


df.describe()


# In[86]:


#checking for normality
import scipy.stats as st
import pylab


# In[87]:


st.probplot(df['YearsExperience'], dist = 'norm', plot = pylab);


# In[21]:


df.skew()


# In[22]:


df.kurt()


# In[33]:


# trying to make data normally distributed
df['YearsExperience'] = df['YearsExperience'].apply(lambda x: np.log(x))


# In[88]:


x = df.drop(columns = ['Salary'])


# In[89]:


y = df['Salary']


# In[90]:


# spliting the data between train and test
from sklearn.model_selection import train_test_split


# In[91]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 123)


# In[92]:


# importing the machine learning algorithm
from sklearn.linear_model import LinearRegression


# In[93]:


# making object 
lr = LinearRegression()


# In[94]:


# training the model
lr.fit(x_train, y_train)


# In[95]:


lr.intercept_


# In[96]:


lr.coef_


# In[97]:


# making prediction
y_pred = lr.predict(x_test)


# In[98]:


y_pred


# In[99]:


# checking Accuracy
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error


# In[100]:


r2_score(y_test, y_pred)


# In[101]:


mean_squared_error(y_test, y_pred)


# In[102]:


mean_absolute_percentage_error(y_test, y_pred)


# In[103]:


# drawing the graph
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred)


# In[ ]:





# In[ ]:




