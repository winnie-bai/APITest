import pytest

if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir=./result', '--junit-xml=./junit-result/result.xml'])
