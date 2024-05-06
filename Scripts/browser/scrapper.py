# The file contains method for scrapping the data using beautifulsoup and selenium

from selenium import webdriver
from bs4 import BeautifulSoup
from chromedriver_py import binary_path
import csv
import time

def fetch_data(first_name,last_name):

    """
    Returns the data with top 10 users with same first name and last name.
    """

    # Setting up headless browser
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #driver = webdriver.Chrome(options=options)
    svc = webdriver.ChromeService(binary_path)
    driver = webdriver.Chrome(service=svc)

    # Create search query
    query = f"https://www.linkedin.com/search/results/people/?keywords={first_name}%20{last_name}&origin=GLOBAL_SEARCH_HEADER&sid=*kM"
    print(query)

    #send http request
    driver.get(query)
    #waiting for page to load
    driver.implicitly_wait(10)

    start = time.time()
    
    # will be used in while loop
    initialScroll = 0
    finalScroll = 1000

    while True:
        driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")

        # this command scrolls the window starting from
        # the pixel value stored in the initialScroll 
        # variable to the pixel value stored at the
        # finalScroll variable

        initialScroll = finalScroll
        finalScroll += 1000

        #Stops script for 5 sec for data to load
        time.sleep(5)

        end = time.time()

        # setting minimum 30 sec scroll time.
        if round(end - start)>30:
            break    

    #Parse html content
    soup = BeautifulSoup(driver.page_source,'html.parser')

    # Extracting html  of the complete introduction box
    # that contains the name,company name,location.
    
    profiles = soup.find_all('li', {"class" : "reusable-search__result-container"})
    #print(introduction)

    # writing the data into csv files.
    with open('linkedin.csv','w',newline = "", encoding = 'utf-8') as file:
        fieldnames = ['Name','Headline','Location']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # Subsetting top 10 profiles we need to scrap.
        for profile in profiles[:10]:
            # Name of the person is in a tag with span
            profile_title = profile.find('span',{'class' : "entity-result__title-text"})
            name =  ""
            #extracting only text part from the search result obtained.
            # Strip removes extra spaces 
            if profile_title is not None:
                name_location = profile_title.find('span',{"aria-hidden":"true"})
                if name_location is not None:
                    name = name_location.get_text(strip=True)
    

            #searches for job into headline
            job = ""
            job_div = profile.find('div',{'class':'entity-result__primary-subtitle t-14 t-black t-normal'})
            if job_div is not None:
                job = job_div.get_text(strip=True)


            #searches for location 
            location = ""
            location_div = profile.find('div',{'class':'entity-result__secondary-subtitle t-14 t-normal'})
            if location_div is not None:
                location = location_div.get_text(strip=True)


            writer.writerow({
                'Name':name,
                'Headline':job,
                'Location':location
            })
    driver.quit()                 

           

if __name__ == "__main__":
   First_name = input('Enter your first name:')
   Last_name = input('Enter your last name:')
   fetch_data(First_name,Last_name)