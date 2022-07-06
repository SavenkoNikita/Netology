from pprint import pprint

import requests

import Secret_data


class YandexDisk:

    def __init__(self):
        self.token = Secret_data.YaDisk_token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        """Возвращает список файлов с Я.Диска"""

        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href_json = self._get_upload_link(disk_file_path=disk_file_path)
        # pprint(href_json)
        href = href_json['href']
        response = requests.put(href, data=open(filename, 'rb'))
        print(response.status_code)
        response.raise_for_status()  # If status code is not 2##, break func, and print error
        if response.status_code == 201:
            print('Success')
        else:
            print(response.status_code)


class Reddit:

    def get_popular_videos(self):
        url = 'https://www.reddit.com/r/gifs/top.json?t=day'
        response = requests.get(url, headers={'User-agent': 'netology'})  # noqa
        return response.json()


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
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # ya = YandexDisk()
    # pprint(ya.get_files_list())
    # file_txt = '/home/nik/Рабочий стол/Netology/test_upload_file.txt'  # noqa
    # ya.upload_file_to_disk('netology/Test_file.txt', file_txt)  # noqa

    # reddit = Reddit()
    # pprint(reddit.get_popular_videos())

    ###
    # Задача №1
    # Кто самый умный супергерой?
    pprint(SuperHero().who_is_the_smartest(['Hulk', 'Captain_America', 'Thanos']))
    ###

    ###
    # Задача №2
    # Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на
    # Яндекс.Диск с таким же именем.
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '/home/nik/Рабочий стол/Netology/test_upload_file.txt'
    token = Secret_data.YaDisk_token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
