from django import urls
from django.contrib.auth import get_user_model
import pytest
from django.urls import reverse


@pytest.mark.parametrize('param', [

    ('home'),
    ('login'),
    ('register'),
    ('new-note'),

])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200



