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

def oxdir(oo):
    # 莫名其妙
    print(len(dir(oo)))
    for ooo in dir(oo):
        print(ooo)

def oxvars(oo):
    # 莫名其妙
    # TypeError: vars() argument must have __dict__ attribute
    print(len(vars(oo)))
    for ooo in vars(oo):
        print(ooo)


# 方式2：限制为特定可选值（需Python 3.8+）
    # 莫名其妙
def set_direction(direction: Literal["left", "right", "up", "down"] = "left") -> None:
    print(f"Moving {direction}")

# 方式3：可选参数（允许None）
    # 莫名其妙
def connect(timeout: Optional[int] = None) -> None:
    timeout = timeout or 30  # 默认值30

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

def classify_member(obj, member_name):
    """对对象的成员进行分类
    
    Args:
        obj: 要检查的对象
        member_name: 成员名称
        
    Returns:
        tuple: (category, subcategory, value)
    """
    try:
        # 首先检查是否是属性
        cls = obj if isinstance(obj, type) else type(obj)
        if hasattr(cls, member_name):
            member_descriptor = getattr(cls, member_name)
            if isinstance(member_descriptor, property):
                try:
                    value = getattr(obj, member_name)
                    return ('property', 'property', str(value)[:100])
                except Exception:
                    return ('property', 'property', '<unavailable>')
        
        member = getattr(obj, member_name)
        member_type = safe_type(obj, member_name)
        type_name = get_type_name(member_type)
        member_value = str(member)[:100]  # 限制值的长度
        
        # 检查是否是特殊方法
        if member_name.startswith('__') and member_name.endswith('__'):
            for subcategory, methods in special_methods.items():
                if member_name in methods:
                    return ('special', subcategory, member_value)
            return ('special', 'other_special', member_value)
        
        # 获取基本分类
        category = get_type_category(member_type)
        
        # 如果是其他类型，尝试通过继承关系确定更具体的分类
        if category == 'other':
            mro = get_mro(member)
            if mro:
                for base in mro[1:]:  # 跳过自身
                    base_type = safe_type(base)
                    base_category = get_type_category(base_type)
                    if base_category != 'other':
                        return (base_category, get_type_name(base_type), member_value)
        
        return (category, type_name, member_value)
    except Exception as e:
        return ('other', 'unavailable', '<unavailable>')

def ox(
        theobj: object="test", 
        ifprint: bool = True, 
        savefile: Optional[str] = 'md', 
        show_inner_members: str = 'none',
        show_onlyknown: bool = False, 
        bygroup: bool = True
        ):
    """探索对象的成员并进行分类
    
    Args:
        theobj: 要探索的对象
        ifprint: 是否在控制台打印结果
        savefile: 保存结果的文件格式（"md"/"json"/"both"/None）
        show_inner_members: 内部成员显示选项（'_'/'__'/'both'/'none'）
        show_onlyknown: 是否只显示已知类型的成员
        bygroup: 是否按组显示结果
    
    Returns:
        str: 格式化的结果文本
    """
    winww = terminal_size.columns-2
    result_content_text = "\n" + "_"*winww + "\n"
    
    # 显示对象类型信息
    obj_type = safe_type(theobj)
    obj_category = get_type_category(obj_type)
    result_content_text += f"\n\033[1;44m OBJECT TYPE: {obj_type} (Category: {obj_category}) \033[0m\n\n"
    
    # 如果对象有文档字符串，显示它
    if hasattr(theobj, '__doc__') and theobj.__doc__:
        doc = theobj.__doc__.strip().split('\n')[0]  # 只显示第一行
        result_content_text += f" Documentation: {doc}\n"
    
    result_content_text += "_"*winww + "\n\n\033[1;44m OBJECT MEMBERS: \033[0m\n"
    
    if ifprint:
        print(result_content_text)
    
    # 获取并分类所有成员
    members = dir(theobj)
    classified_members = {}
    
    for member in sorted(members):
        # 处理内部成员过滤
        is_dunder = member.startswith('__') and member.endswith('__')  # 特殊方法
        is_private = member.startswith('_') and not member.startswith('__')  # 单下划线
        is_very_private = member.startswith('__') and not member.endswith('__')  # 双下划线

        # 根据show_inner_members参数过滤
        if show_inner_members == 'none':
            # 不显示任何内部成员
            if member.startswith('_'):
                continue
        elif show_inner_members == '_':
            # 只显示单下划线成员，不显示双下划线和特殊方法
            if not is_private or is_dunder or is_very_private:
                continue
        elif show_inner_members == '__':
            # 只显示双下划线成员，不显示单下划线和特殊方法
            if not is_very_private or is_dunder:
                continue
        # 'both' 显示所有成员，不需要过滤
        
        # 处理名称修饰（name mangling）
        display_name = member
        if is_very_private and not isinstance(theobj, type):
            # 对于实例对象，需要处理名称修饰
            cls_name = theobj.__class__.__name__
            display_name = f"_{cls_name}{member}"
        
        # 分类成员
        category, subcategory, value = classify_member(theobj, member)
        
        # 如果只显示已知类型且当前类型为'other'，则跳过
        if show_onlyknown and category == 'other':
            continue
        
        # 将成员添加到分类中
        if category not in classified_members:
            classified_members[category] = []
        classified_members[category].append({
            'name': display_name,
            'type': subcategory,
            'value': value
        })
    
    # 准备JSON输出
    resjson["objname"] = str(theobj)
    resjson["objitms"] = []
    
    # 按分类显示结果
    for category in sorted(classified_members.keys()):
        members = classified_members[category]
        if not members:
            continue
        
        # 添加分类标题
        # 如果是descriptor类别且包含property类型，显示为PROPERTY
        display_category = "PROPERTY" if category == "descriptor" else category.upper()
        result_content_text += f"\n\033[1;40;34m {display_category} \033[0m\n"
        
        # 显示该分类下的所有成员
        for member in sorted(members, key=lambda x: x['name']):
            # 对于属性，简化显示格式
            if category == 'descriptor' and member['type'] == 'property':
                member_text = f"{member['name']}"
                if member['value'] != '<unavailable>':
                    member_text += f": {member['value']}"
            else:
                member_text = f"{member['name']} ({member['type']})"
                if member['value'] != '<unavailable>':
                    member_text += f": {member['value']}"
            result_content_text += f"    {member_text}\n"
        
        # 为JSON输出准备数据
        resjson["objitms"].append([
            category,
            [member['name'] for member in members]
        ])

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