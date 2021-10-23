# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestEliminarLibroController(BaseTestCase):
    """EliminarLibroController integration test stubs"""

    def test_delete_book(self):
        """Test case for delete_book

        Poner ID del libro a eliminar
        """
        response = self.client.open(
            '/mdacuna/ApiRest/1.0.0/books/2',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
