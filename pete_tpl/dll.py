import ctypes

from pete_tpl.c_types import CParameter

lib = None


def init():
    global lib
    if not lib is None:
        return
    lib = ctypes.cdll.LoadLibrary('liblibpetetpl.so')
    lib.petetpl_init()

    lib.petetpl_render.restype = ctypes.c_void_p
    lib.petetpl_render.argtypes = [ctypes.c_uint, ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(CParameter)]


def get_lib():
    return lib