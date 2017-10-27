class Error(Exception):
    '''Base class for exceptions in this module'''
    pass


class LenghtError(Error):
    '''Exceptions raised for error in lenght of string'''
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)