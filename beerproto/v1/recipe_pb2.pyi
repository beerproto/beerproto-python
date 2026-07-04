from beerproto.v1 import boil_pb2 as _boil_pb2
from beerproto.v1 import culture_pb2 as _culture_pb2
from beerproto.v1 import fermentable_pb2 as _fermentable_pb2
from beerproto.v1 import fermentation_pb2 as _fermentation_pb2
from beerproto.v1 import hop_pb2 as _hop_pb2
from beerproto.v1 import mash_pb2 as _mash_pb2
from beerproto.v1 import measureable_units_pb2 as _measureable_units_pb2
from beerproto.v1 import misc_pb2 as _misc_pb2
from beerproto.v1 import packaging_pb2 as _packaging_pb2
from beerproto.v1 import style_pb2 as _style_pb2
from beerproto.v1 import water_pb2 as _water_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecipeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECIPE_UNIT_UNSPECIFIED: _ClassVar[RecipeUnit]
    RECIPE_UNIT_CIDER: _ClassVar[RecipeUnit]
    RECIPE_UNIT_KOMBUCHA: _ClassVar[RecipeUnit]
    RECIPE_UNIT_SODA: _ClassVar[RecipeUnit]
    RECIPE_UNIT_OTHER: _ClassVar[RecipeUnit]
    RECIPE_UNIT_MEAD: _ClassVar[RecipeUnit]
    RECIPE_UNIT_WINE: _ClassVar[RecipeUnit]
    RECIPE_UNIT_EXTRACT: _ClassVar[RecipeUnit]
    RECIPE_UNIT_PARTIAL_MASH: _ClassVar[RecipeUnit]
    RECIPE_UNIT_ALL_GRAIN: _ClassVar[RecipeUnit]
RECIPE_UNIT_UNSPECIFIED: RecipeUnit
RECIPE_UNIT_CIDER: RecipeUnit
RECIPE_UNIT_KOMBUCHA: RecipeUnit
RECIPE_UNIT_SODA: RecipeUnit
RECIPE_UNIT_OTHER: RecipeUnit
RECIPE_UNIT_MEAD: RecipeUnit
RECIPE_UNIT_WINE: RecipeUnit
RECIPE_UNIT_EXTRACT: RecipeUnit
RECIPE_UNIT_PARTIAL_MASH: RecipeUnit
RECIPE_UNIT_ALL_GRAIN: RecipeUnit

class RecipeType(_message.Message):
    __slots__ = ("id", "efficiency", "style", "ibu_estimate", "color_estimate", "beer_ph", "name", "type", "coauthor", "original_gravity", "final_gravity", "carbonation", "fermentation", "author", "ingredients", "mash", "packaging", "boil", "taste", "calories_per_pint", "created", "batch_size", "notes", "alcohol_by_volume", "apparent_attenuation")
    ID_FIELD_NUMBER: _ClassVar[int]
    EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    IBU_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    COLOR_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    BEER_PH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COAUTHOR_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    FINAL_GRAVITY_FIELD_NUMBER: _ClassVar[int]
    CARBONATION_FIELD_NUMBER: _ClassVar[int]
    FERMENTATION_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    MASH_FIELD_NUMBER: _ClassVar[int]
    PACKAGING_FIELD_NUMBER: _ClassVar[int]
    BOIL_FIELD_NUMBER: _ClassVar[int]
    TASTE_FIELD_NUMBER: _ClassVar[int]
    CALORIES_PER_PINT_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    ALCOHOL_BY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    APPARENT_ATTENUATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    efficiency: EfficiencyType
    style: _style_pb2.RecipeStyleType
    ibu_estimate: _hop_pb2.IBUEstimateType
    color_estimate: _measureable_units_pb2.ColorType
    beer_ph: _measureable_units_pb2.AcidityType
    name: str
    type: RecipeUnit
    coauthor: str
    original_gravity: _measureable_units_pb2.GravityType
    final_gravity: _measureable_units_pb2.GravityType
    carbonation: _measureable_units_pb2.CarbonationType
    fermentation: _fermentation_pb2.FermentationProcedureType
    author: str
    ingredients: IngredientsType
    mash: _mash_pb2.MashProcedureType
    packaging: _packaging_pb2.PackagingProcedureType
    boil: _boil_pb2.BoilProcedureType
    taste: TasteType
    calories_per_pint: float
    created: str
    batch_size: _measureable_units_pb2.VolumeType
    notes: str
    alcohol_by_volume: _measureable_units_pb2.PercentType
    apparent_attenuation: _measureable_units_pb2.PercentType
    def __init__(self, id: _Optional[str] = ..., efficiency: _Optional[_Union[EfficiencyType, _Mapping]] = ..., style: _Optional[_Union[_style_pb2.RecipeStyleType, _Mapping]] = ..., ibu_estimate: _Optional[_Union[_hop_pb2.IBUEstimateType, _Mapping]] = ..., color_estimate: _Optional[_Union[_measureable_units_pb2.ColorType, _Mapping]] = ..., beer_ph: _Optional[_Union[_measureable_units_pb2.AcidityType, _Mapping]] = ..., name: _Optional[str] = ..., type: _Optional[_Union[RecipeUnit, str]] = ..., coauthor: _Optional[str] = ..., original_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., final_gravity: _Optional[_Union[_measureable_units_pb2.GravityType, _Mapping]] = ..., carbonation: _Optional[_Union[_measureable_units_pb2.CarbonationType, _Mapping]] = ..., fermentation: _Optional[_Union[_fermentation_pb2.FermentationProcedureType, _Mapping]] = ..., author: _Optional[str] = ..., ingredients: _Optional[_Union[IngredientsType, _Mapping]] = ..., mash: _Optional[_Union[_mash_pb2.MashProcedureType, _Mapping]] = ..., packaging: _Optional[_Union[_packaging_pb2.PackagingProcedureType, _Mapping]] = ..., boil: _Optional[_Union[_boil_pb2.BoilProcedureType, _Mapping]] = ..., taste: _Optional[_Union[TasteType, _Mapping]] = ..., calories_per_pint: _Optional[float] = ..., created: _Optional[str] = ..., batch_size: _Optional[_Union[_measureable_units_pb2.VolumeType, _Mapping]] = ..., notes: _Optional[str] = ..., alcohol_by_volume: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., apparent_attenuation: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ...) -> None: ...

class EfficiencyType(_message.Message):
    __slots__ = ("conversion", "lauter", "mash", "brewhouse")
    CONVERSION_FIELD_NUMBER: _ClassVar[int]
    LAUTER_FIELD_NUMBER: _ClassVar[int]
    MASH_FIELD_NUMBER: _ClassVar[int]
    BREWHOUSE_FIELD_NUMBER: _ClassVar[int]
    conversion: _measureable_units_pb2.PercentType
    lauter: _measureable_units_pb2.PercentType
    mash: _measureable_units_pb2.PercentType
    brewhouse: _measureable_units_pb2.PercentType
    def __init__(self, conversion: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., lauter: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., mash: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ..., brewhouse: _Optional[_Union[_measureable_units_pb2.PercentType, _Mapping]] = ...) -> None: ...

class IngredientsType(_message.Message):
    __slots__ = ("miscellaneous_additions", "culture_additions", "water_additions", "fermentable_additions", "hop_additions")
    MISCELLANEOUS_ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    CULTURE_ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    WATER_ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    FERMENTABLE_ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    HOP_ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    miscellaneous_additions: _containers.RepeatedCompositeFieldContainer[_misc_pb2.MiscellaneousAdditionType]
    culture_additions: _containers.RepeatedCompositeFieldContainer[_culture_pb2.CultureAdditionType]
    water_additions: _containers.RepeatedCompositeFieldContainer[_water_pb2.WaterAdditionType]
    fermentable_additions: _containers.RepeatedCompositeFieldContainer[_fermentable_pb2.FermentableAdditionType]
    hop_additions: _containers.RepeatedCompositeFieldContainer[_hop_pb2.HopAdditionType]
    def __init__(self, miscellaneous_additions: _Optional[_Iterable[_Union[_misc_pb2.MiscellaneousAdditionType, _Mapping]]] = ..., culture_additions: _Optional[_Iterable[_Union[_culture_pb2.CultureAdditionType, _Mapping]]] = ..., water_additions: _Optional[_Iterable[_Union[_water_pb2.WaterAdditionType, _Mapping]]] = ..., fermentable_additions: _Optional[_Iterable[_Union[_fermentable_pb2.FermentableAdditionType, _Mapping]]] = ..., hop_additions: _Optional[_Iterable[_Union[_hop_pb2.HopAdditionType, _Mapping]]] = ...) -> None: ...

class TasteType(_message.Message):
    __slots__ = ("notes", "rating")
    NOTES_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    notes: str
    rating: float
    def __init__(self, notes: _Optional[str] = ..., rating: _Optional[float] = ...) -> None: ...
