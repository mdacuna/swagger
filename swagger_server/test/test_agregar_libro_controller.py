# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book_response import BookResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAgregarLibroController(BaseTestCase):
    """AgregarLibroController integration test stubs"""

    def test_agregar_libro(self):
        """Test case for agregar_libro

        Agregar un libro a la lista
        """
        body = BookResponse()
        response = self.client.open(
            '/mdacuna/ApiRest/1.0.0/books',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
