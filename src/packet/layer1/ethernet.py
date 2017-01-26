from packet.base_packet import BasePacket


class Ethernet(BasePacket):
    def __init__(self, source, destination, type_):
        self.__src = source
        self.__dst = destination
        self.__type = type_

    @property
    def source(self):
        return self.__src

    @property
    def destination(self):
        return self.__dst

    @property
    def type(self):
        return self.__type

    @source.setter
    def source(self, value):
        if not is_valid_mac_address(value):
            raise InvalidMacAddress()
        self.__src = value

    @destination.setter
    def destination(self, value):
        if not is_valid_mac_address(value):
            raise InvalidMacAddress()
        self.__dst = value
