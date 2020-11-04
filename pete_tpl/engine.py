from typing import Any, Mapping

from pete_tpl import dll
from pete_tpl.c_types import CParameter, CRenderResult
from pete_tpl.exception import NotInitializedException, RenderingException


class Engine:
    def __init__(self):
        dll.init()
        lib = dll.get_lib()
        if lib is None:
            raise NotInitializedException()
        self.dll_handle = lib.petetpl_create_new()

    def render(self, template: str, parameters: Mapping[str, Any] = {}) -> str:
        cparameters = CParameter.from_python_map(parameters)
        cparameters_arg = cparameters
        result = CRenderResult \
            .from_address(dll
                          .get_lib()
                          .petetpl_render(
                            self.dll_handle,
                            template.encode('utf-8'),
                            len(cparameters),
                            cparameters_arg))
        output = result.output.decode('utf-8')
        exception = None if 0 == result.error_code \
            else RenderingException(output, result.error_code)
        dll.get_lib().petetpl_free_render_result(result)
        if exception is not None:
            raise exception
        return output
