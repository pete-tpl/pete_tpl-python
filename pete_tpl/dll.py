import ctypes
import os
import platform

import pete_tpl
from pete_tpl.c_types import CParameter

FILE_EXTENSIONS = {
    'linux': 'so'
}


def format_shared_lib_path() -> str:
    extension = FILE_EXTENSIONS.get(OS_NAME)
    if extension is None:
        raise Exception(f'Cannot determine a file extension for OS: {OS_NAME}')
    module_dir = os.path.dirname(pete_tpl.__file__)
    return f'{module_dir}/libpetetpl.{extension}'


OS_NAME = platform.system().lower()
PETETPL_SHARED_LIB_PATH = format_shared_lib_path()

lib = None


def init():
    global lib
    if lib is not None:
        return
    lib = ctypes.cdll.LoadLibrary(PETETPL_SHARED_LIB_PATH)
    lib.petetpl_init()

    lib.petetpl_render.restype = ctypes.c_void_p
    lib.petetpl_render.argtypes = [ctypes.c_uint, ctypes.c_char_p,
                                   ctypes.c_int,
                                   ctypes.POINTER(CParameter)]


def get_lib() -> ctypes.CDLL:
    return lib
