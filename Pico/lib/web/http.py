"""
Module http - HTTP Protocol
"""
from collections import namedtuple

Header = namedtuple("Header", "html svg png css txt NotFound")

class Http():
    """
    Class Http - Class for Http Protocol Elements
    """
    responseHeader = Header(
        'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n',
        'HTTP/1.0 200 OK\r\nContent-type: image/svg+xml\r\n\r\n',
        'HTTP/1.0 200 OK\r\nContent-type: image/png\r\n\r\n',
        'HTTP/1.0 200 OK\r\nContent-type: text/css\r\n\r\n',
        'HTTP/1.0 200 OK\r\nContent-type: text/plain\r\n\r\n',
        'HTTP/1.0 404 NotFound\r\nContent-type: text/html\r\n\r\n')

    @staticmethod
    def response_header(key):
        """
        response_header(key) - Get Http Response Header

        i.e. response_header("html") gets "HTTP/1.0 200 OK Content-type: text/html"
        """
        return getattr(Http.responseHeader, key).encode()

#-------------------------------------------------------------------
