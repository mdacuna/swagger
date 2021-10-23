# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book_list_response import BookListResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestListarLibrosController(BaseTestCase):
    """ListarLibrosController integration test stubs"""

    def test_search_books(self):
        """Test case for search_books

        Obtener lista de libros
        """
        response = self.client.open(
            '/mdacuna/ApiRest/1.0.0/books',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
