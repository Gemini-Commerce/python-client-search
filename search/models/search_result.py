# coding: utf-8

"""
    Search Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from search.models.search_aggr_map import SearchAggrMap
from search.models.search_params import SearchParams
from typing import Optional, Set
from typing_extensions import Self

class SearchResult(BaseModel):
    """
    contains the search results, aggregations and paging information
    """ # noqa: E501
    index: StrictStr = Field(description="index where the data were extrapolated")
    params: Optional[SearchParams] = None
    page: Optional[StrictInt] = Field(default=None, description="page number of the results you are processing")
    total_pages: Optional[StrictInt] = Field(default=None, description="number of pages of results", alias="totalPages")
    total_hits: Optional[StrictInt] = Field(default=None, description="number of total search results", alias="totalHits")
    hits: Optional[List[StrictStr]] = Field(default=None, description="search result records contained in the specified page")
    aggregations: Optional[Dict[str, SearchAggrMap]] = Field(default=None, description="array of aggregation obtained by search result")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["index", "params", "page", "totalPages", "totalHits", "hits", "aggregations"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SearchResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of params
        if self.params:
            _dict['params'] = self.params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in aggregations (dict)
        _field_dict = {}
        if self.aggregations:
            for _key_aggregations in self.aggregations:
                if self.aggregations[_key_aggregations]:
                    _field_dict[_key_aggregations] = self.aggregations[_key_aggregations].to_dict()
            _dict['aggregations'] = _field_dict
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "index": obj.get("index"),
            "params": SearchParams.from_dict(obj["params"]) if obj.get("params") is not None else None,
            "page": obj.get("page"),
            "totalPages": obj.get("totalPages"),
            "totalHits": obj.get("totalHits"),
            "hits": obj.get("hits"),
            "aggregations": dict(
                (_k, SearchAggrMap.from_dict(_v))
                for _k, _v in obj["aggregations"].items()
            )
            if obj.get("aggregations") is not None
            else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


