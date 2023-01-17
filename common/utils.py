from enum import Enum


class NoErrorMessage(Exception):
    pass


class ButtonUnClickAble(Exception):
    pass


class UserType(Enum):
    SELLER = "seller"
    BUYER = "buyer"


def get_dynamic_enum(class_funcs: type):
    funcs = [method for method in dir(class_funcs) if method.startswith('__') is False]
    dict_funcs = {func_name.upper(): func_name for func_name in funcs}
    return type('Enum', (), dict_funcs)

