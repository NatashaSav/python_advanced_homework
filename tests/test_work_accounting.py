import sys
import unittest
from unittest import mock

import tests
from pycparser.plyparser import parameterized
from zope.interface import document

from main import check_document_existance, get_doc_owner_name, add_new_shelf, remove_doc_from_shelf, add_new_doc, \
    delete_doc, get_input, show_all_docs_info, show_document_info
from unittest.mock import MagicMock, patch



class Test_Accounting(unittest.TestCase):

    def test_check_document_existance(self):
        result = check_document_existance('11-2')
        return self.assertTrue(result)

    @patch('main.get_input', return_value='10006')
    def test_get_owner_name(self, input):
        get_name = get_doc_owner_name()
        self.assertTrue(type(get_name), "str")

    def test_add_new_shelf(self):
        new_shelf = add_new_shelf('4')
        self.assertTrue(new_shelf)

    def test_remove_doc_from_shelf(self):
        shelf = remove_doc_from_shelf(4)
        show_all_docs_info()
        if not shelf:
            self.assertIsNone(shelf)


    @patch('main.input', create=True)
    def test_add_new_doc(self, mock_input):
        mock_input.side_effect = ['12345', 'test_type', 'Иван Тарасов', 4]
        add_new_doc()
        self.assertIn({'type': 'test_type', 'number': '12345', 'name': 'Иван Тарасов'}, show_all_docs_info())
        # self.assertIn('test_type', show_all_docs_info())
        # self.assertIn('Иван Тарасов', show_all_docs_info())







