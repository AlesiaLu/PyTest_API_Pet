import json
import requests
import uuid
from settings import VALID_EMAIL, VALID_PASSWORD


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_register_delete_user(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным валидным email и
        password и удаления данного пользователя"""
        email = uuid.uuid4().hex
        data = {"email": f'alesia@{email}.ru',
                "password": '1234',
                "confirm_password": '1234'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers)
        status = res.status_code
        my_id = res.json().get('id', {})
        return status, my_id

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным валидным email и
        password"""
        data = {"email": VALID_EMAIL,
                "password": VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self) -> json:
        """Запрос к Swagger сайта для получения ID пользователя по указанному уникальному токену"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        my_id = res.text
        return status, my_id

    def post_pet(self) -> json:
        """Запрос к Swagger сайта для создания животного по указанному уникальному токену и информации о животном"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"name": 'Murka', "type": 'cat', "age": 3, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def post_pet_image(self) -> json:
        """Запрос к Swagger сайта для загрузки фото животного по указанному уникальному токену и ссылке на фото"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': ('cat.jpg', open('/Users/alesyalu/PycharmProjects/PyTest_API_Pet/tests/photo/cat.jpg', 'rb'),
                         'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def get_pet(self) -> json:
        """Запрос к Swagger сайта для получения информации о животном по указанному ID животного"""
        pet_id = Pets().post_pet()[0]
        res = requests.get(self.base_url + f'pet/{pet_id}')
        status = res.status_code
        pet_name = res.json().get('pet', {}).get('name')
        pet_type = res.json().get('pet', {}).get('type')
        pet_age = res.json().get('pet', {}).get('age')
        return status, pet_name, pet_type, pet_age

    def patch_pet(self) -> json:
        """Запрос к Swagger сайта для обновления животного по указанному уникальному токену и новой информации о
        животном"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id, "name": 'Tuzik', "type": 'dog'}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        pet_id = res.json()['id']
        return pet_id, status

    def put_pet_like(self) -> json:
        """Запрос к Swagger сайта для добавления лайка животному по указанному уникальному токену и ID животного"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        return status

    def delete_pet(self) -> json:
        """Запрос к Swagger сайта для удаления животного по указанному уникальному токену и ID животного"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        pet_id = res.json().get('pet', {})
        return status, pet_id


Pets().get_register_delete_user()
Pets().get_token()
Pets().get_list_users()
Pets().post_pet()
Pets().post_pet_image()
Pets().get_pet()
Pets().patch_pet()
Pets().put_pet_like()
Pets().delete_pet()
