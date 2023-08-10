import pytest

from apis.wework_party import WeworkParty


class TestParty:
    res = {}

    def setup_class(self):
        self.party = WeworkParty()

    def teardown_class(self):
        pass

    @pytest.mark.parametrize('name', ['创建部门名称'])
    def test_add_party(self, name):
        TestParty.res = self.party.add_party(name)
        assert TestParty.res['data']['party']['name'] == name

    @pytest.mark.parametrize('update_name', ['更新部门名称'])
    def test_update_party(self, update_name):
        TestParty.res = TestParty.res['data']['party']
        other_info = {"manage": "true",
                      "viewable": "true",
                      "changeable": "true",
                      "broadcast": "true",
                      "islocked": "false",
                      "_path": "",
                      "name_en": ""}
        TestParty.res.update(other_info)
        TestParty.res['name'] = update_name
        self.party.update_party(TestParty.res)

    def test_delete_party(self):
        self.party.delete_party(TestParty.res)
