import unittest

import webtest

import server

class TestCase(unittest.TestCase):

    def test_page_has_environ(self):
        testapp = webtest.TestApp(server.APP)
        response = testapp.get('/')
        self.assertNotIn('not set', response.body) 


if __name__ == '__main__':
    unittest.main()
