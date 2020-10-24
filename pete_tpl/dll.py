import ctypes

lib = None

def init():
    global lib
    lib = ctypes.cdll.LoadLibrary('liblibpetetpl.so')
    lib.init()

    lib.render.restype = ctypes.c_void_p
    lib.render.argtypes = [ctypes.c_uint, ctypes.c_char_p]


def get_lib():
    return lib