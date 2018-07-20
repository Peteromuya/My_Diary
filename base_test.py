"""Authenticate a user and an admin to be used during testing
Set up required items to be used during testing
"""
# pylint: disable=W0612
import unittest
import json
from werkzeug.security import generate_password_hash


import sys  # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app


class BaseTests(unittest.TestCase):
    """Authenticate a user and an admin and make the tokens available. Create a diary and request""" 

    def setUp(self):
        self.application = create_app()
        self.app = self.application.test_client

        admin_reg = json.dumps({
            "username": "admin",
            "email": "admin@gmail.com",
            "password": "12345678",
            "confirm_password": "12345678",
            "admin": True})

        user_reg = json.dumps({
            "username": "marcus",
            "email": "marcusrashford@gmail.com",
            "password": "secret12345",
            "confirm_password": "secret12345"})

        admin_log = json.dumps({
            "email": "admin@gmail.com",
            "password": "12345678"})

        user_log = json.dumps({
            "email": "marcusrashford@gmail.com",
            "password": "rashford12345"})

        
        self.app = self.application.test_client()
     

        create_user = self.app.get(
            '/api/v1/create_test_user',
            content_type='application/json')

        
        self.register_user = self.app.post(
            '/api/v1/auth/signup', data=user_reg,
            content_type='application/json')
        print(self.register_user.data)

        user_result = self.app.post(
            '/api/v1/auth/login', data=user_log,
            content_type='application/json')
        print(user_result.status_code)
       

if __name__ == '__main__':
    unittest.main() 
        


    self.user_response = json.loads(user_result.get_data(as_text=True))
        
    user_token = user_response["token"]
    self.user_header = {"Content-Type" : "application/json", "x-access-token" : user_token}

    

    diary = json.dumps(
        {"diary_no.": "010", "to-do": "Going to church"})
    entry = json.dumps(
        {"entry_option": "010", "entry_pass": "564"})

        
    create_diary = self.app.post(
        '/api/v1/diaries', data=diary, content_type='application/json',
        headers=self.admin_header)
    create_entry = self.app.post(
        '/api/v1/entries', data=create_entry, content_type='application/json',
        headers=self.admin_header)


    def tearDown(self):
        with self.application.app_context():
             all_users = {}
             user_count = 1

             all_diaries = {}
             diary_count = 1

             all_entries = {}
             entry_count = 1




                 
