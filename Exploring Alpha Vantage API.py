#!/usr/bin/env python
# coding: utf-8

# In[8]:


with open("API_key_example.txt") as file:
    api=file.read()
    print(api)


# In[9]:


api=api.strip()


# In[10]:


api


# In[4]:


with open("API_key_example.txt") as file:
    api=file.read()
api=api.strip()
print(api)


# In[5]:


get_ipython().run_line_magic('pip', 'install alpha_vantage')


# In[6]:


from alpha_vantage.timeseries import TimeSeries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io


# In[7]:


tsl=TimeSeries(key=api)


# In[8]:


tsl.get_monthly("AAPL")


# In[9]:


tsl.get_monthly("AAPL")


# In[10]:


tsl.get_intraday("AAPL")


# In[12]:


url='https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey='+str(api)
r=requests.get(url)
data=r.json()
print(data)


# In[13]:


url='https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey='+str(api)
r=requests.get(url)
data=BeautifulSoup(r.content)
print(data)


# In[15]:


url='https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=AAPL&interval=60min&apikey='+str(api)
r=requests.get(url)
data=BeautifulSoup(r.content)
print(data)


# In[4]:


from alpha_vantage.timeseries import TimeSeries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
with open("API_key_example.txt") as file:
    api=file.read()
api=api.strip()

url='https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey='+str(api)+'&datatype=csv'
r=requests.get(url).content
data=pd.read_csv(io.StringIO(r.decode("utf-8")))
print(data)


# In[5]:


data.head(50)


# In[6]:


data.head(20)


# In[9]:


tsl=TimeSeries(key=api)
apple1,meta_data=tsl.get_intraday("AAPL")


# In[10]:


meta_data


# apple1
# 

# In[11]:


apple1


# In[12]:


df_apple1=pd.DataFrame(apple1).transpose().reset_index()
df_apple1.head()


# In[16]:


ts2=TimeSeries(key=api,output_format="pandas")
ts2.get_intraday("AAPL")


# In[17]:


df_apple2,metadata=ts2.get_intraday("AAPL",outputsize="full")


# In[18]:


metadata


# In[19]:


df_apple2.reset_index()


# In[21]:


url='https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=AAPL&interval=60min&apikey='+str(api)
r=requests.get(url)
fd=BeautifulSoup(r.content)
print(fd)


# In[22]:


url='https://www.alphavantage.co/query?function=EARNINGS&symbol=AAPL&interval=60min&apikey='+str(api)
r=requests.get(url)
fd=BeautifulSoup(r.content)
print(fd)


# In[24]:


url='https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=USD&to_symbol=JPY&apikey='+str(api)
r=requests.get(url)
fd=BeautifulSoup(r.content)
print(fd)


# In[25]:


url='https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol=BTC&market=USD&apikey='+str(api)
r=requests.get(url)
fd=BeautifulSoup(r.content)
print(fd)


# In[26]:


url='https://www.alphavantage.co/query?function=REAL_GDP&interval=quarterly&market=USD&apikey='+str(api)
r=requests.get(url)
fd=BeautifulSoup(r.content)
print(fd)


# In[27]:


tsl.get_monthly('MSFT')


# In[ ]:




