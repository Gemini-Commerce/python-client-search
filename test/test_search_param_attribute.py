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

from search.models.search_param_attribute import SearchParamAttribute

class TestSearchParamAttribute(unittest.TestCase):
    """SearchParamAttribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchParamAttribute:
        """Test SearchParamAttribute
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchParamAttribute`
        """
        model = SearchParamAttribute()
        if include_optional:
            return SearchParamAttribute(
                attribute = ''
            )
        else:
            return SearchParamAttribute(
                attribute = '',
        )
        """

    def testSearchParamAttribute(self):
        """Test SearchParamAttribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()