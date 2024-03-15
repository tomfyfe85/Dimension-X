import pytest

from .models import DeeX


@pytest.mark.django_db
def test_deeX_model():
    DeeX.objects.create(full_name="Test Name")
    assert DeeX.objects.all()[0].full_name == "Test Name"
