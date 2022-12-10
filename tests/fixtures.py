import pytest


# ----- Fixture for game_test.test_game_create ----- #

@pytest.fixture
@pytest.mark.django_db
def moderator_token(client, django_user_model):
    """ Fixture: Вход Moderator на сайт и получение token """

    username = "username_test"
    password = "password_test"
    role = "moderator"

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role=role
    )

    response = client.post(
        '/user/login/',
        {
            "username": username,
            "password": password,
        },
        format='json'
    )

    return response.data["token"]
