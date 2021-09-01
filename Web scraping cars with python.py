#!/usr/bin/env python
# coding: utf-8

# # Web Scraping  with python--- Jean Carlos Vitola Cabarcas
# link:https://www.cars.com/ 
# Recuerde ejecutar cada celda en su orden, sino le puedo arrojar error  de varibale no definida
# 
# ![image.png](attachment:image.png)
# 

# ### 1) Importamos los módulos 
# 

# In[18]:


from bs4 import BeautifulSoup #pip install BeautifulSoup
import requests    #pip install requests
import pandas as pd  # pip install pandas , # pip install numpy


# ### 2) Petición HTTP GET

# In[19]:


# Dirección la cual queremos escrapear
url="https://www.cars.com/shopping/results/?stock_type=cpo&makes%5B%5D=toyota&models%5B%5D=&list_price_max=&maximum_distance=20&zip="


# ### 2.1 Get Requests

# In[20]:


#objeto response para hacer la petición
response=requests.get(url)


# ### 2.2 Status code

# In[21]:


response.status_code   # si  la salida es response 200(petición get con exito), 500 Servidor time our, 403 protección de scraper


# ### 3) Objeto Soup

# In[22]:


soup= BeautifulSoup(response.content,"html.parser")  #el objeto soup nos permite usar los atributos para sacar las variables de interrres


# In[11]:


soup # contenido de Html como estructura de  arból


# ![image.png](attachment:image.png)
# 

# ### Results

# In[23]:


#Inspecciono el elemento que quiero parsear como contenedor 
results= soup.find_all("div",{"class":"vehicle-card-main"})
results


# In[24]:


object=results[0]


# ### Price

# In[25]:



object.find("span",{"class":"primary-price"}).get_text()


# ### Name
# 

# In[26]:


object.find("h2").text


# ### Mileage

# In[27]:


object.find("div",{"class":"mileage"}).text


# ### Rating

# In[28]:


object.find("span",{"class":"sds-rating__count"}).text


# ### Dealer-name

# In[29]:


object.find("div",{"class":"dealer-name"}).text.strip()


# ### Review

# In[30]:


object.find("span",{"class":"sds-rating__link sds-button-link"}).text


# ### Image

# In[31]:


object.find("img")["src"]


# ### Url

# In[32]:


object.find("a")["href"]


# ### For-Loop

# In[33]:


name=[]
mileage=[]
dealer_name=[]
rating=[]
price=[]
img=[]
url=[]
jean="https://www.cars.com/"  # identificando el arbol, se observa que el link tiene una parte oculta de dirección


for result in results:
    try:
        name.append(result.find("h2").get_text())
        mileage.append(result.find("div",{"class":"mileage"}).text)
        dealer_name.append(result.find("div",{"class":"dealer-name"}).text.strip())
        rating.append(result.find("span",{"class":"sds-rating__count"}).text)
        price.append(result.find("span",{"class":"primary-price"}).get_text())
        img.append(object.find("img")["src"])
        url.append(jean + (object.find("a")["href"]))
        
    except: 
        name.append("n/a")
        mileage.append("n/a")
        dealer_name("n/a")
        rating.append("n/a")
        price.append("n/a")
        img.append("n/a")
        url.append("n/a")
    
   
    
   
   


# ### Create DataFrame

# In[34]:


cars_sales=pd.DataFrame({"Name":name,"Mielage":mileage,"dealer_name":dealer_name,"Rating":rating,"Price":price,"Img":img,"Url":url})


# In[35]:


cars_sales


# ### output Excel
#     
#     
#     
#     
#     
#     

# In[36]:


cars_sales.to_excel("cars_sales.xlsx", index=False)


# ### Pagination

# In[37]:


name=[]
mileage=[]
dealer_name=[]
rating=[]
price=[]
img=[]
urlx=[]


for i in range(1,30):
    
    #1) identificar rango de la paginación Variable del sitio
    url= 'https://www.cars.com/shopping/results/?page=' + str(i)+'&page_size=20&dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=toyota&maximum_distance=20&mileage_max=&sort=best_match_desc&stock_type=cpo&year_max=&year_min=&zip='

    #Petición HTTP con requests
    response=requests.get(url)
    
    # Isntancio el objeto de BS
    soup= BeautifulSoup(response.content,"html.parser")
    
    # Busco los contenedores de los elementos a parsear
    
    results= soup.find_all("div",{"class":"vehicle-card-main"})
    
    for result in results:
        try:
            name.append(result.find("h2").get_text())
            mileage.append(result.find("div",{"class":"mileage"}).text)
            dealer_name.append(result.find("div",{"class":"dealer-name"}).text.strip())
            rating.append(result.find("span",{"class":"sds-rating__count"}).text)
            price.append(result.find("span",{"class":"primary-price"}).get_text())
            img.append(result.find("img")["src"])
            urlx.append((result.find("a")["href"]))
            
        except:
            name.append("n/a")
            mileage.append("n/a")
            dealer_name("n/a")
            rating.append("n/a")
            price.append("n/a")
            img.append("n/a")
            urlx.append("n/a")
            
            
        
    


# In[37]:


jean_vitola=pd.DataFrame({"Name":name,"Mielage":mileage,"dealer_name":dealer_name,"Rating":rating,"Price":price,"Img":img, "Url":urlx})


# In[12]:


jean_vitola


# In[ ]:




