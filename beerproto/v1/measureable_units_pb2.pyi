from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VolumeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VOLUME_UNIT_UNSPECIFIED: _ClassVar[VolumeUnit]
    VOLUME_UNIT_ML: _ClassVar[VolumeUnit]
    VOLUME_UNIT_L: _ClassVar[VolumeUnit]
    VOLUME_UNIT_TSP: _ClassVar[VolumeUnit]
    VOLUME_UNIT_TBSP: _ClassVar[VolumeUnit]
    VOLUME_UNIT_FLOZ: _ClassVar[VolumeUnit]
    VOLUME_UNIT_CUP: _ClassVar[VolumeUnit]
    VOLUME_UNIT_PT: _ClassVar[VolumeUnit]
    VOLUME_UNIT_QT: _ClassVar[VolumeUnit]
    VOLUME_UNIT_GAL: _ClassVar[VolumeUnit]
    VOLUME_UNIT_BBL: _ClassVar[VolumeUnit]
    VOLUME_UNIT_IFLOZ: _ClassVar[VolumeUnit]
    VOLUME_UNIT_IPT: _ClassVar[VolumeUnit]
    VOLUME_UNIT_IQT: _ClassVar[VolumeUnit]
    VOLUME_UNIT_IGAL: _ClassVar[VolumeUnit]
    VOLUME_UNIT_IBBL: _ClassVar[VolumeUnit]

class MassUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MASS_UNIT_UNSPECIFIED: _ClassVar[MassUnit]
    MASS_UNIT_MG: _ClassVar[MassUnit]
    MASS_UNIT_G: _ClassVar[MassUnit]
    MASS_UNIT_KG: _ClassVar[MassUnit]
    MASS_UNIT_LB: _ClassVar[MassUnit]
    MASS_UNIT_OZ: _ClassVar[MassUnit]

class CellCountUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CELL_COUNT_UNIT_UNSPECIFIED: _ClassVar[CellCountUnit]
    CELL_COUNT_UNIT_CELLS: _ClassVar[CellCountUnit]
    CELL_COUNT_UNIT_MILLION: _ClassVar[CellCountUnit]
    CELL_COUNT_UNIT_BILLION: _ClassVar[CellCountUnit]

class PitchRateUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PITCH_RATE_UNIT_UNSPECIFIED: _ClassVar[PitchRateUnit]
    PITCH_RATE_UNIT_MILLION_CELLS_PER_ML_PER_PLATO: _ClassVar[PitchRateUnit]

class DiastaticPowerUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIASTATIC_POWER_UNIT_UNSPECIFIED: _ClassVar[DiastaticPowerUnit]
    DIASTATIC_POWER_UNIT_LINTNER: _ClassVar[DiastaticPowerUnit]
    DIASTATIC_POWER_UNIT_WK: _ClassVar[DiastaticPowerUnit]

class TemperatureUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPERATURE_UNIT_UNSPECIFIED: _ClassVar[TemperatureUnit]
    TEMPERATURE_UNIT_C: _ClassVar[TemperatureUnit]
    TEMPERATURE_UNIT_F: _ClassVar[TemperatureUnit]

class AcidityUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACIDITY_UNIT_UNSPECIFIED: _ClassVar[AcidityUnit]
    ACIDITY_UNIT_PH: _ClassVar[AcidityUnit]

class TimeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIME_UNIT_UNSPECIFIED: _ClassVar[TimeUnit]
    TIME_UNIT_SEC: _ClassVar[TimeUnit]
    TIME_UNIT_MIN: _ClassVar[TimeUnit]
    TIME_UNIT_HR: _ClassVar[TimeUnit]
    TIME_UNIT_DAY: _ClassVar[TimeUnit]
    TIME_UNIT_WEEK: _ClassVar[TimeUnit]

class ColorUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLOR_UNIT_UNSPECIFIED: _ClassVar[ColorUnit]
    COLOR_UNIT_EBC: _ClassVar[ColorUnit]
    COLOR_UNIT_LOVI: _ClassVar[ColorUnit]
    COLOR_UNIT_SRM: _ClassVar[ColorUnit]

class CarbonationUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CARBONATION_UNIT_UNSPECIFIED: _ClassVar[CarbonationUnit]
    CARBONATION_UNIT_VOLS: _ClassVar[CarbonationUnit]
    CARBONATION_UNIT_GL: _ClassVar[CarbonationUnit]

class BitternessUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BITTERNESS_UNIT_UNSPECIFIED: _ClassVar[BitternessUnit]
    BITTERNESS_UNIT_IBUS: _ClassVar[BitternessUnit]

class GravityUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRAVITY_UNIT_UNSPECIFIED: _ClassVar[GravityUnit]
    GRAVITY_UNIT_SG: _ClassVar[GravityUnit]
    GRAVITY_UNIT_PLATO: _ClassVar[GravityUnit]
    GRAVITY_UNIT_BRIX: _ClassVar[GravityUnit]

class SpecificHeatUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPECIFIC_HEAT_UNIT_UNSPECIFIED: _ClassVar[SpecificHeatUnit]
    SPECIFIC_HEAT_UNIT_CALGC: _ClassVar[SpecificHeatUnit]
    SPECIFIC_HEAT_UNIT_JKGK: _ClassVar[SpecificHeatUnit]
    SPECIFIC_HEAT_UNIT_BTULBF: _ClassVar[SpecificHeatUnit]

class ConcentrationUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONCENTRATION_UNIT_UNSPECIFIED: _ClassVar[ConcentrationUnit]
    CONCENTRATION_UNIT_PPM: _ClassVar[ConcentrationUnit]
    CONCENTRATION_UNIT_PPB: _ClassVar[ConcentrationUnit]
    CONCENTRATION_UNIT_MGL: _ClassVar[ConcentrationUnit]
    CONCENTRATION_UNIT_MG100L: _ClassVar[ConcentrationUnit]

class SpecificVolumeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPECIFIC_VOLUME_UNIT_UNSPECIFIED: _ClassVar[SpecificVolumeUnit]
    SPECIFIC_VOLUME_UNIT_QTLB: _ClassVar[SpecificVolumeUnit]
    SPECIFIC_VOLUME_UNIT_GALLB: _ClassVar[SpecificVolumeUnit]
    SPECIFIC_VOLUME_UNIT_GALOZ: _ClassVar[SpecificVolumeUnit]
    SPECIFIC_VOLUME_UNIT_LG: _ClassVar[SpecificVolumeUnit]
    SPECIFIC_VOLUME_UNIT_LKG: _ClassVar[SpecificVolumeUnit]
    SPECIFIC_VOLUME_UNIT_FLOZOZ: _ClassVar[SpecificVolumeUnit]
    SPECIFIC_VOLUME_UNIT_M3KG: _ClassVar[SpecificVolumeUnit]
    SPECIFIC_VOLUME_UNIT_FT3LB: _ClassVar[SpecificVolumeUnit]

class UnitUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNIT_UNIT_UNSPECIFIED: _ClassVar[UnitUnit]
    UNIT_UNIT_ONE: _ClassVar[UnitUnit]
    UNIT_UNIT_UNIT: _ClassVar[UnitUnit]
    UNIT_UNIT_EACH: _ClassVar[UnitUnit]
    UNIT_UNIT_DIMENSIONLESS: _ClassVar[UnitUnit]
    UNIT_UNIT_PKG: _ClassVar[UnitUnit]

class PercentUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERCENT_UNIT_UNSPECIFIED: _ClassVar[PercentUnit]
    PERCENT_UNIT_PERCENT_SIGN: _ClassVar[PercentUnit]

class ViscosityUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VISCOSITY_UNIT_UNSPECIFIED: _ClassVar[ViscosityUnit]
    VISCOSITY_UNIT_CP: _ClassVar[ViscosityUnit]
    VISCOSITY_UNIT_MPAS: _ClassVar[ViscosityUnit]
    VISCOSITY_UNIT_POISE: _ClassVar[ViscosityUnit]

class RateUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RATE_UNIT_UNSPECIFIED: _ClassVar[RateUnit]
    RATE_UNIT_L_PER_HOUR: _ClassVar[RateUnit]
    RATE_UNIT_L_PER_MINUTE: _ClassVar[RateUnit]
    RATE_UNIT_GAL_PER_HOUR: _ClassVar[RateUnit]
    RATE_UNIT_GAL_PER_MINUTE: _ClassVar[RateUnit]
    RATE_UNIT_HL_PER_HOUR: _ClassVar[RateUnit]
    RATE_UNIT_BBL_PER_HOUR: _ClassVar[RateUnit]
    RATE_UNIT_UK_BBL_PER_HOUR: _ClassVar[RateUnit]
    RATE_UNIT_PERCENT_PER_HOUR: _ClassVar[RateUnit]
    RATE_UNIT_L_PER_KG: _ClassVar[RateUnit]
    RATE_UNIT_GAL_PER_LB: _ClassVar[RateUnit]
    RATE_UNIT_C_PER_MINUTE: _ClassVar[RateUnit]
    RATE_UNIT_F_PER_MINUTE: _ClassVar[RateUnit]

class PressureUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRESSURE_UNIT_UNSPECIFIED: _ClassVar[PressureUnit]
    PRESSURE_UNIT_PASCAL: _ClassVar[PressureUnit]
    PRESSURE_UNIT_BAR: _ClassVar[PressureUnit]
    PRESSURE_UNIT_PSI: _ClassVar[PressureUnit]
    PRESSURE_UNIT_KPA: _ClassVar[PressureUnit]

class EnzymeActivityUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENZYME_ACTIVITY_UNIT_UNSPECIFIED: _ClassVar[EnzymeActivityUnit]
    ENZYME_ACTIVITY_UNIT_DU: _ClassVar[EnzymeActivityUnit]
    ENZYME_ACTIVITY_UNIT_WK: _ClassVar[EnzymeActivityUnit]
    ENZYME_ACTIVITY_UNIT_SKB: _ClassVar[EnzymeActivityUnit]

class EnzymeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENZYME_TYPE_UNSPECIFIED: _ClassVar[EnzymeType]
    ENZYME_TYPE_ALPHA_AMYLASE: _ClassVar[EnzymeType]
    ENZYME_TYPE_BETA_AMYLASE: _ClassVar[EnzymeType]
    ENZYME_TYPE_PROTEASE: _ClassVar[EnzymeType]
VOLUME_UNIT_UNSPECIFIED: VolumeUnit
VOLUME_UNIT_ML: VolumeUnit
VOLUME_UNIT_L: VolumeUnit
VOLUME_UNIT_TSP: VolumeUnit
VOLUME_UNIT_TBSP: VolumeUnit
VOLUME_UNIT_FLOZ: VolumeUnit
VOLUME_UNIT_CUP: VolumeUnit
VOLUME_UNIT_PT: VolumeUnit
VOLUME_UNIT_QT: VolumeUnit
VOLUME_UNIT_GAL: VolumeUnit
VOLUME_UNIT_BBL: VolumeUnit
VOLUME_UNIT_IFLOZ: VolumeUnit
VOLUME_UNIT_IPT: VolumeUnit
VOLUME_UNIT_IQT: VolumeUnit
VOLUME_UNIT_IGAL: VolumeUnit
VOLUME_UNIT_IBBL: VolumeUnit
MASS_UNIT_UNSPECIFIED: MassUnit
MASS_UNIT_MG: MassUnit
MASS_UNIT_G: MassUnit
MASS_UNIT_KG: MassUnit
MASS_UNIT_LB: MassUnit
MASS_UNIT_OZ: MassUnit
CELL_COUNT_UNIT_UNSPECIFIED: CellCountUnit
CELL_COUNT_UNIT_CELLS: CellCountUnit
CELL_COUNT_UNIT_MILLION: CellCountUnit
CELL_COUNT_UNIT_BILLION: CellCountUnit
PITCH_RATE_UNIT_UNSPECIFIED: PitchRateUnit
PITCH_RATE_UNIT_MILLION_CELLS_PER_ML_PER_PLATO: PitchRateUnit
DIASTATIC_POWER_UNIT_UNSPECIFIED: DiastaticPowerUnit
DIASTATIC_POWER_UNIT_LINTNER: DiastaticPowerUnit
DIASTATIC_POWER_UNIT_WK: DiastaticPowerUnit
TEMPERATURE_UNIT_UNSPECIFIED: TemperatureUnit
TEMPERATURE_UNIT_C: TemperatureUnit
TEMPERATURE_UNIT_F: TemperatureUnit
ACIDITY_UNIT_UNSPECIFIED: AcidityUnit
ACIDITY_UNIT_PH: AcidityUnit
TIME_UNIT_UNSPECIFIED: TimeUnit
TIME_UNIT_SEC: TimeUnit
TIME_UNIT_MIN: TimeUnit
TIME_UNIT_HR: TimeUnit
TIME_UNIT_DAY: TimeUnit
TIME_UNIT_WEEK: TimeUnit
COLOR_UNIT_UNSPECIFIED: ColorUnit
COLOR_UNIT_EBC: ColorUnit
COLOR_UNIT_LOVI: ColorUnit
COLOR_UNIT_SRM: ColorUnit
CARBONATION_UNIT_UNSPECIFIED: CarbonationUnit
CARBONATION_UNIT_VOLS: CarbonationUnit
CARBONATION_UNIT_GL: CarbonationUnit
BITTERNESS_UNIT_UNSPECIFIED: BitternessUnit
BITTERNESS_UNIT_IBUS: BitternessUnit
GRAVITY_UNIT_UNSPECIFIED: GravityUnit
GRAVITY_UNIT_SG: GravityUnit
GRAVITY_UNIT_PLATO: GravityUnit
GRAVITY_UNIT_BRIX: GravityUnit
SPECIFIC_HEAT_UNIT_UNSPECIFIED: SpecificHeatUnit
SPECIFIC_HEAT_UNIT_CALGC: SpecificHeatUnit
SPECIFIC_HEAT_UNIT_JKGK: SpecificHeatUnit
SPECIFIC_HEAT_UNIT_BTULBF: SpecificHeatUnit
CONCENTRATION_UNIT_UNSPECIFIED: ConcentrationUnit
CONCENTRATION_UNIT_PPM: ConcentrationUnit
CONCENTRATION_UNIT_PPB: ConcentrationUnit
CONCENTRATION_UNIT_MGL: ConcentrationUnit
CONCENTRATION_UNIT_MG100L: ConcentrationUnit
SPECIFIC_VOLUME_UNIT_UNSPECIFIED: SpecificVolumeUnit
SPECIFIC_VOLUME_UNIT_QTLB: SpecificVolumeUnit
SPECIFIC_VOLUME_UNIT_GALLB: SpecificVolumeUnit
SPECIFIC_VOLUME_UNIT_GALOZ: SpecificVolumeUnit
SPECIFIC_VOLUME_UNIT_LG: SpecificVolumeUnit
SPECIFIC_VOLUME_UNIT_LKG: SpecificVolumeUnit
SPECIFIC_VOLUME_UNIT_FLOZOZ: SpecificVolumeUnit
SPECIFIC_VOLUME_UNIT_M3KG: SpecificVolumeUnit
SPECIFIC_VOLUME_UNIT_FT3LB: SpecificVolumeUnit
UNIT_UNIT_UNSPECIFIED: UnitUnit
UNIT_UNIT_ONE: UnitUnit
UNIT_UNIT_UNIT: UnitUnit
UNIT_UNIT_EACH: UnitUnit
UNIT_UNIT_DIMENSIONLESS: UnitUnit
UNIT_UNIT_PKG: UnitUnit
PERCENT_UNIT_UNSPECIFIED: PercentUnit
PERCENT_UNIT_PERCENT_SIGN: PercentUnit
VISCOSITY_UNIT_UNSPECIFIED: ViscosityUnit
VISCOSITY_UNIT_CP: ViscosityUnit
VISCOSITY_UNIT_MPAS: ViscosityUnit
VISCOSITY_UNIT_POISE: ViscosityUnit
RATE_UNIT_UNSPECIFIED: RateUnit
RATE_UNIT_L_PER_HOUR: RateUnit
RATE_UNIT_L_PER_MINUTE: RateUnit
RATE_UNIT_GAL_PER_HOUR: RateUnit
RATE_UNIT_GAL_PER_MINUTE: RateUnit
RATE_UNIT_HL_PER_HOUR: RateUnit
RATE_UNIT_BBL_PER_HOUR: RateUnit
RATE_UNIT_UK_BBL_PER_HOUR: RateUnit
RATE_UNIT_PERCENT_PER_HOUR: RateUnit
RATE_UNIT_L_PER_KG: RateUnit
RATE_UNIT_GAL_PER_LB: RateUnit
RATE_UNIT_C_PER_MINUTE: RateUnit
RATE_UNIT_F_PER_MINUTE: RateUnit
PRESSURE_UNIT_UNSPECIFIED: PressureUnit
PRESSURE_UNIT_PASCAL: PressureUnit
PRESSURE_UNIT_BAR: PressureUnit
PRESSURE_UNIT_PSI: PressureUnit
PRESSURE_UNIT_KPA: PressureUnit
ENZYME_ACTIVITY_UNIT_UNSPECIFIED: EnzymeActivityUnit
ENZYME_ACTIVITY_UNIT_DU: EnzymeActivityUnit
ENZYME_ACTIVITY_UNIT_WK: EnzymeActivityUnit
ENZYME_ACTIVITY_UNIT_SKB: EnzymeActivityUnit
ENZYME_TYPE_UNSPECIFIED: EnzymeType
ENZYME_TYPE_ALPHA_AMYLASE: EnzymeType
ENZYME_TYPE_BETA_AMYLASE: EnzymeType
ENZYME_TYPE_PROTEASE: EnzymeType

class VolumeType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: VolumeUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[VolumeUnit, str]] = ...) -> None: ...

class MassType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: MassUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[MassUnit, str]] = ...) -> None: ...

class CellCountType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: CellCountUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[CellCountUnit, str]] = ...) -> None: ...

class PitchRateType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: PitchRateUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[PitchRateUnit, str]] = ...) -> None: ...

class DiastaticPowerType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: DiastaticPowerUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[DiastaticPowerUnit, str]] = ...) -> None: ...

class TemperatureType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: TemperatureUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[TemperatureUnit, str]] = ...) -> None: ...

class AcidityType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: AcidityUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[AcidityUnit, str]] = ...) -> None: ...

class TimeType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: int
    unit: TimeUnit
    def __init__(self, value: _Optional[int] = ..., unit: _Optional[_Union[TimeUnit, str]] = ...) -> None: ...

class ColorType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: ColorUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[ColorUnit, str]] = ...) -> None: ...

class CarbonationType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: CarbonationUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[CarbonationUnit, str]] = ...) -> None: ...

class BitternessType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: BitternessUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[BitternessUnit, str]] = ...) -> None: ...

class GravityType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: GravityUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[GravityUnit, str]] = ...) -> None: ...

class SpecificHeatType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: SpecificHeatUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[SpecificHeatUnit, str]] = ...) -> None: ...

class ConcentrationType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: ConcentrationUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[ConcentrationUnit, str]] = ...) -> None: ...

class SpecificVolumeType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: SpecificVolumeUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[SpecificVolumeUnit, str]] = ...) -> None: ...

class UnitType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: UnitUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[UnitUnit, str]] = ...) -> None: ...

class PercentType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: PercentUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[PercentUnit, str]] = ...) -> None: ...

class ViscosityType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: ViscosityUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[ViscosityUnit, str]] = ...) -> None: ...

class CarbonationRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: CarbonationType
    maximum: CarbonationType
    def __init__(self, minimum: _Optional[_Union[CarbonationType, _Mapping]] = ..., maximum: _Optional[_Union[CarbonationType, _Mapping]] = ...) -> None: ...

class BitternessRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: BitternessType
    maximum: BitternessType
    def __init__(self, minimum: _Optional[_Union[BitternessType, _Mapping]] = ..., maximum: _Optional[_Union[BitternessType, _Mapping]] = ...) -> None: ...

class TemperatureRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: TemperatureType
    maximum: TemperatureType
    def __init__(self, minimum: _Optional[_Union[TemperatureType, _Mapping]] = ..., maximum: _Optional[_Union[TemperatureType, _Mapping]] = ...) -> None: ...

class ColorRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: ColorType
    maximum: ColorType
    def __init__(self, minimum: _Optional[_Union[ColorType, _Mapping]] = ..., maximum: _Optional[_Union[ColorType, _Mapping]] = ...) -> None: ...

class GravityRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: GravityType
    maximum: GravityType
    def __init__(self, minimum: _Optional[_Union[GravityType, _Mapping]] = ..., maximum: _Optional[_Union[GravityType, _Mapping]] = ...) -> None: ...

class PercentRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: PercentType
    maximum: PercentType
    def __init__(self, minimum: _Optional[_Union[PercentType, _Mapping]] = ..., maximum: _Optional[_Union[PercentType, _Mapping]] = ...) -> None: ...

class TimeRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: TimeType
    maximum: TimeType
    def __init__(self, minimum: _Optional[_Union[TimeType, _Mapping]] = ..., maximum: _Optional[_Union[TimeType, _Mapping]] = ...) -> None: ...

class ViscosityRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: ViscosityType
    maximum: ViscosityType
    def __init__(self, minimum: _Optional[_Union[ViscosityType, _Mapping]] = ..., maximum: _Optional[_Union[ViscosityType, _Mapping]] = ...) -> None: ...

class DiastaticPowerRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: DiastaticPowerType
    maximum: DiastaticPowerType
    def __init__(self, minimum: _Optional[_Union[DiastaticPowerType, _Mapping]] = ..., maximum: _Optional[_Union[DiastaticPowerType, _Mapping]] = ...) -> None: ...

class SpecificVolumeRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: SpecificVolumeType
    maximum: SpecificVolumeType
    def __init__(self, minimum: _Optional[_Union[SpecificVolumeType, _Mapping]] = ..., maximum: _Optional[_Union[SpecificVolumeType, _Mapping]] = ...) -> None: ...

class AcidityRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: AcidityType
    maximum: AcidityType
    def __init__(self, minimum: _Optional[_Union[AcidityType, _Mapping]] = ..., maximum: _Optional[_Union[AcidityType, _Mapping]] = ...) -> None: ...

class ConcentrationRangeType(_message.Message):
    __slots__ = ("minimum", "maximum")
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: ConcentrationType
    maximum: ConcentrationType
    def __init__(self, minimum: _Optional[_Union[ConcentrationType, _Mapping]] = ..., maximum: _Optional[_Union[ConcentrationType, _Mapping]] = ...) -> None: ...

class RateType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: RateUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[RateUnit, str]] = ...) -> None: ...

class PressureType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: PressureUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[PressureUnit, str]] = ...) -> None: ...

class EnzymeActivityType(_message.Message):
    __slots__ = ("value", "unit")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: EnzymeActivityUnit
    def __init__(self, value: _Optional[float] = ..., unit: _Optional[_Union[EnzymeActivityUnit, str]] = ...) -> None: ...

class EnzymeActivity(_message.Message):
    __slots__ = ("kind", "activity")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    kind: EnzymeType
    activity: EnzymeActivityType
    def __init__(self, kind: _Optional[_Union[EnzymeType, str]] = ..., activity: _Optional[_Union[EnzymeActivityType, _Mapping]] = ...) -> None: ...
