from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.eats.tests import utils
from apps.eats.models import Institution, Dish, Ingredient


class DishAPITests(APITestCase):
    def setUp(self):
        self.user_owner, self.owner_token = utils.create_user(
            username='test_user',
            email='test@test.ru',
            password='pass_test',
        )
        self.another_user, self.another_user_token = utils.create_user(
            username='test_user1',
            email='test1@test.ru',
            password='pass_test',
        )
        self.institution = Institution.objects.create(
            name='test',
            address="пр. Мира 22",
            working_hours_begin='10:00',
            working_hours_end='11:00',
            owner_id=self.user_owner.id,
        )
        self.institution.save()
        self.ingredient = Ingredient.objects.create(
            name='ingredient_1',
            calories_value=100,
        )
        self.dish_data = {
            'name': 'pizza',
            'price': 300,
            'institution': self.institution.id,
            'ingredients': [
                self.ingredient.id,
            ],
        }
        self.dish = Dish.objects.create(
            name=self.dish_data['name'],
            institution_id=self.dish_data['institution'],
            price=self.dish_data['price'],
        )
        self.dish.ingredients.add(self.ingredient)
        self.dish.save()

    def test_dish_update_action_only_by_owner(self):
        """
        Test: Dish PUT doesn't work without owner's authtoken
        """
        self.dish_data['name'] = 'updated_name'
        url = reverse('dishes-detail', args=(self.dish.id,))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.another_user_token[0].key)
        response = self.client.put(url, self.dish_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token[0].key)
        response = self.client.put(url, self.dish_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.dish_data['name'])

    def test_dish_partial_update_action_only_by_owner(self):
        """
        Test: Dish PATCH doesn't work without owner's authtoken
        """
        self.dish_data['name'] = 'updated_name'
        url = reverse('dishes-detail', args=(self.dish.id,))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.another_user_token[0].key)
        response = self.client.put(url, self.dish_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token[0].key)
        response = self.client.patch(url, self.dish_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.dish_data['name'])

    def test_dish_delete_action_by_owner(self):
        """
        Test: Dish DELETE doesn't work without owner's authtoken
        """
        url = reverse('dishes-detail', args=(self.dish.id,))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.another_user_token[0].key)
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token[0].key)
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
