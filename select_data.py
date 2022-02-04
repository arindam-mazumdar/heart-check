#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv('LLCP2020.csv', low_memory=False)


# In[15]:


data = data.drop('Unnamed: 0', axis=1)


# In[22]:


data=data.dropna()


# In[24]:


data['IMONTH'].astype(int)


# In[28]:


np.array(data.columns)


# In[43]:


#data.drop(list(data[data['MARITAL'] == ' '].index))


# In[56]:


data_MICHD=data.drop(list(data[data['_MICHD']==' '].index))


# In[80]:


data_short=data[['_STATE','_MICHD','CVDCRHD4', 'SMOKE100', 'SMOKDAY2', 'STOPSMK2', 'LASTSMK2','USENOW3', 'LCSFIRST', 'LCSLAST', 'LCSNUMCG', '_SMOKER3','_RFSMOK3']]


# In[71]:


data_MICHD['_MICHD'].astype(int).hist() 


# In[83]:


data_short.to_csv('heart_smoke.csv')


# In[84]:


data_short2=data[['DIABAGE3','']] 


# In[85]:


data_short2


# # Create data file for cigarte tax from all the collected files 

# In[30]:


import datetime as dt


# In[2]:


df_all_time = pd.read_csv('cig_tax_2002-22.csv')


# In[72]:


df_all_time.head()


# In[10]:


df_all_time['Pack of 20'] = df_all_time['Pack of 20'].str.replace('$','')


# In[28]:


df_all_time = df_all_time[df_all_time['Date'] != '--'].


# In[52]:


df_all_time=df_all_time.reset_index(drop=True);


# In[55]:


df_all_time['Date'] = df_all_time['Date'].str.replace('/21','/2021')


# In[59]:


years = [dt.datetime.strptime(df_all_time.loc[i,'Date'], '%m/%d/%Y').year for i in range(len(df_all_time))]


# In[63]:


years = np.array(years)


# In[89]:


df_all_time['Year'] = years


# In[67]:


yr_range=list(range(years.min(),years.max()))


# In[84]:


df_all_time.columns=['State', 'increase', 'Pack of 20', 'Date']


# In[88]:


tax_all=pd.DataFrame({'State':df_all_time['State'].unique()})


# In[123]:


for year in yr_range:
    list1=[]
    for i in range(len(tax_all)):
        l =0
        for k in range(len(df_all_time)):
            if df_all_time.loc[k,'State'] == tax_all.loc[i,'State']:
                if df_all_time.loc[k,'Year'] == 2005 and l==0 :
                    list1.append(df_all_time.loc[k,'Pack of 20'])
                    l+=1
                elif l == 0:
                    list1.append(np.nan)
                    l +=1
                elif l >0 and df_all_time.loc[k,'Year'] == 2005:
                    list1=list1[:-1]
                    list1.append(df_all_time.loc[k,'Pack of 20'])
    tax_all[str(year)]=list1


# In[125]:


#tax_all.head()


# In[126]:


df_2011 = pd.read_csv('cig_tax_2011.csv')
df_2015 = pd.read_csv('cig_tax_2015.csv')
df_2021 = pd.read_csv('cig_tax_2021.csv')


# In[127]:


df_2011.head()


# In[143]:


set(tax_all['State'])


# In[144]:


set(df_2011['State'])


# In[ ]:




