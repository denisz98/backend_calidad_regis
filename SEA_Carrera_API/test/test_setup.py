from faker import Faker

from rest_framework import status
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):

    def setUp(self):
        from apps.user.models import User

        faker = Faker()

        self.login_url = '/login/'
        self.user = User.objects.create_superuser(
            name='denisz',
            last_name='zaldivar',
            username='denisz',
            rol = 'admin',
            password='3105',
            email=faker.email()
        )
        
        response = self.client.post(
            self.login_url,
            {
                'username': 'denisz',
                'password': '3105'
            },
            format='json'
        )
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # import pdb; pdb.set_trace()
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION= self.token)
        return super().setUp()

    # def test_jshdbjs(self):
    #     pass