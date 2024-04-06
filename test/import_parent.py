import os

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)
print('basename:    ', os.path.basename(__file__))
print('dirname:     ', os.path.dirname(__file__))
print('abspath:     ', os.path.abspath(__file__))
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))


def write2file(content_txt:str):
    print('[set target path 1]')
    target_path_1 = os.path.join(os.path.dirname(__file__), 'target_1.txt')

    print('target_path_1: ', target_path_1)

    print('write target file:')
    with open(target_path_1,"w", encoding="utf-8") as f:
        print(f.write(content_txt))
        
    return target_path_1


def copytxtfile(scr,dst):

    print('read target file:')
    with open(scr) as scrf:
        content_txt = scrf.read()
        
        with open(dst,"w",encoding="utf-8") as dstf:
            print(dstf.write(content_txt))

def normpath():
    
    print('[set target path 2]')
    target_path_2 = os.path.join(os.path.dirname(__file__), '../dst/target_2.txt')

    print('target_path_2: ', target_path_2)
    print('normalize    : ', os.path.normpath(target_path_2))

