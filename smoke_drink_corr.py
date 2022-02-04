#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv('LLCP2020.csv', low_memory=False)


# In[12]:


data = data.drop('Unnamed: 0', axis=1)
data=data.dropna()


# In[13]:


drink_smoke_data = data[['_STATE', 'ALCDAY5', 'SMOKDAY2']]


# In[26]:


drink_smoke_data['ALCDAY5']= drink_smoke_data['ALCDAY5'].str.replace('   ','0')


# In[27]:


drink_smoke_data['ALCDAY5'] = drink_smoke_data['ALCDAY5'].astype(int)


# In[34]:


drink_smoke_data['ALCDAY5'].unique()


# In[37]:


drink_smoke_data['ALCDAY5']=drink_smoke_data[['ALCDAY5']].replace(888,0)


# In[39]:


drink_smoke_data['ALCDAY5']= drink_smoke_data['ALCDAY5'].replace(101,1)


# In[41]:


for i in [208, 203, 205, 201, 222, 103, 212, 102, 107, 204,
       101, 215, 999, 228, 230, 104, 210, 225, 206, 202, 777, 220, 227,
       207, 105, 229, 214, 106, 209, 216, 221, 218, 226, 224, 213, 211,
       217, 223, 219]:
    drink_smoke_data['ALCDAY5'] = drink_smoke_data['ALCDAY5'].replace(i,1)


# In[43]:


drink_smoke_data['ALCDAY5'].unique()


# In[53]:


drink_smoke_data['SMOKDAY2']= drink_smoke_data['SMOKDAY2'].str.replace(' ','0')
drink_smoke_data['SMOKDAY2']= drink_smoke_data['SMOKDAY2'].str.replace('3','0')
drink_smoke_data['SMOKDAY2']= drink_smoke_data['SMOKDAY2'].str.replace('9','0')
drink_smoke_data['SMOKDAY2']= drink_smoke_data['SMOKDAY2'].str.replace('7','0')
drink_smoke_data['SMOKDAY2']= drink_smoke_data['SMOKDAY2'].str.replace('2','1')


# In[54]:


drink_smoke_data['SMOKDAY2'].unique()


# In[56]:


drink_smoke_data['SMOKDAY2'] = drink_smoke_data['SMOKDAY2'].astype(int)


# In[105]:


drink_smoke_data.columns=['FIPS', 'Alcohol', 'Smoke']


# In[138]:


grouped_data1 = drink_smoke_data.groupby('FIPS').sum()


# In[139]:


grouped_data2 = drink_smoke_data.groupby('FIPS').count()


# In[142]:


grouped_data1['Drinker percentage'] = grouped_data1['Alcohol']/grouped_data2['Alcohol']  


# In[143]:


grouped_data1['Smoker percentage'] = grouped_data1['Smoke']/grouped_data2['Smoke']


# In[145]:


grouped_data = grouped_data1


# In[146]:


grouped_data.reset_index(inplace=True);


# In[147]:


grouped_data['FIPS']=grouped_data['FIPS'].astype(int)


# In[148]:


state_code= pd.read_csv('state_code.csv')


# In[149]:


total_data=pd.merge(grouped_data, state_code, on = 'FIPS', how='inner')


# In[153]:


total_data.head()


# In[150]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[154]:


plot=sns.regplot(x='Drinker percentage', y = 'Smoker percentage', data = total_data)
#plot.set(xlim=(700,9000))
plot.set(title='Number of Smoker vs Number of Drinker')
plt.savefig('output.png', dpi=300)


# In[124]:


url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
state_data = pd.read_csv(state_unemployment)


# In[127]:


total_data.head()


# In[128]:


import folium


# In[158]:


map1 = folium.Map(location=[48, -105], zoom_start=3)
folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=total_data,
    columns=["Postal Code", "Drinker percentage"],
    key_on="feature.id",
    fill_color="RdBu",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name="Number of active drinkers (%)",
).add_to(map1)

#folium.LayerControl().add_to(map1)

map1


# In[165]:


map1 = folium.Map(location=[48, -105], zoom_start=3)
folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=total_data,
    columns=["Postal Code", "Smoker percentage"],
    key_on="feature.id",
    fill_color="RdBu",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name="Number of active smokers (%)",
).add_to(map1)

#folium.LayerControl().add_to(map1)

map1


# In[164]:


total_data[(total_data['Smoker percentage'] < 0.1)&(total_data['Drinker percentage'] < 0.35)]


# In[168]:


map1.save('drinkers_map')


# In[166]:


import io
from PIL import Image


# In[167]:


img_data = map1._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('image1.png')

img_data = map2._to_png(5)
img = Image.open(io.BytesIO(img_data))
img.save('image2.png')


# In[ ]:




