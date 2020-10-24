from pete_tpl import dll
from pete_tpl.exception import RenderingException
from pete_tpl.render_result import RenderResult

class Engine:
    def __init__(self):
        self.dll_handle = dll.get_lib().create_new()

    def render(self, template: str) -> str:
        result = RenderResult.from_address(dll.get_lib().render(self.dll_handle, template.encode('utf-8')))
        output = result.output.decode('utf-8')
        if 0 == result.error_code:
            return output
        else:
            raise RenderingException(output, result.error_code)
