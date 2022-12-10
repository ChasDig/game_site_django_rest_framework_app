# ----- Simple base test ----- #
def test_root_not_found_start_url(client):
    """ Test: проверяем, чтобы url('/') выдавал error_404 """

    response = client.get('/')
    assert response.status_code == 404
