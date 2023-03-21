import requests 
from bs4 import BeautifulSoup
import fake_useragent

# задачи : вывести название и сылку на отель 

url = 'https://www.tury.ru/hotel/'

user = fake_useragent.UserAgent().random

headers = {'user-agent': user}

sesion = requests.session()
x = 0 

for page in range (0, 1000000, 20):
    
    x +=1
    print (x)

    url1 = f'https://www.tury.ru/hotel/?cn=0&ct=0&cat=0&txt_geo=&srch=&s={page}'
 
    response = sesion.get (url1 , headers = headers).content

    soup = BeautifulSoup(response , 'lxml')

    # block = soup.find ('div' , class_ = 'reviews-travel__column')  # вся страница каталога отелей


    block1 = soup.find_all ('div', class_ = "reviews-travel__item") # все карточки отелей

    for hostel in block1:
        name = hostel.find ('div' , class_ = 'h4').text

        link = hostel.find ('a').get('href') 

        # print (f'название отеля - {name} \n сылка на него - {link}')



        response_hostel = sesion.get (link , headers = headers ).content

        soup_hos = BeautifulSoup( response_hostel , 'lxml')

        try :

            block_des = soup_hos.find ('div', class_ = 'hotel__text').text 

            if len(block_des) < 1 :
                block_des = 'нет описания'
            

        except :
            block_des = 'нет описания'

        print (f'название отеля - {name} \n сылка на него - {link}  \n описание - {block_des}')
            

    if len(block1) < 20:
        break




