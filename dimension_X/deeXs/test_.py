import pytest
from datetime import datetime
from unittest.mock import Mock

from .models import DeeX


@pytest.mark.django_db
def test_DeeX_model():
    date_time = datetime.now()
    date_time = Mock()
    DeeX.objects.create(
        full_name="Test name",
        user_name="Test user name",
        password="TESTing1234",
        email="some_email@geemail.com",
        deeX="HI this is a DEEX",
        slug="/1",
        date_time=date_time,
    )

    assert DeeX.objects.all()[0].full_name == "Test name"
    assert DeeX.objects.all()[0].user_name == "Test user name"
    assert DeeX.objects.all()[0].password == "TESTing1234"
    assert DeeX.objects.all()[0].email == "some_email@geemail.com"
    assert DeeX.objects.all()[0].deeX == "HI this is a DEEX"
    assert DeeX.objects.all()[0].slug == "/1"
    assert DeeX.objects.all()[0].date_time == date_time

    # full_name = models.CharField(max_length=50)
    # user_name = models.CharField(max_length=50)
    # password = models.CharField(max_length=50)
    # email = models.EmailField(max_length=100)
    # deeX = models.TextField(max_length=140)
    # slug = models.SlugField()
    # time_date = models.DateTimeField(auto_now_add=True)
