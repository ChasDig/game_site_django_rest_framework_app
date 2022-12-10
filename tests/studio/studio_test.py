import pytest

from game_app.models import Studio


@pytest.mark.django_db
def test_studio_list(client):
    """ Test: Тестируем данные, возвращаемые при запросе списка студий """

    studio_data = Studio.objects.create(
        name="name_studio_test"
    )

    studio_response = {
            "count": 1,
            "next": None,
        "previous": None,
        "results": [
            {
                "id": studio_data.pk,
                "name": "name_studio_test",
                "poster": None,
                "url": None
            }
        ]
    }

    response = client.get('/api/games/studio/')

    assert response.status_code == 200
    assert response.data == studio_response
