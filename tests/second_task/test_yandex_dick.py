import unittest
import os
from dotenv import load_dotenv

from api_yandex_disk import ApiYDisk


class TestYandexDisk(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.yandex_service = ApiYDisk(token=os.getenv('API_TOKEN'))

    def test_check_response_is_200(self):
        response = self.yandex_service.get("disk/resources", {"path": "test_folder"}).status_code
        self.assertEqual(response, 200)

    def test_check_response_is_not_400(self):
        response = self.yandex_service.get("disk/resources", {"path": "test_folder"}).status_code
        self.assertIsNot(response, 400)

    def test_check_response_is_not_equal_500(self):
        response = self.yandex_service.get("disk/resources", {"path": "test_folder"}).status_code
        self.assertNotEqual(response, 500)

    @unittest.expectedFailure
    def test_check_response_should_be_300(self):
        response = self.yandex_service.get("disk/resources", {"path": "test_folder"}).status_code
        self.assertEqual(response, 300)

    @unittest.expectedFailure
    def test_check_response_should_be_404(self):
        response = self.yandex_service.get("disk/resources", {"path": "test_folder"}).status_code
        self.assertEqual(response, 404)

    def test(self):



