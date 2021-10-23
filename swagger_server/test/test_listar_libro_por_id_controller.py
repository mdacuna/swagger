# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book_response import BookResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestListarLibroPorIDController(BaseTestCase):
    """ListarLibroPorIDController integration test stubs"""

    def test_search_book_id(self):
        """Test case for search_book_id

        Escribir ID del libro
        """
        response = self.client.open(
            '/mdacuna/ApiRest/1.0.0/books/2',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
