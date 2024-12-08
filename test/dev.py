def ansi1():
    # print("\033[90m灰色\033[0m")  # 灰色
    # print("\033[91m红色\033[0m")  # 红色
    # print("\033[92m绿色\033[0m")  # 绿色
    # print("\033[93m黄色\033[0m")  # 黄色
    # print("\033[94m蓝色\033[0m")  # 蓝色
    # print("\033[95m紫色\033[0m")  # 紫色
    # print("\033[96m青色\033[0m")  # 青色
    # print("\033[97m白色\033[0m")  # 白色

    print("\033[100m灰BG\033[0m")  # 灰色
    print("\033[101m红BG\033[0m")  # 红色
    print("\033[102m绿BG\033[0m")  # 绿色
    print("\033[103m黄BG\033[0m")  # 黄色
    print("\033[104m蓝BG\033[0m")  # 蓝色
    print("\033[105m紫BG\033[0m")  # 紫色
    print("\033[106m青BG\033[0m")  # 青色
    print("\033[107m白BG\033[0m")  # 白色

    # print("\033[1;32m这是一个绿色的字体\033[0m")
    # print("这是一行普通的文本")

    for ii in range(111):
        print("\033["+str(ii)+"m"+str(ii)+"色\033[0m")


import sys

def print_ansi1():
    # 选择色彩方案
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m'
    }

    # 开始输出
    print("ANSI 编码示例")

    # 测试文本
    text = "Hello, World! "

    # 测试 ANSI 码
    ansi_codes = {
        "\u0007": "BEL (铃声)",  # 铃声
        "\u001B[3m": "RGB(Red)",   # 红色
        "\u001B[22m": "RGB(Green)", # 绿色
        "\u001B[31m": "RGB(Yellow)",# 黄色
        "\u001B[32m": "RGB(Blue) ", # 蓝色
        "\u001B[33m": "RGB(Magenta)",# 紫色
        "\u001B[34m": "RGB(Cyan) ", # 青色
        "\u001B[35m": "RGB(Red-Black)",
        "\u001B[36m": "RGB(Green-Black)",
        "\u001B[37m": "RGB(Yellow-Black)",
        "\u001B[40m": "RGB(White-Black)", # 白色
        "\u001B[41m": "RGB(Black-Red) ",
        "\u001B[42m": "RGB(Black-Green)",
        "\u001B[43m": "RGB(Black-Yellow)",
        "\u001B[44m": "RGB(Black-Blue) ", # 蓝色
        "\u001B[45m": "RGB(Black-Magenta)",# 紫色
        "\u001B[46m": "RGB(Black-Cyan) ",
        "\u001B[47m": "RGB(Bright Black)",
        "\u0008": "退格键",  # 退格键
        "\u001b[1;34m": "高亮红",
        "\u001b[31;1m": "反白红",
        "\u001b[32;1m": "反白绿"
    }

    for key, value in ansi_codes.items():
        print(f"{key} : {value}")

    # 结束输出
    print("\033[0m")

def print_ansi2():
    # 开始输出
    print("ANSI 编码示例")

    # 测试文本
    text = "Hello, World! "

    # 测试 ANSI 码
    ansi_codes = {
        "\u001B[30m": f"红色 {text}",
        "\u001B[32m": f"绿色 {text}",
        "\u001B[33m": f"黄色 {text}",
        "\u001B[34m": f"蓝色 {text}",
        "\u001B[35m": f"紫色 {text}",
        "\u001B[36m": f"青色 {text}",
        "\u001B[37m": f"白色 {text}",
        "\u001B[40m": f"黑色背景 {text}",
        "\u001B[41m": f"红色背景 {text}",
        "\u001B[42m": f"绿色背景 {text}",
        "\u001B[43m": f"黄色背景 {text}",
        "\u001B[44m": f"蓝色背景 {text}",
        "\u001B[45m": f"紫色背景 {text}",
        "\u001B[46m": f"青色背景 {text}",
        "\u001B[47m": f"亮黑背景 {text}"
    }

    for key, value in ansi_codes.items():
        print(f"{key} : {value}")

    # 结束输出
    print("\033[0m")



def print_ansi():
    print("所有 ANSI 样式")
    print("\033[1m粗体\033[0m")  # 粗体
    print("\033[2m下划线\033[0m")  # 下划线
    print("\033[3m倒影\033[0m")  # 倒影
    print("\033[4m高亮\033[0m")  # 高亮

    print("前景色:")
    print("\033[30m黑色\033[0m")
    print("\033[31m红色\033[0m")
    print("\033[32m绿色\033[0m")
    print("\033[33m黄色\033[0m")
    print("\033[34m蓝色\033[0m")
    print("\033[35m紫色\033[0m")
    print("\033[36m青色\033[0m")
    print("\033[37m白色\033[0m")

    print("背景色:")
    print("\033[40m黑色BG\033[0m")  # 黑色背景
    print("\033[41m红色BG\033[0m")  # 红色背景
    print("\033[42m绿色BG\033[0m")  # 绿色背景
    print("\033[43m黄色BG\033[0m")  # 黄色背景
    print("\033[44m蓝色BG\033[0m")  # 蓝色背景
    print("\033[45m紫色BG\033[0m")  # 紫色背景
    print("\033[46m青色BG\033[0m")  # 青色背景
    print("\033[47m白色BG\033[0m")  # 白色背景

    print("组合:")
    print("\033[1;30m粗体黑色\033[0m")
    print("\033[2;31m下划线红色\033[0m")
    print("\033[3;32m倒影绿色\033[0m")
    print("\033[4;33m高亮黄色\033[0m")

    # # 组合所有样式
    # for i in range(100):
    #     if i < 10:
    #         print(f"\033[{i}m 背景\033[0m")
    #     else:
    #         num = i // 10 * 10 + (i % 10)
    #         if num < 40:
    #             print(f"\033[{num}m 前景色\033[0m")
    #         elif num < 80:
    #             print(f"\033[{num}m 背景\033[0m")
    #         else:
    #             print(f"\033[{num}m 组合前景和背景\033[0m")




if __name__ == "__main__":
    print_ansi()
