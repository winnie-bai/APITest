import requests

from utils.log_utils import logger
from utils.yaml_utils import open_yaml


class BaseApi:

    def __init__(self):
        self.url = open_yaml('test.yaml')['env']

    def __set_headers(self, request_args: dict):

        headers = open_yaml('cookie.yaml')
        if request_args.get('headers'):
            request_args['headers'].update(headers)
        else:
            request_args['headers'] = headers

        return request_args

    def send(self, method, path, **kwargs):
        kwargs = self.__set_headers(kwargs)
        proxy = {'http': 'http://127.0.0.1:8888',
                 'https': 'http://127.0.0.1:8888'}
        # r = requests.request(method=method, url=self.url + path, proxies=proxy, **kwargs, verify=False)
        r = requests.request(method=method, url=self.url + path, **kwargs)
        logger.debug(f"{self.url + path}请求响应结果为{r.json()}")
        return r.json()
