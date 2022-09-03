#!/usr/bin/python3
"""test module for the file storage class"""
import json
import unittest
from models import storage


class TestFileStorageClass(unittest.TestCase):
    """Test for FileStorage class methods and atrributes"""

    @classmethod
    def setUpClass(cls):
        """sets up class instance"""
        cls.testStorage = storage

    @classmethod
    def tearDownClass(cls):
        """ tear down the created class instance """
        del cls.testStorage

    def test_all_method(self):
        """test the all method whether it return all the objects and as dict"""
        objects = self.testStorage.all()
        self.assertIsInstance(objects, dict)

    def test_save_method(self):
        """test the save method to see if it saves objects to JSON file"""
        with open("file.json", 'r') as f:
            content = json.load(f)
            mytype = type(content)
            self.assertEqual(mytype, dict)

    if '__name__' == '__main__':
        unittest.main()
