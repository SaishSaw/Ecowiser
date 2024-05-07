# Web Scrapping

 In today's data-driven world, access to accurate and relevant information is paramount for making informed decisions. With the exponential growth of digital content, web scraping has emerged as a powerful tool for extracting valuable data from websites efficiently and systematically. In this project, we aim to harness the power of web scraping using Python to extract data from LinkedIn, the world's largest professional networking platform.

Advantages of Web Scraping:

* Access to Rich and Timely Data: Web scraping enables us to access a vast amount of data available on the web, including real-time updates. By extracting data from LinkedIn, we can gather insights into various aspects such as industry trends, job postings, company information, and user profiles.

* Competitive Intelligence: By scraping data from LinkedIn, we gain valuable insights into competitor activities, market trends, and user behavior. This information can help businesses stay ahead of the curve and make strategic decisions to gain a competitive edge.

* Automated Data Collection: Web scraping allows us to automate the process of data collection, saving time and resources. Instead of manually browsing through web pages and copying information, we can write scripts to extract data programmatically, enabling us to gather large volumes of data quickly and efficiently.

* Customized Data Extraction: With web scraping, we have the flexibility to tailor the data extraction process to our specific requirements. We can define the parameters, filters, and data fields to extract only the relevant information we need, ensuring data accuracy and relevance.

* Enhanced Decision Making: By analyzing the extracted data, we can derive valuable insights and trends that can inform decision-making processes across various domains such as business, marketing, finance, and human resources. These insights enable organizations to make data-driven decisions that drive growth and success.

* Research and Analysis: Web scraping empowers researchers, analysts, and data scientists to conduct in-depth research and analysis by accessing a wide range of publicly available data sources. This data can be used for academic research, market analysis, sentiment analysis, and other analytical purposes.

By leveraging the advantages of web scraping, we can unlock the potential of data available on LinkedIn and gain actionable insights that drive innovation, growth, and success in today's competitive landscape.


## Overview

* The repository is an simple tutorial for web scrpaing data using web browser automation and api.
* The folder scripts consists of two folders each for different methods used for scraping.
* The script for scrapping are written in python.
* Scripting is done with point to obtain maximum data which can be extracted.
* Data obtained from scripting is stored in .csv file format which can be later used for further analysis.
* As of this demo is concered we have restricted to only 10 profiles that match with our search queries.


## Contents
* Script folder consisting of api and browser folder
* API folder consists of api_based_scripting.py file and sample output
* Browser folder consists of scrapper.py file and sample output

## Requirements
* The requirements for this project is mentioned in requirements.txt
* For browser based scrapping we need selenium and bs4 to implement the scrapping process
* While scrapping using selenium we need driver for our latest browser version.It is necessary that driver version is compatible with browser version else we can encounter error.
* We have used chromedriver_py python module for satisfying the driver requirements (Chrome Version: 124.0.6367.119)
* In order to install chromdriver_py follow ![link](https://pypi.org/project/chromedriver-py/)

## Install requirements
Follow the commands to install the requirements file.
``` ruby
pip install -r requirements.txt 
pip install chromedriver-py
```
