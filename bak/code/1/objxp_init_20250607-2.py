import os
import json
import shutil
from typing import Literal, Optional, Union


def get_terminal_size_shutil():
    return shutil.get_terminal_size((80, 20))  # Default width and height

terminal_size = get_terminal_size_shutil()

initial_classes = {
    'func': [
        "function",
        "method",
        "builtin_function_or_method",
        "method_descriptor",
        "wrapper_descriptor",  # 特殊方法的包装器
        "slot_wrapper"  # 内置方法包装器
    ],
    
    'data': [
        "int",
        "float",
        "bool",
        "str",
        "list",
        "dict",
        "set",
        "tuple",
        "bytes",
        "bytearray",
        "complex",
        "range",
        "memoryview"
    ],
    
    'class': [
        "type",
        "class"
    ],
    
    'module': [
        "module",
        "modulespec",
        "moduledef"
    ],
    
    'descriptor': [
        "property",
        "getset_descriptor",
        "member_descriptor",
        "classmethod",
        "staticmethod"
    ],
    
    'special': [
        "method-wrapper",
        "slot_descriptor",
        "wrapper_descriptor",
        "mappingproxy"  # 类字典的只读视图
    ],
    
    'loader': [
        "sourcefileloader",
        "sourcelessfileloader",
        "frozen_importlib",
        "builtinimporter"
    ],
    
    'iterator': [
        "iterator",
        "generator",
        "coroutine",
        "async_generator"
    ],
    
    'other': [
        "nonetype",
        "object",
        "ellipsis",
        "notimplemented"
    ]
}

# 特殊方法分类
special_methods = {
    'creation': ['__new__', '__init__', '__del__'],
    'representation': ['__str__', '__repr__', '__format__'],
    'comparison': ['__eq__', '__ne__', '__lt__', '__le__', '__gt__', '__ge__', '__hash__'],
    'container': ['__len__', '__getitem__', '__setitem__', '__delitem__', '__iter__', '__next__', '__contains__'],
    'numeric': ['__add__', '__sub__', '__mul__', '__truediv__', '__floordiv__', '__mod__', '__pow__'],
    'attribute': ['__getattr__', '__setattr__', '__delattr__', '__getattribute__', '__dir__'],
    'callable': ['__call__'],
    'context': ['__enter__', '__exit__'],
    'other_special': []
}

    
resjson = {
    "objname":"",
    "objitms":[]
}


def safe_type(obj, attr=None):
    """安全地获取对象或属性的类型字符串
    
    Args:
        obj: 要获取类型的对象
        attr: 如果提供，则获取obj的attr属性的类型
        
    Returns:
        str: 类型的字符串表示，格式为"<class 'type_name'>"
    """
    try:
        if attr is not None:
            return str(type(getattr(obj, attr)))
        else:
            return str(type(obj))
    except Exception:
        return "unavailable"

def get_type_name(type_str):
    """从类型字符串中提取类型名称
    
    Args:
        type_str: 类型的字符串表示，格式为"<class 'type_name'>"
        
    Returns:
        str: 类型名称，小写
    """
    try:
        # 从"<class 'type_name'>"中提取"type_name"
        name = type_str.split("'")[1].lower()
        return name
    except (IndexError, AttributeError):
        return "unknown"

def get_mro(obj):
    """获取对象的方法解析顺序（继承链）
    
    Args:
        obj: 要获取MRO的对象
        
    Returns:
        list or None: 对象的MRO列表，如果不可用则返回None
    """
    try:
        if isinstance(obj, type):
            return obj.__mro__
        return type(obj).__mro__
    except (AttributeError, TypeError):
        return None

def get_type_category(obj_type_str):
    """根据对象的类型字符串确定其分类
    
    Args:
        obj_type_str: 对象类型的字符串表示
        
    Returns:
        str: 分类名称
    """
    type_name = get_type_name(obj_type_str)
    
    # 检查每个分类中是否包含该类型
    for category, types in initial_classes.items():
        if any(t.lower() == type_name for t in types):
            return category
            
    # 如果找不到匹配项，返回'other'
    return 'other'

def ox(
        theobj: object="test", 
        ifprint = True, 
        savefile: str | None = 'md', 
        show_inner_members: str = 'none', # none show both, True show only inner members, False show only outer members
        show_onlyknown: bool = False, 
        bygroup: bool = True
        ):
    """
    function ox list members of theobj

    param theobj: what to explor
    param savefile: "md", "json", "both", None, if save the results to a file (md or json, or both of 2).
    param show_inner_members: '_', '__', 'both'(_,__), 'none'(only outer members), if only show inner members of the object.
    param show_onlyknown: True ( 不包括非典型的自定义成员 ), False ( 包括非典成员 ), if only show known members of the object.
    param ifprint: True, False, if print the results on console.

    return: str results.

    """
    winww = terminal_size.columns-2
    # print(f'Width: {terminal_size.columns}, Height: {terminal_size.lines}')
    result_content_text = "\n"
    result_content_text += "_"*winww+"\n"
    result_content_text += "\n\033[1;44m OBJ'S TYPE: \033[0m\n\n"
    result_content_text += " "*4+str(type(theobj))+"\n"
    result_content_text += "_"*winww+"\n"
    result_content_text += "\n\033[1;44m OBJ'S MEMBERS: \033[0m\n"

    resjson["objname"]=str(theobj)

    print(result_content_text) if ifprint else None

    dirlist = dir(theobj)

    dirResult_sorted = sorted(
        dirlist, 
        key=lambda x: safe_type(theobj,x)
        )

    previous_type_str = ""
    dirjson = []
    atypeitm = []
    
    for objitem in dirResult_sorted:
        current_type_str = safe_type(theobj,objitem)

        if (previous_type_str != current_type_str):

            dirjson.append([current_type_str,[]])
            
            attrtype_all = initial_classes.get(current_type_str, ["other"])
            
            previous_type_str = current_type_str

        dirjson[-1][1].append(objitem)

    resjson["objitms"]=dirjson

    for iii in dirjson:
        
        content_title_typename = iii[0]
        result_content_text += "\n"+content_title_typename+"\n"
        print("\n"+" "*4+"\033[1;40;34m "+content_title_typename[8:-2].upper()+" \033[0m\033[40;34mmembers: \033[0m") if ifprint else None
        
        content_objs_list = ""
        for jjj in iii[1]:
            content_objs_list += jjj + ", "
            
        print(" "*4+content_objs_list + "\n") if ifprint else None
        result_content_text += content_objs_list + "\n"

    if savefile == "md" or savefile == "both":
        with open("objxp"+".md",'w', encoding="UTF-8") as ff:
            ff.write(result_content_text)

    if savefile == "json" or savefile == "both":
        with open("objxp"+".json",'w', encoding="UTF-8") as ff:
            ff.write(json.dumps(resjson))
    
    return result_content_text


# vars() is alternative to dirs(), or locals()


def what_is_vars():
    locals = vars().copy()
    for kk,vv in locals.items():
        print(kk,type())

    helpinfo = """
    vars() 是 Python 内置的一个函数，用于返回对象的 dict 属性，这是一个包含对象属性和它们值的字典。对于大多数 Python 对象，vars() 返回的是对象的命名空间。如果对象没有 dict 属性，比如内置类型或没有定义 dict 的自定义对象，vars() 将引发 TypeError。

    例如：
    ```python
    class MyClass:
        def __init__(self):
            self.a = 1
            self.b = 2

    obj = MyClass()
    print(vars(obj))  # 输出: {'a': 1, 'b': 2}
    ```
    在没有参数的情况下调用 vars()，它等价于 locals()，返回当前作用域中的局部符号表，也是一个字典。

    例如：
    ```python
    def my_function():
        x = 10
        y = 20
        print(vars())  # 输出: {'x': 10, 'y': 20}

    my_function()

    ```
    总结一下，vars() 主要用于获取对象的属性字典或当前作用域的局部符号表。


    """
        
if __name__=="__main__":
    ox(100)