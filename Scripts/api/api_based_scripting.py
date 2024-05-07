# The file contains method to script the user profile from linkedin using linkedin-api
# We will install the basic libraries required for running the script
# We have created a venv for ensuring the version dependencies and smooth fucntion of script

# Importing necessary libraries
import getpass
import csv
from linkedin_api import Linkedin
from dataclasses import dataclass
import json





@dataclass
class Linkedin_data:
    """Stores information of user profile"""

    
    
    def fetch_names(self,first_name,last_name,filename):
        """
    Returns the first 5 profiles with similar names
    Input : First name, last name and filename to save the data
    Output : Top 5 similar profile
        """    
        
        username = input("Enter your username or registered email-address:")
        password = getpass.getpass("Enter your password:")    #Ensures password is not visible



        # takes your username,password for initiating the api
        linkedin = Linkedin(username,password)
        if linkedin:
            print("Authentication completed!")
        else:
            print("Error in authentication")
        

        try:
            # provides search result for people with user input
            search_result = linkedin.search_people(first_name,last_name, limit = 10)
            #print(search_result)

            # writing data to csv file
            with open(filename,'w', newline='', encoding = 'utf-8') as f:
                fieldname = ['Name','Profession','Location','Industry','Headline']
                writer = csv.DictWriter(f,fieldnames=fieldname)
                writer.writeheader()
                for results in search_result:

                    # accessing the data in the search results which can be used for more data collection

                    #Extracts profession details
                    profession = ''
                    if results['jobtitle'] is not None:
                        profession = results['jobtitle']
                    else:
                        profession = 'NA'
                    
                    #Extracts name
                    Name = ''
                    if results['name'] is not None:
                        Name = results['name']
                    else:
                        Name = 'NA'

                    #Extracts the location
                    location = ''
                    if results['location'] is not None:
                        location = results['location']
                    else:
                        location = 'NA'

                    #Extracts urn_id
                    urn_id = ''
                    if results['urn_id'] is not None:
                        urn_id = results['urn_id']
                    else:
                        urn_id = 'NA'    

                    # Using name for extracting profile details
                    # from profile details we can acess profile skills,headlines and current industry.
                    profile_details = linkedin.get_profile(urn_id)
                    industry = profile_details['industryName']
                    headline = profile_details['headline']
                    
             
                    writer.writerow({
                        'Name' : Name,
                        'Profession': profession,
                        'Location': location,
                        'Industry': industry,
                        'Headline': headline
                    })
                return filename
        except ValueError as e:
            print(f'There is no user with {first_name}{last_name}')
        

if __name__ == "__main__":
    linkedin_data = Linkedin_data()
    first_name = input("Enter the first name:")
    last_name = input("Enter the last name:")
    filename = input('Enter name for saving the file(include .csv at last):')
    linkedin_data.fetch_names(first_name,last_name,filename)
