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

from search.models.search_query_response import SearchQueryResponse

class TestSearchQueryResponse(unittest.TestCase):
    """SearchQueryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchQueryResponse:
        """Test SearchQueryResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchQueryResponse`
        """
        model = SearchQueryResponse()
        if include_optional:
            return SearchQueryResponse(
                result = [
                    search.models.search_result.searchResult(
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
                            min_score = 1.337, ), 
                        page = 56, 
                        total_pages = 56, 
                        total_hits = 56, 
                        hits = [
                            ''
                            ], 
                        aggregations = {
                            'key' : search.models.search_aggr_map.searchAggrMap(
                                results = [
                                    ''
                                    ], )
                            }, )
                    ],
                errors = [
                    search.models.search_query_error.searchQueryError(
                        code = '', 
                        message = '', )
                    ]
            )
        else:
            return SearchQueryResponse(
        )
        """

    def testSearchQueryResponse(self):
        """Test SearchQueryResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
