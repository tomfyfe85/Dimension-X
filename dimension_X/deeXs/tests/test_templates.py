def test_deeX_template(client):
    response = client.get("/deeXs/")
    assert response.status_code == 200
    assert "DEEX" in response.content.decode("utf_8")