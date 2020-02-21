'''import sys

count = sys.stdin.readline().strip()

result = 0
max = 0
for i in range(int(count)):
    el = sys.stdin.readline().strip()
    if el == '1':
        result += 1
    else:
        if max < result:
            max = result
        result = 0

print(max if max > result else result)
'''



'''#### №3
import sys
count = sys.stdin.readline().strip()
alist = []
ch = 0
for i in range(int(count)):
    el = sys.stdin.readline().strip()
    if el != ch:
        alist.append(el)
    ch = el
print(alist)
'''

'''##### №4

import sys

n = int(sys.stdin.readline().strip())


def foo(s, l, r, pairs):
    if l == pairs and r == pairs:
        print(s)
    else:
        if l < pairs:
            foo(s + '(', l + 1, r, pairs)
        if r < l:
            foo(s + ')', l, r + 1, pairs)


foo('', 0, 0, n)'''

'''##### №5

import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

l1 = list(s1)
l2 = list(s2)

l1.sort()
l2.sort()
print(l1, l2)
print(1 if l1==l2 else 0)


'''

##### №4

import sys

n = int(sys.stdin.readline().strip())


def foo(s, l, r, pairs):
    if l == pairs and r == pairs:
        print(s)
    else:
        if l < pairs:
            foo(s + '(', l + 1, r, pairs)
        if r < l:
            foo(s + ')', l, r + 1, pairs)


foo('', 0, 0, n)