import  app

#定义获取业务节点树的类
class GetTreeAPI():
    def __init__(self):
        #接口的路径
        self.getTree_url = app.BASE_URL + '/api/AutoModule/GetTree'

    def getTree(self,session,userName='111',MenuType='222'):
        url = self.getTree_url+MenuType+userName
        print(url)
        response = session.get(url)
        return  response
