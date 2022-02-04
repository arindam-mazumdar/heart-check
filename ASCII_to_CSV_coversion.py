#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd


# In[2]:


data= open('LLCP2020.asc', 'r')


# In[3]:


dr = data.read()


# In[ ]:


form = pd.read_csv(../'format.csv')


# In[32]:


form.columns=['Start_Col, Var_Name, Length]


# In[47]:


array_name=['array_'+str(form.loc[i,'Var_Name']) for i in range(len(form))]


# In[52]:


dr_lines=dr.split('\n');


# In[63]:


array_name[0]=[dr_lines[j][form.loc[0,'Start_Col']-1:form.loc[0,'Start_Col']-1+form.loc[0,'Length']] for j in range(len(dr_lines))]
table = pd.DataFrame({str(form.loc[0,'Var_Name']):array_name[0]})


# In[81]:


for i in range(1,len(form)):
    array_name[i]=[dr_lines[j][form.loc[i,'Start_Col']-1:form.loc[i,'Start_Col']-1+form.loc[i,'Length']] for j in range(len(dr_lines))]
    table[str(form.loc[i,'Var_Name'])]=array_name[i]


# In[83]:


table.to_csv('LLCP2020.csv')


# In[82]:


table.head()


# In[ ]:




