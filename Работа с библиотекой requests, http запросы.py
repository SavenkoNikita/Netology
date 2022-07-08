import datetime
from pprint import pprint

import requests


class SuperHero:

    def __init__(self):
        self.token = '2619421814940190'
        self.url = f'https://superheroapi.com/api/{self.token}/'

    def get_json_params_hero(self, name_hero):
        response = requests.get(f'{self.url}search/{name_hero}')
        return response.json()

    def get_an_intelligence_level(self, name_hero):
        data_hero = self.get_json_params_hero(name_hero)
        intelligence = data_hero['results'][0]['powerstats']['intelligence']  # noqa
        return intelligence

    def who_is_the_smartest(self, list_hero):
        dict_hero = {}

        intelligence_level = {'hero': 0}

        for i in list_hero:
            dict_hero[i] = self.get_an_intelligence_level(i)
            print(f'У {i} уровень интеллекта равен {int(self.get_an_intelligence_level(i))}')
            for values in intelligence_level.values():
                if int(self.get_an_intelligence_level(i)) > int(values):
                    intelligence_level = {i: self.get_an_intelligence_level(i)}

        top_hero = list(intelligence_level.keys())[0]
        top_skill = list(intelligence_level.values())[0]

        return f'У {top_hero} самый высокий интеллект, он равен {top_skill}'


class YaUploader:
    def __init__(self, token: str):  # noqa
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)

        href_json = response.json()
        href = href_json['href']
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()  # If status code is not 2##, break func, and print error
        if response.status_code == 201:
            print(f'Файл "{file_path}" успешно размещён на Я.Диск')
        else:
            print(f'При отправке файла возникла ошибка - {response.status_code}')


class StackOverFlow:
    def __init__(self):
        self.todate = datetime.date.today()  # Текущая дата  # noqa
        self.fromdate = self.todate - datetime.timedelta(days=2)  # текущая дата минус 2 дня  # noqa
        self.params = {
            'fromdate': self.fromdate,  # noqa
            'todate': self.todate,  # noqa
            'tagged': 'python',
            'site': 'stackoverflow'
        }
        self.url = 'https://api.stackexchange.com/2.3/search/advanced/'

    def get_question_python(self):
        response = requests.get(self.url, params=self.params)
        response.raise_for_status()
        items_json = response.json()
        items = items_json['items']

        count = 1  # Счётчик вопросов
        for elem in items:
            print(f'{count}. {elem["title"]}')
            count += 1


if __name__ == '__main__':
    ###
    # Задача №1
    # Кто самый умный супергерой?
    print('Задача №1')
    pprint(SuperHero().who_is_the_smartest(['Hulk', 'Captain_America', 'Thanos']))
    ###

    ###
    # Задача №2
    # Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на
    # Яндекс.Диск с таким же именем. Получить путь к загружаемому файлу и токен от пользователя  # noqa
    print('Задача №2')
    path_to_file = input('Укажите путь к файлу который хотите загрузить на Я.Диск:\n')
    token = input('Укажите ваш токен Я.Диска:\n')
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
    ###

    ###
    # Задача №3(необязательная)
    # Нужно написать программу, которая выводит все вопросы за последние два дня и содержит тэг 'Python'
    print('Задача №3')
    StackOverFlow().get_question_python()
    ###
