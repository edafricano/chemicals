# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from pandas.core.frame import DataFrame
from typing import (
    List,
    Tuple,
    Union,
)


def Dadgostar_Shaw(T: float, similarity_variable: float) -> float: ...


def Lastovka_Shaw(T: float, similarity_variable: float, cyclic_aliphatic: bool = ...) -> float: ...


def Lastovka_Shaw_T_for_Hm(
    Hm: float,
    MW: float,
    similarity_variable: float,
    T_ref: float = ...,
    factor: float = ...
) -> float: ...


def Lastovka_Shaw_integral(T: float, similarity_variable: float, cyclic_aliphatic: bool = ...) -> float: ...


def Lastovka_Shaw_integral_over_T(T: float, similarity_variable: float, cyclic_aliphatic: bool = ...) -> float: ...


def Lastovka_solid(T: int, similarity_variable: float) -> float: ...


def Lastovka_solid_integral(T: int, similarity_variable: float) -> float: ...


def Lastovka_solid_integral_over_T(T: int, similarity_variable: float) -> float: ...


def Rowlinson_Bondi(T: float, Tc: float, omega: float, Cpgm: float) -> float: ...


def Rowlinson_Poling(T: float, Tc: float, omega: float, Cpgm: float) -> float: ...


def TRCCp(
    T: float,
    a0: float,
    a1: float,
    a2: float,
    a3: float,
    a4: float,
    a5: float,
    a6: float,
    a7: float
) -> float: ...


def TRCCp_integral(
    T: float,
    a0: float,
    a1: float,
    a2: float,
    a3: float,
    a4: float,
    a5: float,
    a6: float,
    a7: float,
    I: float = ...
) -> float: ...


def TRCCp_integral_over_T(
    T: int,
    a0: float,
    a1: int,
    a2: int,
    a3: float,
    a4: float,
    a5: int,
    a6: int,
    a7: int,
    J: int = ...
) -> float: ...


def Zabransky_cubic(T: float, a1: float, a2: float, a3: float, a4: float) -> float: ...


def Zabransky_cubic_integral(T: float, a1: float, a2: float, a3: float, a4: float) -> float: ...


def Zabransky_cubic_integral_over_T(T: float, a1: float, a2: float, a3: float, a4: float) -> float: ...


def Zabransky_quasi_polynomial(
    T: int,
    Tc: float,
    a1: float,
    a2: float,
    a3: float,
    a4: float,
    a5: float,
    a6: float
) -> float: ...


def Zabransky_quasi_polynomial_integral(
    T: int,
    Tc: float,
    a1: float,
    a2: float,
    a3: float,
    a4: float,
    a5: float,
    a6: float
) -> float: ...


def Zabransky_quasi_polynomial_integral_over_T(
    T: int,
    Tc: float,
    a1: float,
    a2: float,
    a3: float,
    a4: float,
    a5: float,
    a6: float
) -> float: ...


def __getattr__(name: str) -> DataFrame: ...


def _load_Cp_data() -> None: ...


class HeatCapacity:
    @classmethod
    def __init_subclass__(cls) -> None: ...


class PiecewiseHeatCapacity:
    @property
    def Tmin(self) -> float: ...
    def __init__(self, models: List[ZabranskySpline]) -> None: ...
    def calculate(self, T: int) -> float: ...
    def force_calculate(self, T: int) -> float: ...
    def force_calculate_integral(self, Ta: float, Tb: float) -> float: ...
    def force_calculate_integral_over_T(self, Ta: float, Tb: float) -> float: ...


class ZabranskyQuasipolynomial:
    def __init__(
        self,
        coeffs: Tuple[float, float, float, float, float, float],
        Tc: float,
        Tmin: float,
        Tmax: float
    ) -> None: ...


class ZabranskySpline:
    def __init__(self, coeffs: Tuple[float, float, float, float], Tmin: float, Tmax: float) -> None: ...
    def calculate(self, T: int) -> float: ...
    def calculate_integral(self, Ta: float, Tb: float) -> float: ...
    def calculate_integral_over_T(self, Ta: float, Tb: float) -> float: ...

__all__: List[str]