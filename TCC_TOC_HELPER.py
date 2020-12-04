#!/usr/bin/env python
# coding: utf-8

# In[45]:


#format_text = '<p id="alternatives" /p>'
#TOC_Text = '/horse-racing/#alternatives'


# In[12]:


def print_anchor_tags(url):
    import os.path
    import requests
    res = requests.get(url)
    html_page = res.content

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    set([t.parent.name for t in text])
    output = ''
    output_2 = ''
    blacklist = {'[document]','a','body','button','div','em','fieldset','figcaption','figure','footer','form','head','header','html','i','label','legend','li','link','main','meta','nav','p','script','span','strong','style','svg','title','ul'}
    final_list_H1 = []
    final_list_H2and3 =[]
    H1 =[]
    H2and3 =[]
    Full_List = []
    final_list=[]
    page_title = url.replace("https://www.considerate-consumer.com/","")
    filename = page_title + "_HTML_ANCHORTEXT+TOC_HELPER_output.txt"
    file = open(filename, "w")
    
    A = "\n"+"Squarespace Anchor Text and TOC Helper"+"\n"+"\n"+"Here are the HTML Anchor Texts for the webpage that you provided. Additionally, the TOC links will be included for convenience." "\n" + "\n"+ "Instructions for use:" + "\n" +"Please ensure that all headings are done for the page (This helper will work even if the headings are not correct but H1, H2, and H3 need to be set.)." + "\n" + "Enable the page." + "\n" + "Copy the URL for the page and use it when prompted." + "\n" + "Copy the text as needed. (Note: if H1 headings are properly identified on the page, the html for the horizontal line will be included.)"+ "\n" + "\n" +"For any problem or questions, please consult Tyler Stevenson @stevetylda@gmail.com" + "\n" + "\n" + "For use by The Considerate Consumer Content Management Team"+"\n" + "\n" +"Have a nice day! :)"+"\n"+"\n"+"\n"+ "\n"+ "Here is the Table of Contents for Easy Copying: "+ "\n"+"\n"
    file.writelines(A)
    
    for t in text:
        #H1 Outputs
        if t.parent.name == 'h1':
            output = '{}'.format(t)
            output = output.replace("\n","")
            output = output.lstrip()
            H1.append(output)
        #H2 and H3 Outputs
        if t.parent.name == 'h2':
            output = '{}'.format(t)
            output = output.replace("\n","")
            output = output.lstrip()
            H2and3.append(output)   
        if t.parent.name == 'h3':
            output = '{}'.format(t)
            output = output.replace("\n","")
            output = output.lstrip()
            H2and3.append(output)
            
            
    for t in text:
        if t.parent.name == 'h1':
            output = '{}'.format(t)
            output = output.replace("\n","")
            output = output.lstrip()
            output = output.upper()
            Full_List.append(output)
            
        if t.parent.name == 'h2':
            output = '{}'.format(t)
            output = output.replace("\n","")
            output = output.lstrip()
            output = output.title()
            output = output.replace("Learn More","")
            output = output.replace("Subscribe To Our Newsletter","")
            output = "     " + output
            Full_List.append(output)   
        if t.parent.name == 'h3':
            output = '{}'.format(t)
            output = output.replace("\n","")
            output = output.lstrip()
            output = output.title()
            output = output.replace("Learn More","")
            output = output.replace("Subscribe To Our Newsletter","")
            output = "          " + output
            Full_List.append(output)

    for h in Full_List:
        final_list.append(h)
        T = str(h)+'\n'
        file.writelines(T)
        
    for h in H1:
        h = h.replace("\n","")
        h = h.lstrip()
        final_list_H1.append(h) 
            
    for h in H2and3:
        h = h.replace("\n","") 
        h = h.lstrip()
        final_list_H2and3.append(h) 
        
##################################################################################################################       
    #Outputs for H1
    page_title = url.replace("https://www.considerate-consumer.com/","")
    for i in final_list_H1:
        #Dealing with the Anchor Link
        html = i.lower()
        html = html.replace("-"," ")
        html = html.replace(",","")
        html = html.replace("?","")
        html = html.replace("!","")
        html = html.replace(".","")
        html = html.replace("'","")
        html = html.replace("&","")
        html = html.replace("(","")
        html = html.replace(")","")
        html = html.replace(" ","-")
        html = html.replace("--","-")
        html = html.replace("...","")
        html = html.replace(" ","")
        
        TOC_name = "/" + str(page_title) + "/#" + html
        html = "<p id=" + '"'+ str(html) + '"' + " /p>"
        vertical_line = '<hr style="width:100%" /hr>'
        G = "\n"+ "--------------------------------------------------------------------------------"+"\n" +str(i.upper())+"\n"+ "HTML ANCHOR TEXT: "+ str(vertical_line) + "" + str(html)+ "\n"+ "TOC Link: "+ str(TOC_name)+"\n"
        file.writelines(G)  

    #Outputs for H2 and H3
    for j in final_list_H2and3:
        #Dealing with the Anchor Link
        jtml = j.lower()
        jtml = jtml.replace("-"," ")
        jtml = jtml.replace(",","")
        jtml = jtml.replace("?","")
        jtml = jtml.replace("!","")
        jtml = jtml.replace(".","")
        jtml = jtml.replace("'","")
        jtml = jtml.replace("&","")
        jtml = jtml.replace("(","")
        jtml = jtml.replace(")","")
        jtml = jtml.replace(" ","-")
        jtml = jtml.replace("--","-")
        jtml = jtml.replace("...","")
        jtml = jtml.replace(" ","")
        jtml = jtml.replace("-[a-z]","")
        
        TOC_name = "/" + str(page_title) + "/#" + jtml
        jtml = "<p id=" + '"'+ str(jtml) + '"' + " /p>"
        L = "\n"+"--------------------------------------------------------------------------------"+"\n" + str(j.upper())+ "\n"+ "HTML ANCHOR TEXT: "+ str(jtml)+ "\n"+ "TOC Link: "+ str(TOC_name)+"\n"
        file.writelines(L)
   
    
####################################################################################################################


    file.close()

print("|************************************************************************************************|")  
print("                    Welcome to the TCC Anchor Text and TOC Helper!")
print("")
print("Please enter the URL for the page here:  ")
print_anchor_tags(input())
print("")
print("|************************************************************************************************|")
print("                   Helper complete. The output text file is ready.")


# In[ ]:




