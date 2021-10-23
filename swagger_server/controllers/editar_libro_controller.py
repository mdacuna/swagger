import connexion
import six

from swagger_server.models.book_response import BookResponse  # noqa: E501
from swagger_server import util


def edit_book(body=None):  # noqa: E501
    """Proporcionar la ID del libro a editar

    Editar o agregar nuevas caracteristicas a un libro de la lista # noqa: E501

    :param body: Formato para editar un libro
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = BookResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
