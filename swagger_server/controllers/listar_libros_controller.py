import connexion
import six

from swagger_server.models.book_list_response import BookListResponse  # noqa: E501
from swagger_server import util


def search_books():  # noqa: E501
    """Obtener lista de libros

    You can search for available books in the system  # noqa: E501


    :rtype: List[BookListResponse]
    """
    return 'do some magic!'
