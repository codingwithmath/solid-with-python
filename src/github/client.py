import requests
import json


class Github(object):
    BASE_URL = "https://api.github.com"

    def __init__(self, user):
        self._user = user

    @classmethod
    def handle_request(cls, endpoint, method="GET", data={}):
        try:
            url = f"{cls.BASE_URL}/{endpoint}"
            print(f"URL que será chamada: {url}")

            payload = {"json": data}
            print(f"Body: {json.dumps(data, indent=2, default=str)}")

            response = requests.request(method=method, url=url)
            return response.json()
        except Exception as error:
            error_message = error
        raise Exception(f"Error while handle request: {error_message}")

    def get_repos_by_user(self):
        endpoint = f'users/{self._user}/repos'
        response = self.handle_request(endpoint=endpoint, method="GET")
        return response
