# search.SearchApi

All URIs are relative to *https://search.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_configuration**](SearchApi.md#search_configuration) | **POST** /search.Search/Configuration | Indexes configuration
[**search_delete**](SearchApi.md#search_delete) | **POST** /search.Search/Delete | Delete Indexes
[**search_insert_or_replace**](SearchApi.md#search_insert_or_replace) | **POST** /search.Search/InsertOrReplace | Insert or replace documents to different elasticsearch indexes
[**search_m_search**](SearchApi.md#search_m_search) | **POST** /search.Search/MSearch | Send queries to different elasticsearch indexes
[**search_update**](SearchApi.md#search_update) | **POST** /search.Search/Update | Update documents to different elasticsearch indexes


# **search_configuration**
> object search_configuration(body)

Indexes configuration

Create or update indexes by a passed configuration schema

### Example

* Api Key Authentication (standardAuthorization):
* Api Key Authentication (geminiAuthorization):

```python
import search
from search.models.search_config_request import SearchConfigRequest
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
    except Exception as e:
        print("Exception when calling SearchApi->search_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchConfigRequest**](SearchConfigRequest.md)|  | 

### Return type

**object**

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [geminiAuthorization](../README.md#geminiAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_delete**
> SearchDeleteResponse search_delete(body)

Delete Indexes

Delete indexes from ElasticSearch and Cassandra configuration

### Example

* Api Key Authentication (standardAuthorization):
* Api Key Authentication (geminiAuthorization):

```python
import search
from search.models.search_delete_request import SearchDeleteRequest
from search.models.search_delete_response import SearchDeleteResponse
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
    body = search.SearchDeleteRequest() # SearchDeleteRequest | 

    try:
        # Delete Indexes
        api_response = api_instance.search_delete(body)
        print("The response of SearchApi->search_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchDeleteRequest**](SearchDeleteRequest.md)|  | 

### Return type

[**SearchDeleteResponse**](SearchDeleteResponse.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [geminiAuthorization](../README.md#geminiAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_insert_or_replace**
> SearchWriteResponse search_insert_or_replace(body)

Insert or replace documents to different elasticsearch indexes

Insert or replace a document or more in a specified ElasticSearch index of a tenant

### Example

* Api Key Authentication (standardAuthorization):
* Api Key Authentication (geminiAuthorization):

```python
import search
from search.models.search_write_request import SearchWriteRequest
from search.models.search_write_response import SearchWriteResponse
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
    body = search.SearchWriteRequest() # SearchWriteRequest | 

    try:
        # Insert or replace documents to different elasticsearch indexes
        api_response = api_instance.search_insert_or_replace(body)
        print("The response of SearchApi->search_insert_or_replace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_insert_or_replace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchWriteRequest**](SearchWriteRequest.md)|  | 

### Return type

[**SearchWriteResponse**](SearchWriteResponse.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [geminiAuthorization](../README.md#geminiAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_m_search**
> SearchQueryResponse search_m_search(body)

Send queries to different elasticsearch indexes

MSearch promises to send a list of queries to elasticsearch to be executed on different indexes, it can also be used as an autocomplete by adding the corresponding TYPE

### Example

* Api Key Authentication (standardAuthorization):
* Api Key Authentication (geminiAuthorization):

```python
import search
from search.models.search_query_request import SearchQueryRequest
from search.models.search_query_response import SearchQueryResponse
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
    body = search.SearchQueryRequest() # SearchQueryRequest | 

    try:
        # Send queries to different elasticsearch indexes
        api_response = api_instance.search_m_search(body)
        print("The response of SearchApi->search_m_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_m_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchQueryRequest**](SearchQueryRequest.md)|  | 

### Return type

[**SearchQueryResponse**](SearchQueryResponse.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [geminiAuthorization](../README.md#geminiAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_update**
> SearchWriteResponse search_update(body)

Update documents to different elasticsearch indexes

Update a document or more in a specified ElasticSearch index of a tenant

### Example

* Api Key Authentication (standardAuthorization):
* Api Key Authentication (geminiAuthorization):

```python
import search
from search.models.search_write_request import SearchWriteRequest
from search.models.search_write_response import SearchWriteResponse
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
    body = search.SearchWriteRequest() # SearchWriteRequest | 

    try:
        # Update documents to different elasticsearch indexes
        api_response = api_instance.search_update(body)
        print("The response of SearchApi->search_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchWriteRequest**](SearchWriteRequest.md)|  | 

### Return type

[**SearchWriteResponse**](SearchWriteResponse.md)

### Authorization

[standardAuthorization](../README.md#standardAuthorization), [geminiAuthorization](../README.md#geminiAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

