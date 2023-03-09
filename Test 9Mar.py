#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


titanic=sns.load_dataset("titanic")


# In[3]:


titanic.head()


# In[6]:


import plotly.express as px
import numpy as np


# In[5]:


pip install plotly


# In[7]:


px.scatter(data_frame=titanic,x="age",y="fare")


# Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express.

# In[12]:


tips = sns.load_dataset('tips')


# In[13]:


tips


# In[21]:


df=px.data.tips()


# In[26]:


fig=px.box(df,y="total_bill")
fig.show()


# Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
# the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
# column with the color parameter.

# In[29]:


import plotly.express as px
df=px.data.tips()

fig=px.histogram(df,x="sex",y="total_bill",color="day",pattern_shape="smoker")
fig.show()


# Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
# the color parameter.
# Note: Use "sepal_length", "sepal_width", "petal_length", "petal_width" columns only with the
# dimensions parameter.

# In[31]:


import plotly.express as px
df = px.data.iris()
fig=px.scatter_matrix(df,dimensions=["sepal_length","sepal_width","petal_length","petal_width"],
                      color="species")
fig.show()


# Q5. What is Distplot? Using Plotly express, plot a distplot.

# The displot figure factory display a combination of statistical representing of numerical data,such as histogram,kernel density estimation or normal curve,and rug plot.
# 
# The displot can composed of all or any combination of the following 3 components:-
# a)histogram
# b)curve
# c)rug plot

# In[37]:


import plotly.figure_factory as ff
x=np.random.randn(1000)
hist_data=[x]
group_labels=['distplot']
fig=ff.create_distplot(hist_data,group_labels)
fig.show()


# In[ ]:




