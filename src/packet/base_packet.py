from abc import ABCMeta, abstractmethod


class BasePacket(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __getstate__(self):
        pass

    @abstractmethod
    def __setstate__(self, state):
        pass
