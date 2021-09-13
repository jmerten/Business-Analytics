# Module 5 XML Web Scraping
# Created by: Jason Merten

import requests
from lxml import objectify

parameter = 'tavg'  # temperature average
state = '44'    # Virginia
month = '08'    # August
year = '2018'
url = 'https://www.ncdc.noaa.gov/cag/statewide/rankings/%s-%s-%s%s/data.xml'

response = requests.get(url % (state,parameter,year,month)).content

root = objectify.fromstring(response)

for i in range(0,5):
    print('W&M Username: Jmerten')
    print('Value: ',root['data'][i]['value'])
    print('Mean: ',root['data'][i]['mean'])
    print('Departure: ',root['data'][i]['departure'])
    print('LowRank: ',root['data'][i]['lowRank'])
    print('HighRank: ',root['data'][i]['highRank'])
    print('----------------')