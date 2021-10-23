# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BookListResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, title: str=None, description: str=None, author: str=None):  # noqa: E501
        """BookListResponse - a model defined in Swagger

        :param id: The id of this BookListResponse.  # noqa: E501
        :type id: str
        :param title: The title of this BookListResponse.  # noqa: E501
        :type title: str
        :param description: The description of this BookListResponse.  # noqa: E501
        :type description: str
        :param author: The author of this BookListResponse.  # noqa: E501
        :type author: str
        """
        self.swagger_types = {
            'id': str,
            'title': str,
            'description': str,
            'author': str
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'description': 'description',
            'author': 'author'
        }
        self._id = id
        self._title = title
        self._description = description
        self._author = author

    @classmethod
    def from_dict(cls, dikt) -> 'BookListResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BookListResponse of this BookListResponse.  # noqa: E501
        :rtype: BookListResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this BookListResponse.


        :return: The id of this BookListResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this BookListResponse.


        :param id: The id of this BookListResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this BookListResponse.


        :return: The title of this BookListResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this BookListResponse.


        :param title: The title of this BookListResponse.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this BookListResponse.


        :return: The description of this BookListResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this BookListResponse.


        :param description: The description of this BookListResponse.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def author(self) -> str:
        """Gets the author of this BookListResponse.


        :return: The author of this BookListResponse.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """Sets the author of this BookListResponse.


        :param author: The author of this BookListResponse.
        :type author: str
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author