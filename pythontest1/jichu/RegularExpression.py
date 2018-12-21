import re
a = 'abc, acc, adc, aec, afc'

r = re.findall('a[c-e]c', a)

print(r)
