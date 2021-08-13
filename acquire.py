#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np


# In[23]:


import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[ ]:





# In[26]:


import os

def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  


# In[66]:


def get_iris_data():
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        iris = pd.read_sql('SELECT * FROM measurements JOIN species on species.species_id = measurements.species_id', get_connection('iris_db'))
        iris = iris.loc[:,~iris.columns.duplicated()]
        iris = iris.drop(columns=['measurement_id'])

        # Write that dataframe to disk for later. Called "caching" the data for later.
        iris.to_csv(filename)

        # Return the dataframe to the calling code
        return iris  

