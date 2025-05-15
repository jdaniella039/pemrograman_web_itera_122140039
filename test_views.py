import unittest
from pyramid import testing

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home_view(self):
        from pemweb.views import home
        request = testing.DummyRequest()
        response = home(request)
        assert response['message'] == 'API Mahasiswa aktif'
