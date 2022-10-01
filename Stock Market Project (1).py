#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_excel('Indian stock market final sheet Part 1.xlsx')


# In[162]:


df.head(3)


# In[8]:


# Task one - Firstly, screen the companies and visualise them according to sub-sectors using a pie chart
# or a bar charts.


# In[160]:


df['Sub-Sector'].isna().sum()


# In[ ]:


# How to fill null value for the Sub-Sector column


# In[259]:


a = pd.DataFrame(df['Sub-Sector'].value_counts())
a


# In[161]:


# can unique and value count of column can be of different numbers


# In[9]:


len(df['Sub-Sector'].value_counts())


# In[8]:


a = df['Sub-Sector'].unique()
len(a)


# In[277]:


plt.figure(figsize = (10, 10))
plt.pie(a['Sub-Sector'], labels = a.index, autopct = "%.2f");


# In[278]:


a1 = a.index


# In[ ]:





# In[ ]:


# Secondly, visualise the companies by segregating them according to Market Cap in
# three categories: Large Cap(>20,000 crore), Mid Cap (5,000 to 20,000 crore) &
# Small Cap(<5,000).


# In[ ]:


# how to make a new column in the data frame based on the condition on any exiting column


# In[167]:


df.head(3)


# In[365]:


large = 'large'
mid = 'mid'
small = 'small'


# In[366]:


for i in range(len(a)):
    if a[i] > 20000:
        size.append(large)
    elif a[i] < 20000 and a[i] > 5000:
        size.append(mid)
    else:
        size.append(small)
        


# In[367]:


df['size'] = size


# In[368]:


plt.figure(figsize = (10, 10))
plt.pie(df['size'].value_counts(), labels = df['size'].unique(), autopct = '%.2f');


# In[369]:


# 3 Thirdly, pick 10 random companies from the entire group and visualise the following
#through a line chart
#Find the Intrinsic Value of the company based on 3 cases of growth (g): Assume
# 3 Cases for g (Growth) : Good (15% Growth) ; Bad (-5% Growth); Best (25%Growth)
# Visualise these 10 companies on a line chart for all 3 cases of growth going
# forward against its current market cap.


# In[250]:


# choosing 10 random company
random_10 = df.iloc[np.random.randint(1, 50, 10)]


# In[370]:


'''V : Intrinsic Value
EPS : The Company’s last 12 month earnings per share
8.5 : The constant represents the appropriate P-E ratio for a no-growth
 company as proposed by Graham.
g : The company's long-term (five years) earnings growth estimate
6 : The average Return of FDs (6%)
Y : The current yield on AAA corporate bonds.
'''


# In[280]:


random_10.head(2)


# In[329]:


random_10['Goodins'] = random_10['Earnings Per Share'] * (8.5 + (2 * g1) * 6 / 7.45)


# In[333]:


random_10['Badins'] = random_10['Earnings Per Share'] * (8.5 + (2 * g2) * 6 / 7.45)


# In[334]:


random_10['Greatins'] = random_10['Earnings Per Share'] * (8.5 + (2 * g3) * 6 / 7.45)


# In[336]:


random_10['Total_no_of_share'] = random_10['Market Cap'] / random_10['Close Price']


# In[338]:


random_10['15% Growth Rate'] = random_10['Total_no_of_share'] * random_10['Goodins']


# In[339]:


random_10['-5% Growth Rate'] = random_10['Total_no_of_share'] * random_10['Badins']


# In[340]:


random_10['25% Growth Rate'] = random_10['Total_no_of_share'] * random_10['Greatins']


# In[375]:


tcs = random_10.head(1)
ran = [2022, 2027]


# In[376]:


plt.figure(figsize = (5, 5))
plt.plot(ran, [tcs['Market Cap'], tcs['15% Growth Rate']], label = '15% Growth Rate')
plt.plot(ran, [tcs['Market Cap'], tcs['-5% Growth Rate']], label = '-5% Growth Rate')
plt.plot(ran, [tcs['Market Cap'], tcs['25% Growth Rate']], label = '25% Growth Rate')

plt.xlabel('year')
plt.ylabel('Market Cap')

plt.title('Simple plot')

plt.legend() # it gives the small box at the left side for describing the graph variable

plt.show()


# In[353]:





# In[4]:


plt.figure(figsize = (10, 10))
sns.countplot(x='Sub-Sector', data = df)


# In[ ]:




