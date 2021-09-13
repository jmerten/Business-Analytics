# M5: JSON Scraping
# Created by Jason Merten

import requests

url = 'https://buckets.peterbeshai.com/api/?player=201939&season=2015'
headerText = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41'}
response = requests.get(url,headers=headerText)
json = response.json()

jump_shots = []
for i in json:
    if i['ACTION_TYPE']=='Jump Shot':
        if i['EVENT_TYPE']=='Made Shot':
            jump_shots.append(1)
        else:
            jump_shots.append(0)
print('W&M Username: Jmerten')
print('Number of Jump Shots: ',len(jump_shots))
print('Number of Successful Jump Shots: ',sum(jump_shots))
print('% Successful Jump Shots: ',round(sum(jump_shots)/len(jump_shots)*100,2),'%')