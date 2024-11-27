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

from search.models.search_write_response import SearchWriteResponse

class TestSearchWriteResponse(unittest.TestCase):
    """SearchWriteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchWriteResponse:
        """Test SearchWriteResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchWriteResponse`
        """
        model = SearchWriteResponse()
        if include_optional:
            return SearchWriteResponse(
                index = '',
                errors = [
                    search.models.search_write_error.searchWriteError(
                        code = '', 
                        document_key_name = '', 
                        document_key_value = '', 
                        message = '', )
                    ]
            )
        else:
            return SearchWriteResponse(
                index = '',
        )
        """

    def testSearchWriteResponse(self):
        """Test SearchWriteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()