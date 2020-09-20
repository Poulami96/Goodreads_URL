import os
import re
import requests
import xml.etree.ElementTree as ET
 
def get_book_details(url:str)->dict: 
    try:
        numbers = re.findall('\d+',url)
        res="https://www.goodreads.com/book/show/"+numbers[0]+".xml?key=wyfpaokyxy16ZIjMLaCA"
        r = requests.get(res)
        root = ET.fromstring(r.text)
        tree = ET.ElementTree(root)
        tree.write("file.xml")
        my_tree=ET.parse('file.xml')
        my_root=my_tree.getroot()
        
        try:
            for x in my_root.findall('book'):
                title=x.find('title').text
                average_rating=x.find('average_rating').text
                ratings_count=x.find('ratings_count').text
                num_pages=x.find('num_pages').text
                image_url=x.find('image_url').text
                publication_year=x.find('publication_year').text
                authors=x.find('authors').text
                
                #5.Fields not having value can be given null values
                if(title==None):
                    title="NULL"
                    
                if(average_rating==None):
                    average_rating="NULL"
                else:
                    average_rating=float(average_rating)
                
                if(ratings_count==None):
                    ratings_count="NULL"
                else:
                    ratings_count=int(float(ratings_count))
                    
                if(num_pages==None):
                    num_pages="NULL"
                else:
                    num_pages=int(float(num_pages))
                
                if(image_url==None):
                    image_url="NULL"
                
                if(publication_year==None):
                    publication_year="NULL"
                
                if(publication_year==None):
                    publication_year="NULL"
                
                dict={"title":title,"average_rating":average_rating,"ratings_count":ratings_count,"num_pages":num_pages,"image_url":image_url,"publication_year":publication_year,"authors":authors}
                
            for x in my_root.findall('.book/authors/author'):
                authors=x.find('name').text
                
                #5.Fields not having value can be given null values
                if(authors==None):
                    authors="NULL"
                    
                dict1={"authors":authors}
                dict.update(dict1)
        except:
            #4.Goodreads returns invalid XML response,return an empty dictionary
            dict={}
            return dict  
        
        return dict
    except:
        #Raise an exception InvalidGoodreadsURL
        raise Exception("InvalidGoodreadsURL")
    
#BONUS 1-Take URL from command line input
url=str(input())

print(get_book_details(url))
if os.path.exists("file.xml"): 
    os.remove("file.xml") 