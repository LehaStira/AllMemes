import requests
from os import mkdir
with open('token.txt', 'r') as f:
    my_token = f.read()

TOKEN = my_token
COUNT_OF_POSTS = 10000 # количество постов

class Parser:
    def __init__(self):
        self.__main_url = 'https://api.vk.com/method/wall.get' # урла для реквеста
        self.__token = TOKEN  #
        # придумать другую возможность импорта токена
        self.version = 5.21  # версия вк апи
        self.my_count = 100 # максимум за такт - 100 постов
        self.my_offset = 0  # эту хрень мы сдвигаем на 100 и увеличиваем, скорее всего ей не место в инициализаторе
        self.c = 0


    @staticmethod
    def create_dir_of_group(path):
        mkdir(path)

    @staticmethod
    def create_dir_of_quality(path):
        mkdir(path)

    @staticmethod
    def save_meme(path, image_bytes):
        with open(path, 'wb') as f:
            f.write(image_bytes)


    def download(self, url, domain, quality):
        image_bytes = requests.get(url).content
        dir_of_group = f'{domain}'
        try:
            Parser.create_dir_of_group(dir_of_group)
        except OSError:
            pass
        dir_of_quality = f'{dir_of_group}\\{quality}'

        try:
            Parser.create_dir_of_quality(dir_of_quality)
            self.c = 0
        except OSError:
            self.c+=1

        meme_path = f'{dir_of_quality}\\{self.c}.jpg'
        Parser.save_meme(path = meme_path,
                         image_bytes = image_bytes)

        return f'Привет, это лог! {self.c}.jpg успешно поставлен! Качество = {quality}, путь - {meme_path}'

    def get_memes(self, domain):
        c = 0  # сколько сохраненных картинок
        COUNT_OF_POSTS = 10000  # количество постов
        while self.my_offset <= COUNT_OF_POSTS:
            response = requests.get(self.__main_url, params={
                'access_token': self.__token,
                'v': self.version,
                'domain': domain,  # домен группы
                'count': self.my_count,
                'offset': self.my_offset})
            data = response.json()  # первый ноль
            for i in range(1, self.my_count-1):  # получаем сто постов за итерацию while
                try:
                    quality = 'photo_2560'  # всего подкачеств картинок - 9
                    if data['response']['items'][i]['marked_as_ads'] != 0:  # если реклама, то минус
                        continue
                    #for q in range(1, quality+1):
                        #url = data['response']['items'][i]['attachments'][0]['photo']['sizes'][q]['url']
                    url = data['response']['items'][i]['attachments'][0]['photo']['photo_2560']
                    c += 1
                    res_string = self.download(url = url,
                                                 domain = domain,
                                                 quality = quality)
                    print(res_string)
                except IndexError:
                    pass
                except KeyError:
                    print('Нет фотографии')




if __name__ == '__main__':
    my_parse = Parser()
    list_of_domains = ['dobriememes', 'prosvet_pub', 'eight_out_ten']
    for domain in list_of_domains:
        my_parse.get_memes(domain=domain)




