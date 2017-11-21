#class from Ira Woodring

from abc import ABCMeta, abstractmethod

"""class to update those who observe others"""
class Observer(object):
        __metaclass__ = ABCMeta

        @abstractmethod
        def update(self):
                pass
