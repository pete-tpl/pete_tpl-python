class NotInitializedException(Exception):
    def __init__(self, msg='PETE is not initialized', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class RenderingException(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code
