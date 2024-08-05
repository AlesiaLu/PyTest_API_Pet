from api import Pets

pt = Pets()


def test_register_delete_user():
    status = pt.get_register_delete_user()[0]
    my_id = pt.get_register_delete_user()[1]
    assert status == 200
    assert my_id == {}


def test_get_token():
    status = pt.get_token()[1]
    token = pt.get_token()[0]
    assert token
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    my_id = pt.get_list_users()[1]
    assert status == 200
    assert my_id


def test_post_pet():
    status = pt.post_pet()[1]
    pet_id = pt.post_pet()[0]
    assert status == 200
    assert pet_id


def test_post_pet_image():
    status = pt.post_pet_image()[0]
    link = pt.post_pet_image()[1]
    assert status == 200
    assert link


def test_get_pet():
    status = pt.get_pet()[0]
    pet_name = pt.get_pet()[1]
    pet_type = pt.get_pet()[2]
    pet_age = pt.get_pet()[3]
    assert status == 200
    assert pet_name
    assert pet_type
    assert pet_age


def test_patch_pet():
    status = pt.patch_pet()[1]
    pet_id = pt.patch_pet()[0]
    assert status == 200
    assert pet_id


def test_put_pet_like():
    status = pt.put_pet_like()
    assert status == 200


def test_delete_pet():
    status = pt.delete_pet()[0]
    pet_id = pt.delete_pet()[1]
    assert status == 200
    assert pet_id == {}
