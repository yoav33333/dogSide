import json
import time

from util.singelton import SingletonMeta
from util.util import is_not_function


class jsonGen(metaclass=SingletonMeta):
    # def gen_map(self, vars):
    #     for var in vars:
    #         if hasattr(var, '__dict__'):
    #             self.map[var.__class__.__name__] = {k: v for k, v in var.__dict__.items() if not k.startswith('_')}
    #         else:
    #             self.map[var.__class__.__name__] = var
    def __init__(self, classes=None):
        if classes is None:
            return
        for cls in classes:
            register_class(cls)
        # _registered_classes.append(classes)
        # self.map = self.mapGen()

    def mapGen(self):
        result = {}
        for class_name, cls in _registered_classes.items():
            instance = cls()
            result[class_name] = {}
            # print(ins)
            for key, value in cls.__dict__.items():
                if (not key.startswith('_') and is_not_function(value)
                        and not callable(value) and key != "instance"):
                    result[class_name][key] = getattr(instance, key, None)

            # result[class_name] = {
            #     "name": getattr(instance, "name", None),
            #     "age": getattr(instance, "age", None)
            # }
        # map = {}
        # for cls in _registered_classes:
        #
        #     # cls = cls if isinstance(cls, type) else type(cls)
        #     print(type(cls).__name__)
        #     print(type(cls))
        #     print(cls)
        #     map[type(cls).__name__] = {k: v for k, v in cls.__dict__.items()
        #                          if not k.startswith('_') and is_not_function(v)}
        return result
    def updateClasses(self, json_data):
        try:
            data = json.loads(json_data)
            for cls_name, cls_data in data.items():
                for cls in _registered_classes:
                    if cls.__name__ == cls_name:
                        for key, value in cls_data.items():
                            setattr(cls, key, value)
                            print(key, value)
        except json.JSONDecodeError:
            print("Invalid JSON data provided for class update.")
    def getJson(self):

        try:
            return json.dumps(self.mapGen())
        except:
            return "{}"
_registered_classes = {}

def register_class(cls):
    _registered_classes[cls.__name__] = cls
    return cls