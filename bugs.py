class HttpException(Exception):
    statuscode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statuscode} and message: {self.message}')

class NotFoundException(HttpException):
    statuscode = 404
    message = 'Resource Not Found'

class serverErrorException(HttpException):
    statuscode = 500
    message = 'Internal Server Error'

def raiseServerError():
    raise NotFoundException()

raiseServerError()
