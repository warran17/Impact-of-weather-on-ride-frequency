#!/usr/bin/env python
# coding: utf-8

# ## Project Description

# _*Project description:*_
#  The task is to find patterns in the available information for Zuber, a new ride-sharing company that's launching in Chicago. Passenger preferences and the impact of external factors on rides are tried to understand.
# A database is studied, analyze data from competitors, and test a hypothesis about the impact of weather on ride frequency.
# 

# ### Step 1. Write a code to parse the data on weather in Chicago in November 2017 from the website:

# ### Step 2. Exploratory data analysis

# ### Step 3. Test the hypothesis that the duration of rides from the the Loop to O'Hare International Airport changes on rainy Saturdays.

# ### Step 4. Exploratory data analysis (Python)

# In[1]:


import pandas as pd
from scipy import stats as st


# In[2]:



company_trips=pd.read_csv('/datasets/project_sql_result_01.csv')
dropoff= pd.read_csv('/datasets/project_sql_result_04.csv')


# In[3]:


print(company_trips.head())
print(dropoff.head())


# In[4]:


print(company_trips.info())


# In[5]:


print(dropoff.info())


# <div class="alert alert-success">
#     The data was loaded and inspected!
# </div>

# In[6]:


top_destination=dropoff.head(11)
print(top_destination)


# In[7]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
width = 0.8  # the width of the bars
df2 = company_trips[:10].copy()

#others
new_row = pd.DataFrame(data = {
    'company_name' : ['others'],
    'trips_amount' : [company_trips['trips_amount'][10:].sum()]
})

#combining top 5 with others
df2 = pd.concat([df2, new_row])
        
    
    

x= df2['company_name']
y=df2['trips_amount']

fig, ax = plt.subplots()
rects1 = ax.bar(x , y, width, label='Men')
ax.set_xticklabels(x, rotation=90, fontdict={'horizontalalignment':'right','size':10});

ax.set_ylabel('trips_amount');
ax.set_title('taxi companies and number of rides plot');
plt.show()



# >'Flash Cab' is the by far the most popular company as it makes 19558 trips on average on November 15-16, 2017 followed by 
# Taxi Affiliation Services at 11422 and Medallion Leasing at 10367.

# In[8]:


width = 0.8  # the width of the bars
df2 = dropoff[:10].copy()

#others
new_row = pd.DataFrame(data = {
    'dropoff_location_name' : ['others'],
    'average_trips' : [dropoff['average_trips'][10:].sum()]
})

#combining top 5 with others
df2 = pd.concat([df2, new_row])
        
    
    

x= df2['dropoff_location_name']
y=df2['average_trips']

fig, ax = plt.subplots()
rects1 = ax.bar(x , y, width, label='Men')
ax.set_xticklabels(x, rotation=90, fontdict={'horizontalalignment':'right','size':10});

ax.set_ylabel('Average Trips');
ax.set_title('Average trips on top 10 neighbourhood');
plt.show()


# >Most taxi trip ended to 'Loop' (10727.46 on average on November 2017. Other most popular neighbourhoods are 'River North' with 9523.66 average trips and 'Streeterville' with  6664.66 average trips.

# <div class="alert alert-success">
#     Top taxi caompanies and dropoff locations were identified successfully. Visualizations are appropriate
# </div>

# ### Step 5. Testing hypotheses (Python)

# > **NULL HYPOTHESIS:** "The average duration of rides from Loop neighborhood to O'Hare International Airport do not changes on 
#     rainy Saturdays."
#     
# 
# > **Alternative Hypothesis:** "The average duration of rides from Loop neighborhood to O'Hare International Airport changes on rainy Saturdays."
# 

# In[9]:


weather_time=pd.read_csv('/datasets/project_sql_result_07.csv')


# In[10]:


print(weather_time.sample(7))


# In[11]:


weather_time['start_ts']=pd.to_datetime(weather_time['start_ts'])
weather_time['day']=weather_time['start_ts'].dt.weekday
Rainy=weather_time[weather_time['weather_conditions']=='Bad']
Sunny=weather_time[weather_time['weather_conditions']=='Good']
print(Rainy.head())
print(Sunny.head())


# In[12]:


print(Rainy['duration_seconds'].mean())
print(Sunny['duration_seconds'].mean())


# In[15]:


alpha=0.05
results_variation = st.ttest_ind(
    Rainy['duration_seconds'],         
    Sunny['duration_seconds'] )

print('p-value:  {:.7f}'.format(results_variation.pvalue))

if (results_variation.pvalue < alpha):
     print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")


# >The average duration of rides from Loop neighborhood to O'Hare International Airport changes on rainy Saturdays.

# ### Conclusion

# * 'Flash Cab' is the by far the most popular company as it makes 19558 trips on average on November 15-16, 2017 followed by Taxi Affiliation Services at 11422 and Medallion Leasing at 10367.
# 
# * Most taxi trip ended to 'Loop' (10727.46 on average on November 2017. Other most popular neighbourhoods are 'River North' with 9523.66 average trips and 'Streeterville' with 6664.66 average trips.
# 
# * The average duration of rides from Loop neighborhood to O'Hare International Airport changes on rainy Saturdays.

# In[ ]:




