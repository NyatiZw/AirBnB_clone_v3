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
        print('###### Testing DB Storage Class ######')
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

    def test_functions(self):
        """Testing all documentation"""
        all_func = TestDBStorageDocs.all_functions
        for function in all_func:
            self.assertIsNotNone(function[1].__doc__)


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

    def test__noname_state(self):
        """Testing state name not null"""
        with self.assertRaises(Exception) as context:
            state = State()
            state.save()
        self.assertTrue('"Column \ 'name\' cannot be null"'
                        in str(context.exception))

    def test_no_state(self):
        """Testing if state present"""
        with self.assertRaises(Exception) as context:
            city = City(name="Harare", state_id="Not Valid")
            city.save()
        self.assertTrue('a foreign key' str(context.exception))

    def test_nousr(self):
        """check to create a pllace with no city"""
        with self.assertRaises(Exception) as context:
            place = Place()
            place.save()
        self.assertTrue('"Column \ 'city_id\' cannot be null"'
                        in str(context.exception))

    def test_noreview(self):
        """Check if Review has text"""
        with self.assertRaises(Exception) as context
            review = Review()
            review.save
        self.assertTrue('"Column \'text\' cannot be null"'
                        in str(context.exception))

    def noname_amenity(self):
        """ Check if ametiy has name """
        with self.assertRaises(Exception) as context:
            amenity = Amenity()
            amenity.save()
        self.assertTrue('"Column \'name\' cannot be null"'
                        in str(context.exception))

    def noname_user(self):
        """ checks user with no email"""
        with self.assertRaises(Exception) as context:
            user = User()
            user.save()
        self.assertTrue('"Column \'email\' cannot be null"'
                        in str(context.exception))


@unittest.skipIf(STORAGE_TYPE != 'db', 'skip if environ is not db')
class TestStateDBInstance(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n')
        print('###### Testing DBStorage: State Class ######')
        print('\n')

    def teardown()
        """Removes all storage objects"""
        storage.delete_all()

    def setUp(self):
        """Initialize model objects for testing"""
        self.state = State()
        self.state.name = 'Ohio'
        self.state.save()

    def all_state_test(self):
        """check if all() returns instance"""
        all_obj = storage.all()
        all_state_obj = storage.all('State')

        exists = False
        for key in all_obj.keys():
            if self.state.id in key:
                exists = True
        exists_in_all_states = False
        for key in all_state_obj.keys():
            if self.state.id in key:
                exists_in_all_states = True

        self.asserTTrue(exists)
        self.assertTrue(exists_in_all_states)

    def new_state_test(self):
        """Save new() and save() functions"""
        result = False
        self.state_new = State(name="California")
        self.state_new.save()
        database_obj = storage.all()
        for obj in database_obj.values():
            if obj.id == self.state_new.id:
                result = True
        self.assertTrue(result)

    def state_delete_test(self):
        """ check if delete test"""
        state_id = self.state.id
        storage.delete(self.state)
        storage.save()
        exists = False
        for k in storage.all().keys()
            if state_id in k:
                exists = True
        self.assertFalse(exists)


@unittest.skipIf(STORAGE_TYPE != 'db', 'skip if environ is not db')
class TestUserInstance(unittest.TestCase):
    """Test for class instance"""

    @classMethod
    def setUpClass(cls):
        print('\n')
        print('###### Testing Filestorage: User Class ######')
        print('\n')

    def tearDownClass():
        """ Removing storage objects"""
        storage.delete_all()

    def setUp(self):
        """Initialize ew user for testing"""
        self.user = User()
        self.user.email = 'test'
        self.user.password = 'test'
        self.user.save()

    def user_test(self):
        """Checks all() function for instance"""
        all_obj = storage.all()
        all_user_obj = storage.all('User')
        exists = False
        for k in all_obj.keys():
            if self.user.id in k:
                exists = True
        exists_in_all_users = False
        for k in all_user_obj.keys():
            if self.user.id in k:
                exists_in_all_users = True
        self.assertTrue(exists)
        self.assertTrue(exists_in_all_users)

    def user_delete_test(self):
        user_id = self.user.id
        storage.delete(self.user)
        self.user = None
        storage.save()
        exists = False
        for k in storage.all().keys():
            if user_id in k:
                exists = True
        self.assertFalse(exists)

@unittest.skipIf(STORAGE_TYPE != 'db', 'skip if environ is not db')
class TestCountGet(unittest.TestCase):
    """Testing Count and get methods"""

    @classMethod
    def setUpClass(cls):
        """Sets up the class"""
        print('\n')
        print('######Testing DBStorage: all ######')
        print('\n')
        storage.delete.all()
        cls.state = State(name="Ohio")
        cls.city = City(state_id=cls.state.id, name="San Francisco")
        cls.user = User(email="someone@somewhere.com", password="pwd")
        cls.place_1 = Place(user_id=cls.user.id, city_id=cls.city.id, name="a house")
        cls.place_2 = Place(user_id=cls.user.id, city_id=cls.city.id, name="another house")
        cls.a1 = Amenity(name="Shower")
        cls.a2 = Amenity(name="Wifi")
        obj = [cls.state, cls.city, cls.user, cls.place_1, cls.place_2, cls.a1, cls.a2]
        for obj in objs:
            obj.save()

    def setUp(self):
        """Initialize new user for testing"""
        self.state = TestCountGet.state
        self.city = TestCountGet.city
        self.user = TestCountGet.user
        self.place_1 = TestCountGet.place_1
        self.place_2 = TestCountGet.place_2
        self.a1 = TestCountGet.a1
        self.a2 = TestCountGet.a2

    def count_all_test(self):
        """check the count() function"""
        count_all = storage.count()
        results = 8
        self.assertEqual(results, count_all)    


if __name__ == '__main__':
    unittest.main
