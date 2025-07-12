import json

from util.singelton import SingletonMeta
from util.util import is_not_function


class jsonGen():
    # def gen_map(self, vars):
    #     for var in vars:
    #         if hasattr(var, '__dict__'):
    #             self.map[var.__class__.__name__] = {k: v for k, v in var.__dict__.items() if not k.startswith('_')}
    #         else:
    #             self.map[var.__class__.__name__] = var

    def mapGen(self):
        map = {}
        for cls in _registered_classes:
            # print(cls.__name__)

            if hasattr(cls, '__dict__'):
                # print(cls.__name__)
                # map[cls.__name__] = cls
                map[cls.__name__] = {k: v for k, v in cls.__dict__.items()
                                     if not k.startswith('_') and is_not_function(v)}
            else:
                map[type(cls).__name__] = cls
        # print(map)
        # map = {k: v for k, v in map.items() if not k.startswith('_')}
        return map

    def getJson(self):

        try:
            return json.dumps(self.mapGen())
        except:
            return "{}"
_registered_classes = []

def register_class(cls):
    _registered_classes.append(cls)
    cls._registered_classes = _registered_classes
    return cls