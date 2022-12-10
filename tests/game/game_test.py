import pytest

from game_app.models import Game

@pytest.mark.django_db
def test_game_create(client, moderator_token):
    """ Test: Тестируем создание страницы с новой игрой """

    game_data = {
        "name": "name_test",
        "descriptions": "descriptions_test",
        "date_release": "2023-10-10",
        "price": 4000
    }

    game_response = {
        "name": "name_test",
        "descriptions": "descriptions_test",
        "poster": None,
        "date_add_game": None,
        "date_release": "2023-10-10",
        "price": 4000,
        "url": None,
        "studio": None,
        "author": None,
        "genre": None,
        "system_requirements": None,
        "user": None
    }

    response = client.post(
        '/api/games/game/create/',
        game_data,
        content_type='application/json',
        HTTP_AUTHORIZATION='Token '+ moderator_token
    )

    assert response.status_code == 201
    assert response.data == game_response
