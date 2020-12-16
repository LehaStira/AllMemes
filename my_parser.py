import requests

COUNT_OF_POSTS = 10000 # количество постов

class Parser:
    def __init__(self):
        self.__main_url = 'https://api.vk.com/method/wall.get' # урла для реквеста
        self.__token = '8e3947e09f2d710918e99165329c1170ba2c66f9103447282ef9c43c3c314aa8a990d80529541dac95f07'  #
        # придумать другую возможность импорта токена
        self.version = 5.2  # версия вк апи
        self.my_count = 100 # максимум за такт - 100 постов
        self.my_offset = 0 # эту хрень мы сдвигаем на 100 и увеличиваем, скорее всего ей не место в инициализаторе



def download(url, count, domain):
    image_bytes = requests.get(url).content

    path = f'good_memes\\{domain}-{count}.jpg'
    with open(path, 'wb') as f:
        f.write(image_bytes)
    return f'Привет, это лог! {count}.jpg успешно поставлен! Качество = {9}, путь - {path} '


main_url = 'https://api.vk.com/method/wall.get'
token = '8e3947e09f2d710918e99165329c1170ba2c66f9103447282ef9c43c3c314aa8a990d80529541dac95f07'
version = 5.92
domain = 'dobriememes'
my_count = 100 # максимум за такт - 100 постов
my_offset = 0 # эту хрень мы сдвигаем и на сто увеличиваем
c = 0 # сколько сохраненных картинок
COUNT_OF_POSTS = 10000 # количество постов
while my_offset<=COUNT_OF_POSTS:
    response = requests.get(main_url, params={
        'access_token': token,
        'v' : version,
        'domain' : domain, # домен группы
        'count' : my_count,
        'offset': my_offset})
    data = response.json() #первый ноль
    for i in range(my_count): #получаем сто постов за итерацию while
        try:
            quality = 9
            if data['response']['items'][i]['marked_as_ads']!=0: #если реклама, то минус
                continue
            #for q in range(quality):
            url = data['response']['items'][i]['attachments'][0]['photo']['sizes'][quality]['url']
            c +=1
            print(f'Привет, это лог! Всего фотографий: {c}')
            res_string = download(url=url, count=c, domain=domain)
            print(res_string)
        except IndexError as err:
            print('Нет фотографии!')
        except KeyError as err:
            print('Нет фотографии')
    my_offset+=100