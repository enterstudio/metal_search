import unittest

import app
from search import search_apmex
from search import search_provident
from search import search_shinybars
from search import search_goldeneaglecoins
from search import search_silvertowne
from search import search_gainesvillecoins


class SearchTestCase(unittest.TestCase):
    query1 = 'johnson matthey'
    query2 = 'atlantis mint'
    query3 = 'panda'
    query4 = 'silverbug'

    def test_apmex(self):
        res = search_apmex(self.query1)
        self.assertIsNotNone(res)

    def test_provident(self):
        res = search_provident(self.query1)
        self.assertIsNotNone(res)

    def test_shinybars(self):
        res = search_shinybars(self.query4)
        self.assertIsNotNone(res)
    
    def test_goldeneagle(self):
        res = search_goldeneaglecoins(self.query1)
        self.assertIsNotNone(res)

    def test_silvertowne(self):
        res = search_silvertowne(self.query3)
        self.assertIsNotNone(res)

    def test_gainesville(self):
        res = search_gainesvillecoins(self.query1)
        self.assertIsNotNone(res)


class ApiTestCase(unittest.TestCase):
    query1 = 'johnson matthey'
    query2 = 'panda'
    query3 = 'silverbug'

    def setUp(self):
        self.app = app.app.test_client()

    def test_apmex(self):
        rv = self.app.post('/api/apmex', data={'query': self.query1})
        assert b'img' in rv.data

    def test_provident(self):
        rv = self.app.post('/api/provident', data={'query': self.query1})
        assert b'img' in rv.data

    def test_shinybars(self):
        rv = self.app.post('/api/shinybars', data={'query': self.query3})
        assert b'img' in rv.data

    def test_goldeneagle(self):
        rv = self.app.post('/api/goldeneagle', data={'query': self.query1})
        assert b'img' in rv.data

    def test_silvertowne(self):
        rv = self.app.post('/api/silvertowne', data={'query': self.query2})
        assert b'img' in rv.data

    def test_gainesville(self):
        rv = self.app.post('/api/gainesville', data={'query': self.query1})
        assert b'img' in rv.data


if __name__ == '__main__':
    unittest.main()

