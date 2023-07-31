#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
from models import *
import json
import os
import pep8
import unittest
from models.base_model import Base
from models.engine.db_storage import DBStorage

STORAGE_TYPE = environ.get('HBNB_TYPE_STORAGE')


@unittest.skipIf(STORAGE_TYPE != 'db', 'skip if environ is not db')
class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""

    all_functions = inspect.getmembers(DBStorage, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        print('\n')
        print('###### Testing Docs ######')
        print('\n')

    def tearDown():
        """Remove storage objects"""
        storage.delete_all()

    def test_class(self):
        """Testing documentation for class"""
        expected = ('\n handles storage of all class instance\n')
        actual = DBStorage.__doc__
        self.assertEqual(expected, actual)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        errors = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

@unittest.skipif(STORAGE_TYPE != 'db', "DB Storage doesn't use FileStorage")
class TestTracebackNullError(unittest.TestCase):
    """Testing thhrowback errors"""
    def setupClass(cls):
        """set up class"""
        print('\n')
        print('###### Testing DBStorage ######')
        print('\n')

    def tearDown(self):
        """Teardown class"""
        storage.rollback_session()

    def tearDownClass():
        """Remove all storage objects"""
        storage.delete_all()

    def test_state_noname(self):
        """Testing state name not null"""
        with self.assertRaises(Exception) as context:
            s = State()
            s.save()
        self.assertTrue('"Column \ 'name\' cannot be null"'
                       in str(context.exception))

    def test_city_no_state(self):
        """Testing if state present"""
        with self.assertRaises(Exception) as context:
            c = City(name="Harare", state_id="Not Valid")
            c.save()
        self.assertTrue('a foreign key' str(context.exception))

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""


if __name__ == '__main__':
    unittest.main
