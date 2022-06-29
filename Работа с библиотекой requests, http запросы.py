from pprint import pprint

import requests


# TOKEN = 'AQAAAAAIW_6wAADLW96xU0Wfq0PLv6PWycpdKTc'  # noqa


class YandexDisk:

    def __init__(self):
        self.token = 'AQAAAAAIW_6wAADLW96xU0Wfq0PLv6PWycpdKTc'  # noqa

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

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href_json = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_json.get['href']
        pprint(href)
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()  # If status code is not 2##, break func, and error
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    ya = YandexDisk()
    # pprint(ya.get_files_list())
    file_txt = '/home/nik/Рабочий стол/Netology/test_upload_file.txt'
    ya.upload_file_to_disk('netology/Test_file.txt', file_txt)  # noqa
