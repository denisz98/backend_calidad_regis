from test.test_setup import TestSetUp
from rest_framework import status
from faker import Faker
# from apps.carreras.api.viewsets import *

class TestCase(TestSetUp):
    faker = Faker()
    def test_create_user(self):
        user = {
            "username": self.faker.name(),
            "rol": "admin",
            "email": self.faker.email(),
            "name": self.faker.name(),
            "last_name": self.faker.word(),
            "password": "123456",
            }

        url = '/users/'
        response = self.client.post(url, user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data['id']
    
    def test_update_user(self):
        id = self.test_create_user()
        user ={
            "username": self.faker.name(),
            "rol": "admin",
            "email": self.faker.email(),
            "name": self.faker.name(),
            "last_name": self.faker.word(),
            "password": "123456",
            }
        url = '/users/'
        response = self.client.put(url+str(id)+'/', user, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_user(self):
        response = self.client.get("/users/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user(self):
        id = self.test_create_user()
        response = self.client.get("/users/"+str(id)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['username']

    def test_delete_user(self):
        id = self.test_create_user()
        response = self.client.delete("/users/"+str(id)+'/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_login(self):
        usermane = self.test_retrieve_user()
        login = {
            "username": usermane,
            "password": "123456",
            }

        url = '/login/'
        response = self.client.post(url, login, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data ['refresh-token']

    def test_token(self):
        usermane = self.test_retrieve_user()
        token = {
            "username": usermane,
            "password": "123456",
            }

        url = '/api/token/'
        response = self.client.post(url, token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data ['refresh']

    def test_token_refresh(self):
        refresh = self.test_token()
        token_refresh = {
            "refresh": refresh,
            }

        url = '/api/token/refresh/'
        response = self.client.post(url, token_refresh, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout (self):
        refresh_token = self.test_login()
        logout ={
            'refresh': refresh_token
        }
        url = '/logout/'
        response = self.client.post(url, logout, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_set_password(self):
        id = self.test_create_user()
        user ={
            "password": "654321",
            "password2": "654321",
            "username": self.faker.name(),
            "rol": "admin",
            "email": self.faker.email(),
            "name": self.faker.name(),
            "last_name": self.faker.word()
            }
        url = '/users/'
        response = self.client.put(url+str(id)+'/', user, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
