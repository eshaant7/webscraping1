from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(start_url)

def scrape():
    headers = ["Proper name", "Distance", "Mass", "Radius"]
    star_data = []

    soup = BeautifulSoup(page.text, 'html.parser')

    star_table = soup.find('table')
    temp_list = []
    table_rows = star_table.find_all('tr')
    
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.rstrip() for i in td] 
        #never learned i.text.rstrip
        #we never used it in the class, so why here?
        temp_list.append(row)
        
    Star_names = []
    Distance =[]
    Mass = []
    Radius =[]
    Luminosity = []

    for i in range(1,len(temp_list)):
        Star_names.append(temp_list[i][1]) # why here its 1 
        Distance.append(temp_list[i][3]) # but here its 3
        Mass.append(temp_list[i][5]) # and here its 5
        Radius.append(temp_list[i][6]) # but then here its 6
        Luminosity.append(temp_list[i][7]) # and 7?
        #from 1 to 5, it is skipping 2, and 4, but then its not skipping 6?
        
    df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Luminosity)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
    #why do i use list() function here?
    print(df2)

    df2.to_csv('bright_stars.csv')

scrape()
