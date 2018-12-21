#在Wiki标记中添加无序表
#创建一个无序列表，让每个列表占据一行，并在前面放置一个星号。
# join方法为将列表中的每个元素之间加入字符串，然后以字符串形式连续输出
# slip方法为读取字符串，读到某个特性字符作为分割，将字符串以序列形式输出

import pyperclip

text = pyperclip.paste()

line = text.split('\n')

for i in range(0,len(line)):
    line[i] = '*' + line[i]

text = '\n'.join(line)

pyperclip.copy(text)