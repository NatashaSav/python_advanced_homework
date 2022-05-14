import unittest

from main import check_document_existance, get_doc_owner_name, add_new_shelf, remove_doc_from_shelf, add_new_doc, \
    delete_doc, show_all_docs_info, append_doc_to_shelf, documents
from unittest.mock import patch



class Test_Accounting(unittest.TestCase):

    def test_check_document_existance(self):
        result = check_document_existance('11-2')
        return self.assertTrue(result)

    @patch('main.get_input', return_value='10006')
    def test_get_owner_name(self, input):
        actual_name = get_doc_owner_name()
        expected_name = 'Аристарх Павлов'
        self.assertEqual(actual_name, expected_name)

    def test_add_new_shelf(self):
         append_doc_to_shelf('345', '4')
         self.assertIn('4', add_new_shelf('4'))

    def test_remove_doc_from_shelf(self):
        self.test_add_new_shelf()
        shelf = remove_doc_from_shelf('345')
        self.assertNotIn('4', documents)


    @patch('main.input', create=True)
    def test_add_new_doc(self, mock_input):
        mock_input.side_effect = ['12345', 'test_type', 'Иван Тарасов', 4]
        add_new_doc()
        self.assertIn({'type': 'test_type', 'number': '12345', 'name': 'Иван Тарасов'}, show_all_docs_info())

    @patch('main.input', create=True)
    def test_delete_doc(self, mock_input):
        mock_input.side_effect = ['12345']
        delete_doc()
        self.assertNotIn({'type': 'test_type', 'number': '12345', 'name': 'Иван Тарасов'}, show_all_docs_info())











