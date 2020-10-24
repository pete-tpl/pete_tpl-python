import ctypes

class RenderResult(ctypes.Structure):
    _fields_ = [
        ("output", ctypes.c_char_p),
        ("error_code", ctypes.c_int),
    ]