import pytest

if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir=./allure-results', '--junit-xml=./junit-result/result.xml'])
