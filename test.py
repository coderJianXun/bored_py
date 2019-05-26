import re

p = re.compile('c[b-d]t')
print(p.match('cft'))
