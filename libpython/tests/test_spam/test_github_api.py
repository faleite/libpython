from unittest.mock import Mock

import pytest

from libpython import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/77789023?v=4'
    resp_mock.json.return_value = {
        'login': 'faleite', 'id': 77789023,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpython.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('faleite')
    assert avatar_url == url


def test_buscar_avatar_integracao():

    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars.githubusercontent.com/u/402714?v=4' == url
