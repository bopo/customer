'''
Created by auto_sdk on 2015.08.26
'''
from top.api.base import RestApi


class OpenimTribeModifytribeinfoRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.notice = None
        self.tribe_id = None
        self.tribe_name = None
        self.user = None

    def getapiname(self):
        return 'taobao.openim.tribe.modifytribeinfo'
