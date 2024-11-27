# # SearchParams
contains params needed to perform search

## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset**| **int** | number of the record where to start to take result for pagination  | [optional]
**limit**| **int** | number of search result for page  | [optional]
**term**| **str** | term to search  | [optional]
**searchables**| [**List[SearchParamSearchable]**](SearchParamSearchable.md) | list of attributes where to search the indicated term, if not indicated it uses all in those present in index configuration  | [optional]
**filters**| [**List[SearchParamFilter]**](SearchParamFilter.md) | list of attribute and relative value which you want to filter search results  | [optional]
**attributes**| [**List[SearchParamAttribute]**](SearchParamAttribute.md) | attributes that you want to be present in search results  | [optional]
**facets**| [**List[SearchParamFacet]**](SearchParamFacet.md) | list of attributes you want to create aggregation to make filter suggestion  | [optional]
**sorts**| [**List[SearchParamSort]**](SearchParamSort.md) | params to sort search results  | [optional]
**min_score**| **float** |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

