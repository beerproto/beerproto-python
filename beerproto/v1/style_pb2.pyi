from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StyleCategories(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STYLE_CATEGORIES_UNSPECIFIED: _ClassVar[StyleCategories]
    STYLE_CATEGORIES_BEER: _ClassVar[StyleCategories]
    STYLE_CATEGORIES_CIDER: _ClassVar[StyleCategories]
    STYLE_CATEGORIES_KOMBUCHA: _ClassVar[StyleCategories]
    STYLE_CATEGORIES_MEAD: _ClassVar[StyleCategories]
    STYLE_CATEGORIES_SODA: _ClassVar[StyleCategories]
    STYLE_CATEGORIES_WINE: _ClassVar[StyleCategories]
    STYLE_CATEGORIES_OTHER: _ClassVar[StyleCategories]
STYLE_CATEGORIES_UNSPECIFIED: StyleCategories
STYLE_CATEGORIES_BEER: StyleCategories
STYLE_CATEGORIES_CIDER: StyleCategories
STYLE_CATEGORIES_KOMBUCHA: StyleCategories
STYLE_CATEGORIES_MEAD: StyleCategories
STYLE_CATEGORIES_SODA: StyleCategories
STYLE_CATEGORIES_WINE: StyleCategories
STYLE_CATEGORIES_OTHER: StyleCategories

class StyleBase(_message.Message):
    __slots__ = ("name", "category", "category_number", "style_letter", "style_guide", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STYLE_LETTER_FIELD_NUMBER: _ClassVar[int]
    STYLE_GUIDE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    category: str
    category_number: int
    style_letter: str
    style_guide: str
    type: StyleCategories
    def __init__(self, name: _Optional[str] = ..., category: _Optional[str] = ..., category_number: _Optional[int] = ..., style_letter: _Optional[str] = ..., style_guide: _Optional[str] = ..., type: _Optional[_Union[StyleCategories, str]] = ...) -> None: ...

class StyleType(_message.Message):
    __slots__ = ("base", "id", "aroma", "ingredients", "notes", "flavor", "mouthfeel", "final_gravity", "color", "original_gravity", "examples", "carbonation", "alcohol_by_volume", "international_bitterness_units", "appearance", "overall_impression")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    AROMA_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    MOUTHFEEL_FIELD_NUMBER: _ClassVar[int]
    FINAL_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    CARBONATION_FIELD_NUMBER: _ClassVar[int]
    ALCOHOL_BY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    INTERNATIONAL_BITTERNESS_UNITS_FIELD_NUMBER: _ClassVar[int]
    APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    OVERALL_IMPRESSION_FIELD_NUMBER: _ClassVar[int]
    base: StyleBase
    id: str
    aroma: str
    ingredients: str
    notes: str
    flavor: str
    mouthfeel: str
    final_gravity: _measureable_units_pb2.GravityRangeType
    color: _measureable_units_pb2.ColorRangeType
    original_gravity: _measureable_units_pb2.GravityRangeType
    examples: str
    carbonation: _measureable_units_pb2.CarbonationRangeType
    alcohol_by_volume: _measureable_units_pb2.PercentRangeType
    international_bitterness_units: _measureable_units_pb2.BitternessRangeType
    appearance: str
    overall_impression: str
    def __init__(self, base: _Optional[_Union[StyleBase, _Mapping]] = ..., id: _Optional[str] = ..., aroma: _Optional[str] = ..., ingredients: _Optional[str] = ..., notes: _Optional[str] = ..., flavor: _Optional[str] = ..., mouthfeel: _Optional[str] = ..., final_gravity: _Optional[_Union[_measureable_units_pb2.GravityRangeType, _Mapping]] = ..., color: _Optional[_Union[_measureable_units_pb2.ColorRangeType, _Mapping]] = ..., original_gravity: _Optional[_Union[_measureable_units_pb2.GravityRangeType, _Mapping]] = ..., examples: _Optional[str] = ..., carbonation: _Optional[_Union[_measureable_units_pb2.CarbonationRangeType, _Mapping]] = ..., alcohol_by_volume: _Optional[_Union[_measureable_units_pb2.PercentRangeType, _Mapping]] = ..., international_bitterness_units: _Optional[_Union[_measureable_units_pb2.BitternessRangeType, _Mapping]] = ..., appearance: _Optional[str] = ..., overall_impression: _Optional[str] = ...) -> None: ...

class RecipeStyleType(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: StyleBase
    def __init__(self, base: _Optional[_Union[StyleBase, _Mapping]] = ...) -> None: ...
