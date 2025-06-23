import os
import json
import shutil
from typing import Literal, Optional, Union


def get_terminal_size_shutil():
    return shutil.get_terminal_size((80, 20))  # Default width and height

terminal_size = get_terminal_size_shutil()

initial_classes = {

    'func' : [
        "function",
        "module",
    ],
    
    'data' : [
        "int",
        "float",
        "bool",
        "str",
        "list",
        "dict",
        "set",
        "tuple",
    ],
    
    'builtin' : [
        "builtin_function_or_method",
    ],
    
    'other' : [
        "type",
        "method-wrapper",
        "nonetype"
    ]
}

    
resjson = {
    "objname":"",
    "objitms":[]
}


def safe_type(obj, attr):
    try:
        return str(type(getattr(obj, attr)))
    except Exception:
        return "unavailable"

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