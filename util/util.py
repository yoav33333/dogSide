import types

def is_not_function(item):
    return not isinstance(item, (types.FunctionType, types.MethodType, staticmethod, classmethod))

