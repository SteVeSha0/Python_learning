#书本实例，用正则表达式进行电话号码和E-mail提取
#复制一段文本，从复制的文本中提取电话号码和email粘贴打印出来

#! python3

import pyperclip, re

#创建一个正则表达用于匹配电话号码，西方格式
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    )''', re.VERBOSE)

#创建一个正则表达式用于匹配email地址

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)


#从剪切板的文本中找到所有匹配
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#所有匹配连接成一个字符串，复制到剪切板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email addresses found.')