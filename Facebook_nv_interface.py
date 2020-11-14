#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
import time
import os
from datetime import datetime
#installer selenium avant


# In[ ]:


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)



driver.get("https://www.facebook.com")

time.sleep(6)


# In[ ]:


email_element = driver.find_element_by_xpath('.//*[@id="email"]')

email_element.send_keys('')#mettre votre mail facebook

password_element = driver.find_element_by_xpath('.//*[@id="pass"]')

password_element.send_keys('')#mettre le mdp facebook

time.sleep(6)


# In[ ]:


#on valide les identifiant et connexion
log_btm_element = driver.find_element_by_xpath('//*[@id="u_0_b"]')

log_btm_element.click()
time.sleep(3)


# In[4]:



today_d=datetime.now()
today=today_d.isoweekday()
#today=3
print(today)
#h=datetime.datetime.now().strftime('%M')


# In[5]:


os.listdir(r"C:\Users\ibrahim\Downloads\Lundi")
Lundi_images= os.listdir(r"C:\Users\ibrahim\Downloads\Lundi") #il faudra remplacer le chemin par celui de votre ordinateur
Mardi_images= os.listdir(r"C:\Users\ibrahim\Downloads\Mardi")#vous aurez juste à créer des dossier Lundi,Mardi dans le dossier telechargement
Mercredi_images= os.listdir(r"C:\Users\ibrahim\Downloads\Mercredi")
Jeudi_images= os.listdir(r"C:\Users\ibrahim\Downloads\Jeudi")
Vendredi_images= os.listdir(r"C:\Users\ibrahim\Downloads\Vendredi")
Samedi_images= os.listdir(r"C:\Users\ibrahim\Downloads\Samedi")
Dimanche_images= os.listdir(r"C:\Users\ibrahim\Downloads\Dimanche")


# In[6]:


import datetime #rajout de vos groupes facebook
groupe=['https://www.facebook.com/groups/358167132234927','https://www.facebook.com/groups/778629356289090']


# In[8]:


#relancer le block 2 fois si ça la page internet block
""""Dans les variables val changez l adresse en fonction de votre ordi"""
site=['https://www.facebook.com/groups/358167132234927/?ref=bookmarks','https://www.facebook.com/groups/778629356289090/?ref=bookmarks'] 
#c'est la liste des site d'on veut poster des articles automatiquement on peut en ajouter l'infini
while 1:
    compteur=0  
    for br in range (len(site)):
        h=datetime.datetime.now().strftime('%H')
        z=h
        #on se connecte au groupe facebook
        driver.get(site[br]) #mettre l'adresse de votre groupe facebook
        time.sleep(5)
        #on clique pour pouvoir ecrire un message
        #lien = driver.find_element_by_xpath('//*[@id="js_2l"]/div[1]/div/div[1]/div/div[2]/div/div/div/div')
        lien = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div')
        lien.click()
        time.sleep(4)
        if h=='07' or h =="08" or h =="09" or h =="10" or h =="11" or h =="12" or h=="13" or h=="14" or h== "15" or h== "16" or h== "17" or h=="18" or h=="19" or h=="20":
            print("heure égale a",h)
            #on reclique sur le champs texte
            message=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')
            message.send_keys("hello") #message de l'article
       
        
        
            if today ==1:
                for i in range(1):#le nombre d'images que l'on veut charger,dans le dossier du jour, ne pas mettre un chiffre superieur au nombre d'image 
                    if z =='07':
                        compteur=0
                    if z =='08':
                        compteur=1
                    if z =='09':
                        compteur=2
                    if z =='10':
                        compteur=3
                    if z =='11':
                        compteur=4
                    if z =='12':
                        compteur=5
                    if z =='13':
                        compteur=6
                    if z =='14':
                        compteur=7
                    if z =='15':
                        compteur=8
                    if z =='16':
                        compteur=9
                    if z =='17':
                        compteur=10
                    if z =='18':
                        compteur=11
                    if z =='19':
                        compteur=12
                    if z =='20':
                        compteur=13
                    val="C:\\users\\ibrahim\\Downloads\\Lundi\\"+str(Lundi_images[compteur])
                    
                    print(val)
                    image=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/input').send_keys(val)
                time.sleep(5)
                publier=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div[1]')
                publier.click()
            if today ==2:
                for i in range(1):#
                    if z =='07':
                        compteur=0
                    if z =='08':
                        compteur=1
                    if z =='09':
                        compteur=2
                    if z =='10':
                        compteur=3
                    if z =='11':
                        compteur=4
                    if z =='12':
                        compteur=5
                    if z =='13':
                        compteur=6
                    if z =='14':
                        compteur=7
                    if z =='15':
                        compteur=8
                    if z =='16':
                        compteur=9
                    if z =='17':
                        compteur=10
                    if z =='18':
                        compteur=11
                    if z =='19':
                        compteur=12
                    if z =='21':
                        compteur=13
                    
                    val="C:\\users\\ibrahim\\Downloads\\Mardi\\"+str(Mardi_images[compteur])
                    print(val)
                    image=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/input').send_keys(val)
                time.sleep(5)
                publier=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div[1]')
                publier.click()
            if today ==3:
                for i in range(1):
                    if z =='07':
                        compteur=0
                    if z =='08':
                        compteur=1
                    if z =='09':
                        compteur=2
                    if z =='10':
                        compteur=3
                    if z =='11':
                        compteur=4
                    if z =='12':
                        compteur=5
                    if z =='13':
                        compteur=6
                    if z =='14':
                        compteur=7
                    if z =='15':
                        compteur=8
                    if z =='16':
                        compteur=9
                    if z =='17':
                        compteur=10
                    if z =='18':
                        compteur=11
                    if z =='19':
                        compteur=12
                    if z =='20':
                        compteur=13
                    val="C:\\users\\ibrahim\\Downloads\\Mercredi\\"+str(Mercredi_images[compteur])
                    print(val)
                    image=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/input').send_keys(val)
                time.sleep(5)
                publier=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div[1]')
                publier.click()
            if today ==4:
                for i in range(1):
                    if z =='07':
                        compteur=0
                    if z =='08':
                        compteur=1
                    if z =='09':
                        compteur=2
                    if z =='10':
                        compteur=3
                    if z =='11':
                        compteur=4
                    if z =='12':
                        compteur=5
                    if z =='13':
                        compteur=6
                    if z =='14':
                        compteur=7
                    if z =='15':
                        compteur=8
                    if z =='16':
                        compteur=9
                    if z =='17':
                        compteur=10
                    if z =='18':
                        compteur=11
                    if z =='19':
                        compteur=12
                    if z =='20':
                        compteur=13
                    val="C:\\users\\ibrahim\\Downloads\\Jeudi\\"+str(Jeudi_images[compteur])
                    print(val)
                    image=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/input').send_keys(val)
                time.sleep(5)
                publier=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div[1]')
                publier.click()
            if today ==5:
                for i in range(1):
                    if z =='07':
                        compteur=0
                    if z =='08':
                        compteur=1
                    if z =='09':
                        compteur=2
                    if z =='10':
                        compteur=3
                    if z =='11':
                        compteur=4
                    if z =='12':
                        compteur=5
                    if z =='13':
                        compteur=6
                    if z =='14':
                        compteur=7
                    if z =='15':
                        compteur=8
                    if z =='16':
                        compteur=9
                    if z =='17':
                        compteur=10
                    if z =='18':
                        compteur=11
                    if z =='19':
                        compteur=12
                    if z =='20':
                        compteur=13
                    val="C:\\users\\ibrahim\\Downloads\\Vendredi\\"+str(Vendredi_images[compteur])
                    print(val)
                    image=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/input').send_keys(val)
                time.sleep(5)
                publier=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div[1]')
                publier.click()
            if today ==6:
                for i in range(1):#le nombre d'images que l'on veut charger,da,s le dossier du jour 
                    if z =='07':
                        compteur=0
                    if z =='08':
                        compteur=1
                    if z =='09':
                        compteur=2
                    if z =='10':
                        compteur=3
                    if z =='11':
                        compteur=4
                    if z =='12':
                        compteur=5
                    if z =='13':
                        compteur=6
                    if z =='14':
                        compteur=7
                    if z =='15':
                        compteur=8
                    if z =='16':
                        compteur=9
                    if z =='17':
                        compteur=10
                    if z =='18':
                        compteur=11
                    if z =='19':
                        compteur=12
                    if z =='20':
                        compteur=13
                    val="C:\\users\\ibrahim\\Downloads\\Samedi\\"+str(Samedi_images[compteur])
                    print(val)
                    image=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/input').send_keys(val)
                time.sleep(5)
                publier=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div[1]')
                publier.click()
    
            if today ==7:
                for i in range(1):#le nombre d'images que l'on veut charger,da,s le dossier du jour 
                    if z =='07':
                        compteur=0
                    if z =='08':
                        compteur=1
                    if z =='09':
                        compteur=2
                    if z =='10':
                        compteur=3
                    if z =='11':
                        compteur=4
                    if z =='12':
                        compteur=5
                    if z =='13':
                        compteur=6
                    if z =='14':
                        compteur=7
                    if z =='15':
                        compteur=8
                    if z =='16':
                        compteur=9
                    if z =='17':
                        compteur=10
                    if z =='18':
                        compteur=11
                    if z =='19':
                        compteur=12
                    if z =='20':
                        compteur=13
                    val="C:\\users\\ibrahim\\Downloads\\Dimanche\\"+str(Dimanche_images[compteur])
                    print(val)
                    image=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/input').send_keys(val)
                time.sleep(5)
                publier=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div[1]')
                publier.click()
        time.sleep(30)
        
    time.sleep(3598)

