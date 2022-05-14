import requests


class ApiYDisk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get(self, path, params):
        url = "https://cloud-api.yandex.net/v1/{}".format(path)
        return requests.get(url, headers=self.get_headers(), params=params)