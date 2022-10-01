#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import seaborn as sns


# In[4]:


import numpy as np


# In[5]:


df = sns.load_dataset('titanic')


# In[6]:


df.isnull().sum()


# In[8]:


df['age'].fillna(df['age'].median(), inplace = True)


# In[9]:


df['age'].isnull().sum()


# In[10]:


df.drop(columns = ['deck', 'embark_town'], inplace = True)


# In[11]:


df.info()


# In[12]:


df['embarked'].mode()


# In[13]:


df['embarked'].fillna(df['embarked'].mode()[0], inplace = True)


# In[14]:


df['embarked'].isnull().sum()


# In[15]:


# drawing useful information by appling condition on dataframe


# In[16]:


df


# In[17]:


df.shape


# In[18]:


# analysing first column (survived)
# how many survived or how many not
survive = df['survived'].value_counts()
survive


# In[19]:


print("survived", survive[0]/891 *100)
print('Not Survived', survive[1]/891 * 100)


# In[20]:


# analyzing second column (pclass or passanger class)
df['pclass'].value_counts()


# In[21]:


a = df['pclass'].value_counts()
print('first', a[1]/891*100)
print('second', a[2]/891*100)
print('third', a[3]/891*100)


# In[22]:


# analzing third column
df['sex'].value_counts()


# In[23]:


b = df['sex'].value_counts()


# In[24]:


print('women', b['female']/ 891 *100)
print('men', b['male']/ 891 *100)


# In[25]:


df['age'].describe()


# In[26]:


a = (df['age'] < 50).value_counts()
a


# In[27]:


a = (df['age'] < 18).value_counts()
a


# In[28]:


df['sibsp'].value_counts()


# In[29]:


df['parch'].value_counts()


# In[30]:


# analyzing fare column


# In[31]:


df['fare'].describe()


# In[32]:


df['fare'].mode()


# In[33]:


a = df['fare']> 100
a.value_counts()


# In[34]:


a = df['fare']> 100
a.value_counts()


# In[35]:


df['embarked'].value_counts()


# In[36]:


df['who'].value_counts()


# In[37]:


df['alive'].value_counts()


# In[38]:


df['alone'].value_counts()


# In[39]:


a = df[(df['alone'] == True) & (df['alive'] == 'yes')]
len(a)


# In[40]:


# survived + pclass
a = df[(df['survived'] == 1) & (df['pclass'] == 1)]


# In[41]:


# survival percent of first class
len(a) / 216 * 100


# In[42]:


# survival percent of second class
a = df[(df['survived'] == 1) & (df['pclass'] == 2)]


# In[43]:


len(a) / 184 * 100


# In[44]:


# survival percent of third class
a = df[(df['survived'] == 1) & (df['pclass'] == 3)]


# In[45]:


len(a) / 491 * 100


# In[46]:


# survived + sex
a = df[(df['sex'] == 'female') & (df['survived'] == 1)]
len(a)


# In[47]:


len(a) / 342 * 100


# In[48]:


a = df[(df['sex'] == 'male') & (df['survived'] == 1)]
len(a)


# In[49]:


len(a) / 577 


# In[50]:


len(a) / 342 


# In[51]:


# survived + age
# minimum age survived
df[(df['survived'] == 1) & (df['age'] == 0.42) ]


# In[52]:


# maximum age survived
df[(df['survived'] == 1) & (df['age'] == 80) ]


# In[53]:


# most of the people who survived were young
df[(df['survived'] == 1)]['age'].mean()


# In[54]:


df[(df['survived'] == 1)]['age'].describe()


# In[55]:


df[(df['survived'] == 1) & (df['age'] < 15)].count()


# In[56]:


# survived + fare
df[(df['survived'] == 1) & df['fare'] >]


# In[57]:


df[(df['survived'] == 1) & (df['fare'] < df['fare'].mean())].count()


# In[58]:


a = df['fare'] > 32
a.value_counts()


# In[59]:


df[(df['survived'] == 1) & (df['fare'] > 500 )].count()


# In[60]:


# survive + Embarked


# In[61]:


df[(df['survived'] == 1) & (df['embarked'] == 'S')].count()


# In[62]:


df[(df['survived'] == 1) & (df['embarked'] == 'C')].count()


# In[63]:


df[(df['survived'] == 1) & (df['embarked'] == 'Q')].count()


# In[64]:


a = (df['embarked'] == 'Q').value_counts()


# In[65]:


df[(df['embarked'] == 'C')]['fare'].mean()


# In[66]:


df[(df['embarked'] == 'S')]['fare'].mean()


# In[67]:


df[(df['embarked'] == 'Q')]['fare'].mean()


# In[68]:


df


# In[81]:





# In[82]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




