'''
多重剪贴板
利用关键字，保存每段剪贴板文本，然后通过关键字索取文本

1.针对要检查的关键字，提供命令行参数
2.如果参数是save，那么剪贴板的内容保存到关键字
3.如果参数是list，就将所有的关键字拷贝到剪贴板
4.否则，就将关键字对应的文本拷贝到剪贴板。
    代码需要做到：
    1.从sys.argv读取命令行参数
    2.读写剪贴板
    3.保存并加载shalf文件
'''
#! python3

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
