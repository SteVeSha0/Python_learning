#疯狂填词游戏
# 1.读取txt文件
# 2.读出文件中的ADJECTIVE等关键词组成序列
# 3.允许拥护输入顺序替换关键词，组成新的文本
# 4.将新的文本打印出来，并形成一个新的txt文本

import re

text_file = open('p8\\p8.9.2\\text.txt')
text_read = text_file.read()

def user_input():
    user_inputs = input()
    return user_inputs

print('Enter an adjective:')
user_input_adj = user_input()
text_read = re.sub(r'ADJECTIVE', user_input_adj, text_read, 1)

print('Enter an noun:')
user_input_nou = user_input()
text_read = re.sub(r'NOUN', user_input_nou, text_read, 1)

print('Enter an verb:')
user_input_ver = user_input()
text_read = re.sub(r'VERB', user_input_ver, text_read, 1)

print('Enter an noun:')
user_input_noun = user_input()
text_read = re.sub(r'NOUN', user_input_noun, text_read, 1)

print(text_read)

text_new_file = open('p8\\p8.9.2\\text_new.txt', 'w')
text_new_file.write(text_read)

text_file.close()
text_new_file.close()