#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Modules
import os
import requests
import json
import html
from bs4 import BeautifulSoup


# In[63]:


def getURL(page):
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def link_verifier(url):
    #start_time = process_time()
    #Lists
    url_list = []
    full_list = []
    new_url_list = []
    
    #Create a Text File for Output
    page_title = url.replace("https://www.considerate-consumer.com/","")
    filename = page_title.upper() + "_VERIFIED_LINKS.txt"
    file = open(filename, "w")

    #Access the Webpage
    error_count = 0
    success = False
    while not success and error_count < 7:
        response = requests.request("GET",url)
        if response.status_code < 400:
            success = True
        else:
            print("Error with request, trying again")
            error_count += 1
    if success:
        print("Request successful")
    else:
        print("Successive Failed Attempts, Giving Up...")

    page = str(BeautifulSoup(response.content, features ="lxml"))
   
    #List the URLs from the Page
    while True:
        url, n = getURL(page)
        page = page[n:]
        if url:
            url_list.append(url)
        else:
            break       
        
    for i in url_list:   
        if "https://www.considerate-consumer.com/" not in i: 
            new_url_list.append(i)
        else:
            full_list.append(i)
    for k in new_url_list:
        if k[0] == "/":
            k = k.replace("/", "https://www.considerate-consumer.com/",1)
        if k[0] == "#":
            k = k.replace("#","https://www.considerate-consumer.com/#",1)
 
        full_list.append(k)   
    
    #Now, check for working links. 
    exception_list = []
    code_200 = []
    code_300 = []
    code_400 = []
    code_500 = []
    
    ## Here we can change how many links we pull
    list_loop = full_list

    #Contine check
    idx_429 = []
    while len(list_loop) > 0:
        idx_429 = [] 
        for h in list_loop:
            try:
                ret = requests.head(h)
                
                if ret.status_code == 429:
                    idx_429.append(h)
            
                elif ret.status_code < 300:
                    code_tup = (h, ret.status_code)
                    code_200.append(code_tup)
                
                elif ret.status_code < 400 and ret.status_code > 299:
                    code_tup = (h, ret.status_code)
                    code_300.append(code_tup)
 
                elif int(ret.status_code) > 399 and int(ret.status_code) < 500:
                    code_tup = (h, ret.status_code)
                    code_400.append(code_tup)
                
                else:
                    code_tup = (h, ret.status_code)
                    code_500.append(code_tup)
            
            except:
                continue
                
        list_loop = idx_429
        print("*************************************************************************")
    
    #Adding necessary lines to the output text file
    page_title_2 = page_title.replace("-", " ")
    Z = "\n" + "Link Verifier Output for "+ str(page_title_2.title()) +"\n"+"\n"
    file.write(Z)
    
    A = "\n" + "Status Code 200 - Link List: "+ "\n" +"\n"+"Code               "+ "Link"+"\n"
    file.write(A)
    for h in code_200:
        T = str(h[1])+"     "+str(h[0])+'\n'
        file.writelines(T) 
        
    B = "\n" +"\n"+ "Status Code 300 - Link List: "+ "\n" +"\n"+"Code               "+ "Link"  +"\n"  
    file.write(B)
    for h in code_300:
        T = str(h[1])+"     "+str(h[0])+'\n'
        file.writelines(T)    
   
    C = "\n" +"\n" +"Status Code 400 - Link List: " +"\n" +"\n"+"Code               "+ "Link"+"\n"
    file.write(C)
    for h in code_400:
        T = str(h[1])+"     "+str(h[0])+'\n'
        file.writelines(T)
     
    D = "\n" +"\n" +"Status Code 500 - Link List: " +"\n" +"\n"+"Code               "+ "Link" +"\n"
    file.write(D)
    for h in code_500:
        T = str(h[1])+"     "+str(h[0])+'\n'
        file.writelines(T)
        
    file.close()
    
print("|************************************************************************************************|")  
print("                    Welcome to the TCC Link Verifier!")
print("")
print("Version: 1.0.0 ")
print("")
print("Instructions for use:")
print("     Copy the web address for the target page (e.g. copy : 'https://www.considerate-consumer.com/shopping-bag')")
print("     Wait for program to run - typically <5 minutes")
print("     Output text file will be save to your current working directory.")
print("")
print("Any problems or questions? Please consult Tyler Stevenson")
print("For use by The Considerate Consumer Content Management Team")
print("")
print("Please enter the URL for the page here:  ")
link_verifier(input())
print("")
print("                   Helper complete. The output text file is ready. Have a nice day! :)")
print("|************************************************************************************************|")


# In[ ]:




