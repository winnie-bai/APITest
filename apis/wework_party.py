from base_api.base_api import BaseApi


class WeworkParty(BaseApi):

    def add_party(self, name):
        '''
        :param name: 添加部门名称
        :return: 响应结果
        '''
        add_data = {"parentid": 1688855106488662,
                    "name": name}
        r = self.send('post', 'wework_admin/party?action=addparty', data=add_data)
        return r

    def update_party(self, data):
        ''' 修改部门名称
        :param data: 请求参数
        :return:
        '''
        r = self.send('put', 'wework_admin/party?action=setparty', data=data)
        return r

    def delete_party(self, data):
        '''
        删除部门
        :param data: 请求参数
        :return:
        '''
        r = self.send('DELETE', 'wework_admin/party?action=delparty', data=data)
        return r
