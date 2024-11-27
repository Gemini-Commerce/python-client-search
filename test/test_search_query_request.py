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

from search.models.search_query_request import SearchQueryRequest

class TestSearchQueryRequest(unittest.TestCase):
    """SearchQueryRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchQueryRequest:
        """Test SearchQueryRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchQueryRequest`
        """
        model = SearchQueryRequest()
        if include_optional:
            return SearchQueryRequest(
                tenant_id = '',
                type = 'STANDARD',
                payload = [
                    search.models.search_payload.searchPayload(
                        index = '', 
                        params = search.models.search_params.searchParams(
                            offset = 56, 
                            limit = 56, 
                            term = '', 
                            searchables = [
                                search.models.search_param_searchable.searchParamSearchable(
                                    attribute = '', )
                                ], 
                            filters = [
                                search.models.search_param_filter.searchParamFilter(
                                    filter = '', 
                                    type = 'TERM', )
                                ], 
                            attributes = [
                                search.models.search_param_attribute.searchParamAttribute(
                                    attribute = '', )
                                ], 
                            facets = [
                                search.models.search_param_facet.searchParamFacet(
                                    attribute = '', 
                                    limit = 56, 
                                    name = '', )
                                ], 
                            sorts = [
                                search.models.search_param_sort.searchParamSort(
                                    attribute = '', 
                                    order = 'ASC', )
                                ], 
                            min_score = 1.337, ), )
                    ]
            )
        else:
            return SearchQueryRequest(
                payload = [
                    search.models.search_payload.searchPayload(
                        index = '', 
                        params = search.models.search_params.searchParams(
                            offset = 56, 
                            limit = 56, 
                            term = '', 
                            searchables = [
                                search.models.search_param_searchable.searchParamSearchable(
                                    attribute = '', )
                                ], 
                            filters = [
                                search.models.search_param_filter.searchParamFilter(
                                    filter = '', 
                                    type = 'TERM', )
                                ], 
                            attributes = [
                                search.models.search_param_attribute.searchParamAttribute(
                                    attribute = '', )
                                ], 
                            facets = [
                                search.models.search_param_facet.searchParamFacet(
                                    attribute = '', 
                                    limit = 56, 
                                    name = '', )
                                ], 
                            sorts = [
                                search.models.search_param_sort.searchParamSort(
                                    attribute = '', 
                                    order = 'ASC', )
                                ], 
                            min_score = 1.337, ), )
                    ],
        )
        """

    def testSearchQueryRequest(self):
        """Test SearchQueryRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()