from beerproto.v1 import boil_pb2 as _boil_pb2
from beerproto.v1 import culture_pb2 as _culture_pb2
from beerproto.v1 import equipment_pb2 as _equipment_pb2
from beerproto.v1 import fermentable_pb2 as _fermentable_pb2
from beerproto.v1 import fermentation_pb2 as _fermentation_pb2
from beerproto.v1 import hop_pb2 as _hop_pb2
from beerproto.v1 import mash_pb2 as _mash_pb2
from beerproto.v1 import misc_pb2 as _misc_pb2
from beerproto.v1 import packaging_pb2 as _packaging_pb2
from beerproto.v1 import recipe_pb2 as _recipe_pb2
from beerproto.v1 import style_pb2 as _style_pb2
from beerproto.v1 import water_pb2 as _water_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Recipe(_message.Message):
    __slots__ = ("id", "mashes", "recipes", "miscellaneous_ingredients", "styles", "fermentations", "boil", "version", "fermentables", "cultures", "equipments", "packaging", "hop_varieties", "profiles")
    ID_FIELD_NUMBER: _ClassVar[int]
    MASHES_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    MISCELLANEOUS_INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    STYLES_FIELD_NUMBER: _ClassVar[int]
    FERMENTATIONS_FIELD_NUMBER: _ClassVar[int]
    BOIL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FERMENTABLES_FIELD_NUMBER: _ClassVar[int]
    CULTURES_FIELD_NUMBER: _ClassVar[int]
    EQUIPMENTS_FIELD_NUMBER: _ClassVar[int]
    PACKAGING_FIELD_NUMBER: _ClassVar[int]
    HOP_VARIETIES_FIELD_NUMBER: _ClassVar[int]
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    id: str
    mashes: _containers.RepeatedCompositeFieldContainer[_mash_pb2.MashProcedureType]
    recipes: _containers.RepeatedCompositeFieldContainer[_recipe_pb2.RecipeType]
    miscellaneous_ingredients: _containers.RepeatedCompositeFieldContainer[_misc_pb2.MiscellaneousType]
    styles: _containers.RepeatedCompositeFieldContainer[_style_pb2.StyleType]
    fermentations: _containers.RepeatedCompositeFieldContainer[_fermentation_pb2.FermentationProcedureType]
    boil: _containers.RepeatedCompositeFieldContainer[_boil_pb2.BoilProcedureType]
    version: float
    fermentables: _containers.RepeatedCompositeFieldContainer[_fermentable_pb2.FermentableType]
    cultures: _containers.RepeatedCompositeFieldContainer[_culture_pb2.CultureInformation]
    equipments: _containers.RepeatedCompositeFieldContainer[_equipment_pb2.EquipmentType]
    packaging: _containers.RepeatedCompositeFieldContainer[_packaging_pb2.PackagingProcedureType]
    hop_varieties: _containers.RepeatedCompositeFieldContainer[_hop_pb2.VarietyInformation]
    profiles: _containers.RepeatedCompositeFieldContainer[_water_pb2.WaterBase]
    def __init__(self, id: _Optional[str] = ..., mashes: _Optional[_Iterable[_Union[_mash_pb2.MashProcedureType, _Mapping]]] = ..., recipes: _Optional[_Iterable[_Union[_recipe_pb2.RecipeType, _Mapping]]] = ..., miscellaneous_ingredients: _Optional[_Iterable[_Union[_misc_pb2.MiscellaneousType, _Mapping]]] = ..., styles: _Optional[_Iterable[_Union[_style_pb2.StyleType, _Mapping]]] = ..., fermentations: _Optional[_Iterable[_Union[_fermentation_pb2.FermentationProcedureType, _Mapping]]] = ..., boil: _Optional[_Iterable[_Union[_boil_pb2.BoilProcedureType, _Mapping]]] = ..., version: _Optional[float] = ..., fermentables: _Optional[_Iterable[_Union[_fermentable_pb2.FermentableType, _Mapping]]] = ..., cultures: _Optional[_Iterable[_Union[_culture_pb2.CultureInformation, _Mapping]]] = ..., equipments: _Optional[_Iterable[_Union[_equipment_pb2.EquipmentType, _Mapping]]] = ..., packaging: _Optional[_Iterable[_Union[_packaging_pb2.PackagingProcedureType, _Mapping]]] = ..., hop_varieties: _Optional[_Iterable[_Union[_hop_pb2.VarietyInformation, _Mapping]]] = ..., profiles: _Optional[_Iterable[_Union[_water_pb2.WaterBase, _Mapping]]] = ...) -> None: ...
