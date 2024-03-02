#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


import requests


# In[3]:


requests.get('http://thisisasite.net/')


# In[4]:


response=requests.get('http://thisisasite.net/')


# In[5]:


response.url


# In[6]:


response.status_code


# In[7]:


response.headers


# In[8]:


response.content


# In[9]:


response.text


# In[10]:


get_ipython().run_line_magic('pip', 'install  bs4')


# In[2]:


from bs4 import BeautifulSoup


# In[4]:


import requests
from bs4 import BeautifulSoup
response=requests.get('http://thisisasite.net/')
response.text
soup=BeautifulSoup(response.text)


# In[5]:


import requests
from bs4 import BeautifulSoup


# In[6]:


response=requests.get('http://thisisasite.net/')


# In[7]:


requests.get('http://thisisasite.net/')


# In[8]:


response=requests.get('http://thisisasite.net/')


# In[9]:


response.content


# In[10]:


from bs4 import BeautifulSoup


# In[11]:


soup=BeautifulSoup(response.text)


# In[12]:


print(soup.prettify())


# In[13]:


soup.find("title")


# In[26]:


soup.find_all("article")


# In[15]:


soup.find_all("article")


# In[17]:


print(soup.find("span",class_="phone").text)


# In[21]:


featured_testimonial=soup.find_all('div',class_='quote')
for testimonial in featured_testimonial:
    print(testimonial.text)


# In[24]:


staff=soup.find_all("div",class_="info col-xs-8 col-xs-offset-2 col-sm-7 col-sm-offset-0 col-md-6 col-lg-8")
for s in staff:
    print(s.text)


# In[25]:


links=soup.find_all("a")
for link in links:
    print(link.text, link.get("href"))


# In[27]:


with open("wisdom.txt","w") as f:
    f.write(soup.prettify())


# In[ ]:




