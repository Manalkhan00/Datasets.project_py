#!/usr/bin/env python
# coding: utf-8

# # Exo-planets Dataset

# In[41]:


import pandas as pd


# # Rows method

# In[44]:


df = pd.read_csv('exoplanet_confirm_and_candidates.csv')

#calling out the first 15 rows

print(df.head(15))


# # COLUMNS METHOD
# 
# 

# In[60]:


for col in df.columns: 
    print(col)
    


# In[33]:


#method 2 for accessing columns
columns = ["name","planet_status", "mass","non-null","float64","mass_error_min","mass_error_max","mass_sini","mass_sini_error_min" ,"mass_sini_error_max" ,"radius" , "radius_error_min" , "radius_error_max" , "orbital_period" , "orbital_period_error_min", "orbital_period_error_max"  ,"semi_major_axis"]

#Accessing columns through list,also it can be done through dictionary,tuples etc too
   
print(list(df.columns))


# In[34]:


#METHOD 3

(df.columns)


# In[38]:


df.rename(columns={"name" : "NAMES"})


# # Data information

# In[7]:


print(df.info())


# In[9]:


df.shape


# In[57]:


import pandas as pd
df = pd.read_csv("exoplanet_confirm_and_candidates.csv")

print(df.dropna(inplace = True))
(df.head(16))


# In[58]:


df = pd.read_csv("exoplanet_confirm_and_candidates.csv")
print(df.fillna(98, inplace = True))
(df.head(16))


# In[30]:


#IF THE VALUES ARE NULL IN THE DATASET IT WILL RETURN TRUE OTHERWISE FALSE

df.isnull()


# In[29]:


df.isnull().sum()


# # Changing the values of a specified column

# In[48]:


import pandas as pd


df = pd.read_csv('exoplanet_confirm_and_candidates.csv')
print(df["radius"].fillna(55, inplace = True))
print(df["radius_error_min"].fillna(60, inplace = True))
(df.head(16))


# In[56]:


#dropna() function can also remove the specific empty values from the columns.


df.dropna(subset=['star_age'], inplace = True)
(df.head(16))


# # WAYS OF REMOVING WRONG DATA FROM THE COLUMN
# 
# 
# #Correcting the wrong data from the column value.

# In[27]:




df.loc[7, 'mass_error_min'] = 4.5
df.loc[2, 'mass_error_min'] = 3.5
print(df.head(16))


# # To replace wrong data for larger data sets, e.g. set boundaries for legal values, and replace any values that are outside of the boundaries.
# 
# 

# In[33]:


for x in df.index:
  if df.loc[x, "star_age_error_min"] > 3:
    df.loc[x, "star_age_error_min"] = 3
    
print(df.head(16))


# In[34]:


#IF THE VALUES ARE DUPLICATED IN THE DATASET IT WILL RETURN TRUE OTHERWISE FALSE

print(df.duplicated())
print(df.head(16))


# In[36]:


#The corr() method calculates the relationship between each column in your data set.

df.corr()
df.head(16)

