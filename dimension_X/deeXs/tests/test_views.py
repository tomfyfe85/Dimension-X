from django.urls import reverse

"""
Initially, the #deeX.views will render the deex_list.html template with the text "DEEX"
"""

def test_deeX_view(client):
    view = reverse('deeXs')
    response = client.get(view)
    assert response.status_code == 200
    assert "DEEX" in response.content.decode("utf_8")


# In reverse() I also tried "deeXs/" which is the URL pattern in the main dimension_X ...
# ...  folder at which brings you to the deeX app. 'deeX' is a word I made up to replace tweet, peep or xeet.
# So this will be a page where a list of posts will be displayed.
