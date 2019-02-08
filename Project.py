
# coding: utf-8

# 
# # Project: Investigate Dataset of Appointments Set for Nearby Hospitals
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis & Conclusion</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# Libraries such as pandas, numpy, matplotlib and seaborn are imported.Data from 'noshoowappointments.csv' consisting of appointments set for a hospital is loaded.The data consists of patient Id, appoinment Id, gender of patient, the day when appointment was scheduled,appointment day,age,neighbourhood,whether scholarship was given, disease, whether SMS was recieved and whether they turned up for the appointment.

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


df=pd.read_csv('noshowappointments.csv')
df.head()


# The number of rows,columns of the dataset along with datypes and statistics of each column are found out.

# In[27]:


df.shape


# In[48]:


pd.to_datetime(df['AppointmentDay'])
df['month']=df['AppointmentDay'].dt.month
df.head()


# In[29]:


df.dtypes


# In[30]:


df.describe()


# From the statistics one can note that the mean age of the patient is around 37, majority of them are between 18 and 55.Fewer people got scholarship and most patients suffer from hipertension.

# <a id='wrangling'></a>
# ## Data Wrangling

# An attempt was made to find out the null values and duplicates.The column 'SMS_recieved' is dropped since it is not going to be used in analyzing the data.

# In[31]:


df.info()


# In[32]:


df.nunique()


# In[33]:


sum(df.duplicated())


# There are no null values and duplicate values.

# In[49]:


df.drop(['SMS_received'],axis=1)
df.head()


# <a id='eda'></a>
# ## Exploratory Data Analysis & Conclusion

# The overall dataframe has been plotted.

# In[28]:


df.hist(figsize=(25,15))


# 
# ### Research Question 1 (What is the number of people showing up for the appointment?)

# In[9]:


df1=df['No-show'].value_counts().plot(kind='bar',figsize=(8,10),title='no.people showing up for appointment')
df1.set_xlabel('no-show')
df1.set_ylabel('count')


# It has been found out that nearly 5 times the number of people were absent for the scheduled appointment compared to number of people who were present.   

# 
# ### Research Question 2 (What is the total number of patients suffering from Hipertension)

# In[30]:


Hipertension_patient=df['Hipertension'].sum()
Hipertension_patient


# 21801 people suffer from hipertention.

# 
# ### Research Question 3 (What is the statistics of total number of scholarship given to patients from different neighbourhood?)
# 

# In[42]:


df.groupby('Neighbourhood').sum().Scholarship.describe()


# Each neighbourhood is granted an average of 100 scholorships

# 
# ### Research Question 4 (What is the total number of each type of patients showing up for appointments?)

# In[21]:


def app_y():
    if element in df[df['No-show']=="Yes"]:
        return df
app_y().describe()


# In[23]:


app_y().iloc[:,8:12].sum()


# Given that the patients show up for the appointment, the most number of patients suffer from hipertention and the least are handicapped.Patients who are granted scholarship have got higher probability of turning up for the appoitment 

# 
# ### Research Question 5 (Which neighbourhood has got maximum number of patients turning up for appointments?)

# In[25]:


app_y()['Neighbourhood'].max()


# The maximum number of patients who turn up for the appointment are from 'VILA RUBIM' 

# 
# ### Research Question 6 (What is the total number of scholarships granted for people of different age sector?)

# In[36]:


bin_edges=[0,30,60,90,120]
bin_names=['young','middle-aged','old','v.old']
df['Age seg']=pd.cut(df['Age'],bin_edges,labels=bin_names)
df.head()


# In[37]:


age_scholarship=df.groupby('Age seg').sum().Scholarship
age_scholarship


# In[38]:


df_plot_schol=age_scholarship.plot(kind='bar',title='Scholorship')
df_plot_schol.set_xlabel('Age seg')
df_plot_schol.set_ylabel('frequency')


# Young patients have got the highest scholarships.

# 
# ### Research Question 7 (What is the total number of diabetic patients of different age sector?)

# In[39]:


age_diab=df.groupby('Age seg').Diabetes.sum()


# In[40]:


df_plot_diab=age_diab.plot(kind='bar', title='Age of diabetic patient')
df_plot_diab.set_xlabel('age seg')
df_plot_diab.set_ylabel('frequency')


# Old patients between the age of 60 to 90 suffer from diabetes the most.

# ### Research Question 8 (What is the correlation between various columns of dataset?)

# In[20]:


df.corr()


# In[18]:


#cols=[4,5,6]
#df=df[df.columns[cols]]
corr=df.corr()
plt.figure(figsize=(10,60))
plt.matshow(corr,fignum=1)
plt.xticks(range(len(corr.columns)), corr.columns);
plt.yticks(range(len(corr.columns)), corr.columns);


# Age is positively correlated to all diseases(i.e. with increase in age there is higher chance of suffering from a disease).Age is negatively correlated to scholarship(i.e the yonger lot has higher chance of getting a scholarship)
