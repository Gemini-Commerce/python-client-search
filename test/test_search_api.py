# coding: utf-8

"""
    Search Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from search.api.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SearchApi()

    def tearDown(self) -> None:
        pass

    def test_search_configuration(self) -> None:
        """Test case for search_configuration

        Indexes configuration
        """
        pass

    def test_search_delete(self) -> None:
        """Test case for search_delete

        Delete Indexes
        """
        pass

    def test_search_insert_or_replace(self) -> None:
        """Test case for search_insert_or_replace

        Insert or replace documents to different elasticsearch indexes
        """
        pass

    def test_search_m_search(self) -> None:
        """Test case for search_m_search

        Send queries to different elasticsearch indexes
        """
        pass

    def test_search_update(self) -> None:
        """Test case for search_update

        Update documents to different elasticsearch indexes
        """
        pass


if __name__ == '__main__':
    unittest.main()
