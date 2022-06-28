from pprint import pprint

import requests

TOKEN = 'AQAAAAAIW_6wAADLW96xU0Wfq0PLv6PWycpdKTc'  # noqa


class YandexDisk:

    def __int__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()


if __name__ == '__main__':
    ya = YandexDisk()
    pprint(ya.get_files_list())
