# The file contains method to script the user profile from linkedin using linkedin-api
# We will install the basic libraries required for running the script
# We have created a venv for ensuring the version dependencies and smooth fucntion of script

# Importing necessary libraries
import requests
import csv
from linkedin_api import Linkedin
from dataclasses import dataclass
from typing import List,Dict
import json


@dataclass
class Linkedin_data:
    """Stores information of user profile"""
    
    def fetch_names(self,first_name,last_name):
        """
    Returns the first 5 profiles with similar names
    Input : First name, last name
    Output : Top 5 similar profile
        """    

        linkedin = Linkedin()
        # provides search result for people with user input
        search_result = linkedin.search_people(first_name,last_name, limit = 5)

        #defining filename for our data
        filename = f"{first_name}_{last_name}_data.csv"

        # writing data to csv file
        with open(filename,'w', newline='', encoding = 'utf-8') as f:
            fieldname = ['First_Name','Last_Name','Profession','Feed_Post']
            writer = csv.DictWriter(f,fieldnames=fieldname)
            writer.writeheader()
            for results in search_result:

                # access headline to know about profession/ returns no headline found for profiles with no healdines 
                profession = results.get('headline','No headline found')

                #acess the publicIdentifier to construct profile.
                profile_url = "https://www.linkedin.com/in/" + results['publicIdentifier']

                feed_post = self.get_feed_post(linkedin, results['publicIdentifier'])
             
                writer.writerow({
                    'First_Name': results['firstName'],
                    'Last_Name': results['lastName'],
                    'Profession': profession,
                    'Feed_post': feed_post
                })
        return filename        

    def get_feed_post(self, linkedin, publicIdentifier):
        """
        Returns the recent feed post of the user """
        try:
            profile = linkedin.get_profile(publicIdentifier)
            recent_feed_post = profile.get('activity',{}).get('post',{}).get('content',{}).get('text',None)
            return recent_feed_post
        except Exception as e:
            print(f"Error fetching post details for {publicIdentifier} as e")
            return "No data fetched"
        

if __name__ == "__main__":
    linkedin_data = Linkedin_data()
    first_name = input("Enter the first name:")
    last_name = input("Enter the last name:")
    Linkedin_data.fetch_names(first_name,last_name)
