import json
import requests 


page = 0

names = 'knife'
for step in  range(0,100000) :
    url = f'https://cs.money/1.0/market/sell-orders?limit=60&name={names}&offset={page}'
    
    response = requests.get(url).json()
    
    items = response['items']

    page += 60 

    for item in items : 

        name = item['asset']['names']['short']

        price = item['pricing']['computed']

        link = item ['links']['3d']

        print (f'{price} -- {name} -- {link}')
        print ('=============================')

    if len(items) < 60:
        print ('пошел нахуй')
        break 








        
    

