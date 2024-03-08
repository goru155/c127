from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # Loop to find element using XPATH
        table = soup.find("table", attrs={"class", "wikitable"})

        table_body = table.find("tbody")

        table_rows = table_body.find_all("tr")

        temp_list = []

        for row in table_rows:
            table_col = row.find_all("td")

            for col_data in table_col:
                data = col_data.text.strip()

                temp_list.append(data)

        scraped_data.append(temp_list)

stars_data = []

for i in range(len(scraped_data)):
    
    star_name = scraped_data[i][1]
    dist = scraped_data[i][3]
    mass = scraped_data[i][5]
    radius = scraped_data[i][6]
    lumin = scraped_data[i][7]

    req_data = [star_name,dist,mass,radius,lumin]
    stars_data.append(req_data)

scrape()

headers = ["name", "dist", "mass", "radius", "lumin"]

stars_df_1 = pd.DataFrame(stars_data, columns=headers)

stars_df_1.to_csv('scraped_data.csv',index=True, index_label="id")