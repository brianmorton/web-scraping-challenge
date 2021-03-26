#!/usr/bin/env python
# coding: utf-8

# In[1]:
def scrape():

#imports
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[11]:


#Part 1
#soup set up

url1 = 'https://mars.nasa.gov/news/'
html = requests.get(url1).text
soup = bs(html, 'html.parser')


# In[12]:


#part 1 Section 1
#first news story headline variable storage

newstitle = soup.find(class_ = "content_title" ).text.strip()
print(newstitle)

#first news story description variable storage
newsdescription = soup.find(class_ = 'rollover_description_inner')
newsdescription = newsdescription.text.strip()
print(newsdescription)


# In[21]:


#Part 1 Section 2
# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
featured = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
#Launch splinter and click in
url2 = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

browser.visit(url2)
browser.links.find_by_partial_text('FULL IMAGE').click()

#b-soup request object                             
html = browser.html

#pass request object
souptest = bs(html, 'lxml')

#insert div class to search
ref = souptest.find(class_ = 'fancybox-image')['src']


featured_image_url = featured + ref


print('featured_image_url print: ', featured_image_url)



# tag: fancybox-image, fancybox-skin, fancybox-inner
#featured_image_url = souptest.find(class_ = 'headerimage')['src']

#close browser object
browser.quit()


# In[9]:


#hardcoded if no other option
featured = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/


# In[13]:


#Part 1 Section 3

### Mars Facts
url3 = 'https://space-facts.com/mars/'

read = pd.read_html(url3)

dftable = read[1]

dftable = dftable.drop(['Earth'], axis=1)
dftable
# Use Pandas to convert the data to a HTML table string.
html_table = dftable.to_html()
html_table


# In[18]:


#Part 1 Section 4

### Mars Hemispheres

#* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 
#to obtain high resolution images for each of Mar's hemispheres.

#b-soup to pull titles from images
url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
html = requests.get(url4).text
soup3 = bs(html, 'html.parser')
          
hemindex = soup3.find_all('h3')

Cerebus_title = hemindex[0].text.strip()
print(Cerebus_title)


Schiaparelli_title = hemindex[1].text.strip()
print (Schiaparelli_title)


Syrtis_Major_title = hemindex[2].text.strip()
print (Syrtis_Major_title)


Valles_Marineris_title = hemindex[3].text.strip()
print (Valles_Marineris_title)


# In[27]:


#Splinter portion section 4
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


browser.visit(url4)
browser.links.find_by_partial_text('Cerberus ').click()
#browser.links.find_by_partial_text('Sample').click()

#b-soup request object                             
html = browser.html

#pass request object
soupurl = bs(html, 'lxml')

                    #element to search for
Cerebus_url = soupurl.find(class_ = 'thumb')['href']



#close browser object
browser.quit()


print(Cerebus_url)    


# In[ ]:


browser.visit(url4)
browser.links.find_by_partial_text('Schiaparelli ').click()
#browser.links.find_by_partial_text('Sample').click()

#b-soup request object                             
html = browser.html

#pass request object
soupurl = bs(html, 'lxml')

                    #element to search for
Schiaparelli_url = soupurl.find(class_ = 'thumb')['href']



#close browser object
browser.quit()


print(Cerebus_url)    


# In[ ]:


browser.visit(url4)
browser.links.find_by_partial_text('Syrtis Major ').click()
#browser.links.find_by_partial_text('Sample').click()

#b-soup request object                             
html = browser.html

#pass request object
soupurl = bs(html, 'lxml')

                    #element to search for
Syrtis_url = soupurl.find(class_ = 'thumb')['href']



#close browser object
browser.quit()


print(Cerebus_url)    


# In[ ]:


browser.visit(url4)
browser.links.find_by_partial_text('Valles Marineris ').click()
#browser.links.find_by_partial_text('Sample').click()

#b-soup request object                             
html = browser.html

#pass request object
soupurl = bs(html, 'lxml')

                    #element to search for
Valles_url = soupurl.find(class_ = 'thumb')['href']



#close browser object
browser.quit()


print(Cerebus_url)    


# In[26]:


###############hardcoded urls placeholders###############
Cerebus_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
Schiaparelli_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
Syrtis_url =  'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
Valles_url =   'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'


#append above variables to list with dict object
hemisphere_image_urls = []
hemisphere_image_urls.append({'"title"':Cerebus_title, 'img_url':Cerebus_url})
hemisphere_image_urls.append({'"title"':Schiaparelli_title, 'img_url':Schiaparelli_url})
hemisphere_image_urls.append({'"title"':Syrtis_Major_title, 'img_url':Syrtis_url})
hemisphere_image_urls.append({'"title"':Valles_Marineris_title, 'img_url':Valles_url})

