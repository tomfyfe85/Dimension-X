from django.urls import reverse
from .. import views
"""
Initially, the #deeX.views will render the deex_list.html template with the text "DEEX"
"""

def test_deeX_view(client):
    url = reverse("")
    response = client.get(url)
    assert response.status_code == 200
    assert "DEEX" in response.content.decode("utf_8")


# In reverse() I also tried "deeXs/" which is the URL pattern in the main dimension_X ...
# So this will be a page where a list of posts will be displayed.
