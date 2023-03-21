import requests
from bs4 import BeautifulSoup 

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36'}

 

def info ():
    global name
    x = 0 
    z = 0
    
    for page in range (0,6):
        x +=1
        print (f'{x}страницаааааааааааааааааа')

        url = f'https://zastavok.net/{page}/'
        response = requests.get (url, headers = headers ).content

        soup = BeautifulSoup(response, 'lxml')

        block = soup.find_all ('div' , class_ = 'short_full')  #карточка товара

        for cards in block:

            z = z+1

            name = cards.find ('span', class_ = "short_wallcat").text  #имя товара

            # print (f"{z}{name}") 

def photo (): 
    url = f'https://zastavok.net/' #общая сылка 
    zero = 0
    for page in range(0,2):
        url1 = f'{url}/{page}' #сылка страниц
        
        response = requests.get(url1 , headers = headers).content 

        soup = BeautifulSoup(response , 'lxml')

        block = soup.find_all('div', class_ = 'short_full')#блок карточек

        for image in block:
            link = image.find ('a').get('href')

            link1 = f'{url}/{link}' #сылка переходов на страницу

            response1 = requests.get (link1, headers = headers ).content

            soup1 = BeautifulSoup(response1, 'lxml')

            download = soup1.find('div' , class_ = "block_down") #блок с сылкой на скачивание

            download1 = download.find('a').get('href') #сылка на скачивание


            link_dow = f'{url}{download1}' #полная сылка

            

            im_photo = requests.get(link_dow ).content  #дастаем контент 

            with open (f'D:/phyton/training/парсеры2/image/{zero}.jpg', 'wb') as file:
                file.write(im_photo)   #загружаем на комп 

            zero +=1 
            print ('есть')



def main ():
    info()
    photo()
if __name__ == "__main__":
    main()