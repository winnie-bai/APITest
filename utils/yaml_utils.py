import os.path

import yaml

from utils.log_utils import logger


def open_yaml(file_name):
    '''
    读取yaml文件
    :param file_name: 文件名
    :return:
    '''
    abs_path = os.path.dirname(os.path.dirname(__file__))
    yaml_path = os.path.join(abs_path, 'data')
    file_path = os.path.join(yaml_path, file_name)
    # print(file_path)
    if os.path.exists(file_path):
        with open(file_path, encoding='u8') as f:
            file_content = yaml.safe_load(f)
        return file_content
    else:
        logger.error(f"{file_name}文件不存在")
        return {}

# open_yaml('cookie.yaml')
