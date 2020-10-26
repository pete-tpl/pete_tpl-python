import ctypes
from typing import Any, List, Mapping

from pete_tpl.parameter import Parameter

PARAM_TYPE_INT = 1
PARAM_TYPE_FLOAT = 2
PARAM_TYPE_STRING = 5


class CParameter(ctypes.Structure):
    _fields_ = [
        ("name", ctypes.c_char_p),
        ("param_type", ctypes.c_uint16),
        ("value_float", ctypes.c_double),
        ("value_int", ctypes.c_int64),
        ("value_string", ctypes.c_char_p),
    ]

    def from_python_map(parameters: Mapping[str, Parameter]) -> List['CParameter']:
        result = []
        for k, v in parameters.items():
            result.append(CParameter.from_python_parameter(k, v))

        res_type = CParameter * len(result)
        res_2 = res_type(*result)

        return res_2

    def from_python_parameter(name: str, value: Any) -> 'CParameter':
        result = CParameter()
        result.name = ctypes.c_char_p(name.encode('utf-8')) 
        if isinstance(value, int):
            result.value_int = value
            result.param_type = PARAM_TYPE_INT
        elif isinstance(value, float):
            result.value_float = value
            result.param_type = PARAM_TYPE_FLOAT
        elif isinstance(value, str):
            result.value_string = ctypes.c_char_p(value.encode('utf-8'))
            result.param_type = PARAM_TYPE_STRING
        else:
            raise Exception(f'Unsupported parameter type: {type(value)}')
        return result


class CRenderResult(ctypes.Structure):
    _fields_ = [
        ("output", ctypes.c_char_p),
        ("error_code", ctypes.c_int),
    ]
