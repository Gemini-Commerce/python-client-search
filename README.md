# search_client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.1
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Gemini-Commerce/python-client-search.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Gemini-Commerce/python-client-search.git`)

Then import the package:
```python
import search
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import search
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import search
from search.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://search.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = search.Configuration(
    host = "https://search.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: standardAuthorization
configuration.api_key['standardAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standardAuthorization'] = 'Bearer'

# Configure API key authorization: geminiAuthorization
configuration.api_key['geminiAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['geminiAuthorization'] = 'Bearer'


# Enter a context with an instance of the API client
with search.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search.SearchApi(api_client)
    body = search.SearchConfigRequest() # SearchConfigRequest | 

    try:
        # Indexes configuration
        api_response = api_instance.search_configuration(body)
        print("The response of SearchApi->search_configuration:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchApi->search_configuration: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://search.api.gogemini.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SearchApi* | [**search_configuration**](docs/SearchApi.md#search_configuration) | **POST** /search.Search/Configuration | Indexes configuration
*SearchApi* | [**search_delete**](docs/SearchApi.md#search_delete) | **POST** /search.Search/Delete | Delete Indexes
*SearchApi* | [**search_insert_or_replace**](docs/SearchApi.md#search_insert_or_replace) | **POST** /search.Search/InsertOrReplace | Insert or replace documents to different elasticsearch indexes
*SearchApi* | [**search_m_search**](docs/SearchApi.md#search_m_search) | **POST** /search.Search/MSearch | Send queries to different elasticsearch indexes
*SearchApi* | [**search_update**](docs/SearchApi.md#search_update) | **POST** /search.Search/Update | Update documents to different elasticsearch indexes


## Documentation For Models

 - [ParamSortOrder](docs/ParamSortOrder.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [SearchAggrMap](docs/SearchAggrMap.md)
 - [SearchConfigRequest](docs/SearchConfigRequest.md)
 - [SearchConfigSchema](docs/SearchConfigSchema.md)
 - [SearchConfigSchemaAttribute](docs/SearchConfigSchemaAttribute.md)
 - [SearchConfigSchemaAttributeType](docs/SearchConfigSchemaAttributeType.md)
 - [SearchConfigSchemaFacet](docs/SearchConfigSchemaFacet.md)
 - [SearchConfigSchemaFilter](docs/SearchConfigSchemaFilter.md)
 - [SearchConfigSchemaSearchable](docs/SearchConfigSchemaSearchable.md)
 - [SearchConfigSchemaSortable](docs/SearchConfigSchemaSortable.md)
 - [SearchDeleteConstraints](docs/SearchDeleteConstraints.md)
 - [SearchDeleteError](docs/SearchDeleteError.md)
 - [SearchDeleteRequest](docs/SearchDeleteRequest.md)
 - [SearchDeleteResponse](docs/SearchDeleteResponse.md)
 - [SearchParamAttribute](docs/SearchParamAttribute.md)
 - [SearchParamFacet](docs/SearchParamFacet.md)
 - [SearchParamFacetType](docs/SearchParamFacetType.md)
 - [SearchParamFilter](docs/SearchParamFilter.md)
 - [SearchParamFilterType](docs/SearchParamFilterType.md)
 - [SearchParamSearchable](docs/SearchParamSearchable.md)
 - [SearchParamSort](docs/SearchParamSort.md)
 - [SearchParams](docs/SearchParams.md)
 - [SearchPayload](docs/SearchPayload.md)
 - [SearchQueryError](docs/SearchQueryError.md)
 - [SearchQueryRequest](docs/SearchQueryRequest.md)
 - [SearchQueryRequestType](docs/SearchQueryRequestType.md)
 - [SearchQueryResponse](docs/SearchQueryResponse.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchWriteError](docs/SearchWriteError.md)
 - [SearchWriteRequest](docs/SearchWriteRequest.md)
 - [SearchWriteResponse](docs/SearchWriteResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="geminiAuthorization"></a>
### geminiAuthorization

- **Type**: API key
- **API key parameter name**: X-Gem-Token
- **Location**: HTTP header

<a id="standardAuthorization"></a>
### standardAuthorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

info@gemini-commerce.com


