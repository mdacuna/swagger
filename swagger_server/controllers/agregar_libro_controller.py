import connexion
import six

from swagger_server.models.book_response import BookResponse  # noqa: E501
from swagger_server import util


def agregar_libro(body=None):  # noqa: E501
    """Agregar un libro a la lista

    Adds an item to the system # noqa: E501

    :param body: Formato para agregar libro
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BookResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
