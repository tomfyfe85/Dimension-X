import pytest
from ..models import DeeX


@pytest.fixture
def create_DeeX():
    return DeeX.objects.create(
        full_name="Test name",
        user_name="Test user name",
        password="TESTing1234",
        email="some_email@geemail.com",
        deeX="HI this is a DEEX",
        slug="/1",
    )


@pytest.mark.django_db
def test_DeeX_model(create_DeeX):

    DeeX_object = DeeX.objects.all()[0]
    assert DeeX_object.id == 1
    assert DeeX_object.full_name == "Test name"
    assert DeeX_object.user_name == "Test user name"
    assert DeeX_object.password == "TESTing1234"
    assert DeeX_object.email == "some_email@geemail.com"
    assert DeeX_object.deeX == "HI this is a DEEX"
    assert DeeX_object.slug == "/1"
    assert DeeX_object.date_time == create_DeeX.date_time


