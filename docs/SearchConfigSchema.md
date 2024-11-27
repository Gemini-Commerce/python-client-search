# # SearchConfigSchema
contains index configurations fields

## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index**| **str** | index name, to create or where update configuration  |
**document_key_name**| **str** | field which value will be used as document id [#DOCGENBUG REQUIRED FIELD]  | [optional]
**attributes**| [**List[SearchConfigSchemaAttribute]**](SearchConfigSchemaAttribute.md) | fields that can be stored into index and later retrieved  |
**searchables**| [**List[SearchConfigSchemaSearchable]**](SearchConfigSchemaSearchable.md) | fields that can be used for fulltext searches  | [optional]
**facets**| [**List[SearchConfigSchemaFacet]**](SearchConfigSchemaFacet.md) | fields that can be used for aggregations  | [optional]
**filters**| [**List[SearchConfigSchemaFilter]**](SearchConfigSchemaFilter.md) | fields that can be used for filtering  | [optional]
**sortables**| [**List[SearchConfigSchemaSortable]**](SearchConfigSchemaSortable.md) | fields that can be used for sorting  | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

