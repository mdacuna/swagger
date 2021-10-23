# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book_response import BookResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEditarLibroController(BaseTestCase):
    """EditarLibroController integration test stubs"""

    def test_edit_book(self):
        """Test case for edit_book

        Proporcionar la ID del libro a editar
        """
        body = BookResponse()
        response = self.client.open(
            '/mdacuna/ApiRest/1.0.0/books/2',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
