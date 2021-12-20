import  logging
import unittest
import requests

from api.GetTreeAPI import GetTreeAPI
from utils import assert_utils

class GetTree(unittest.TestCase):
    def setUp(self) -> None:
        self.getTree_api = GetTreeAPI()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()


    def test01_getTree_success(self):
        response = self.getTree_api.getTree(self.session)
        logging.info('getTree response = {}'.format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")