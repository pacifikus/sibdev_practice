from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.eats.tests import utils
from apps.eats.models import Institution


class InstitutionAPITests(APITestCase):
    def setUp(self):
        self.institution_data = {
            "name": "test",
            "address": "пр. Мира 22",
            "working_hours_begin": '10:00',
            "working_hours_end": '20:00',
        }
        self.user_owner, self.owner_token = utils.create_user(
            username='test_user',
            email='test@test.ru',
            password='pass_test'
        )
        self.another_user, self.another_user_token = utils.create_user(
            username='test_user1',
            email='test1@test.ru',
            password='pass_test'
        )
        self.institution = Institution.objects.create(
            name=self.institution_data['name'],
            address=self.institution_data['address'],
            working_hours_begin=self.institution_data['working_hours_begin'],
            working_hours_end=self.institution_data['working_hours_end'],
            owner_id=self.user_owner.id,
        )
        self.institution.save()
        self.count_before = Institution.objects.count()

    def test_institution_list_action_allowed_to_all(self):
        """
        Test: Institution GET works for all users
        """
        url = reverse('eats-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), self.count_before)

    def test_institution_create_action_with_token(self):
        """
        Test: Institution POST works with authtoken
        """
        url = reverse('eats-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token[0].key)
        response = self.client.post(url, self.institution_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_institution_retrieve_action_allowed_to_all(self):
        """
        Test: Institution GET/id/ works for all users
        """
        url = reverse('eats-detail', args=(self.institution.id,))
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.institution.name)

    def test_institution_create_action_without_token(self):
        """
        Test: Institution POST doesn't work without authtoken
        """
        url = reverse('eats-list')
        response = self.client.post(url, self.institution_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_institution_update_action_only_by_owner(self):
        """
        Test: Institution PUT doesn't work without owner's authtoken
        """
        self.institution_data['name'] = 'updated_name'
        url = reverse('eats-detail', args=(self.institution.id,))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.another_user_token[0].key)
        response = self.client.put(url, self.institution_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token[0].key)
        response = self.client.put(url, self.institution_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.institution_data['name'])

    def test_institution_partial_update_action_only_by_owner(self):
        """
        Test: Institution PATCH doesn't work without owner's authtoken
        """
        self.institution_data['name'] = 'updated_name'
        url = reverse('eats-detail', args=(self.institution.id,))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.another_user_token[0].key)
        response = self.client.patch(url, self.institution_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token[0].key)
        response = self.client.patch(url, self.institution_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.institution_data['name'])

    def test_institution_delete_action_by_owner(self):
        """
        Test: Institution DELETE doesn't work without owner's authtoken
        """
        url = reverse('eats-detail', args=(self.institution.id,))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.another_user_token[0].key)
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token[0].key)
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
