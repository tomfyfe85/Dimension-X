from django.urls import reverse

"""
Initially, the #deeX.views will render the deex_list.html template with the text "DEEX"
"""

def test_deeXs_view(client):
    url = reverse("deeXs")
    response = client.get(url)
    assert response.status_code == 200
    assert "DEEX" in response.content.decode("utf_8")


# In reverse() I also tried "deeXs/" which is the URL pattern in the main dimension_X ...
# So this will be a page where a list of posts will be displayed.
