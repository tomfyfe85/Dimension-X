import pytest

from .models import DeeX


@pytest.mark.django_db
def test_deeX_model():
    deeX = DeeX.objects.create(full_name="Test Name")
    name = DeeX.objects.all()[0].full_name
    assert name == "Test Name"
