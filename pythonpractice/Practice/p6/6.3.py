#书本项目：6.3，口令保管箱（密码保管箱）
#原理：如果在电子邮件，游戏等账号中使用同一个密码，可能会导致密码泄露，
#因而建立一个简单的密码保管箱，通过剪切板来保管密码，用到那个账号，
#输入账号，可以从保管箱中通过复制粘贴调出密码

# ! python3
# 6.3.py - An insecure password locker program
PASSWORDS = {'email':'F(D(FS(DF(SD*F(SDF&*DS&*&F',
            'blog':'FD(FS()0f9sdDF(SDF9',
            'Wechat':'123456'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py 6.3.py[account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account)



