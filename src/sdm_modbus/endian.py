import enum


class Endian(str, enum.Enum):
    """An enumeration representing the various byte endianness.

    .. attribute:: AUTO

       This indicates that the byte order is chosen by the
       current native environment.

    .. attribute:: BIG

       This indicates that the bytes are in big endian format

    .. attribute:: LITTLE

       This indicates that the bytes are in little endian format

    .. note:: I am simply borrowing the format strings from the
       python struct module for my convenience.
    """

    AUTO = "@"
    BIG = ">"
    LITTLE = "<"

    def __str__(self):
        """Override to force str representation for enum members"""
        return str.__str__(self)