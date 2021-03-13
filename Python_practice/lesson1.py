

from typing import List


l = [0, 1, 2, 3, 4, 5, 6]

print("index--0--",l[0])
print("index-- 2: --",l[2:])
print("index- :2 ---", l[:2])

print(list("abcdefg"))

# 何を付け足したいか
l.append(100)
print(l)
# どこに何をいれたいか
l.insert(2,1000)
print(l)
# 消したい値を入れる
l.remove(1000) 
print(l)
 # 取り出したいIndex or 空ならさっき入れたやつが取り出される
print(l.pop(1))
print(l)

print("################")

r = [1, 2, 3, 4, 5, 6]
r.reverse()
print(r)

str1 = "my name is k."

#下は ['my', 'name', 'is', 'k.']となる
to_split = str1.split(" ")
print(to_split)

print("####################")

# TODO:my###name###is###k.　となる
x = "###".join(to_split)
print(x)

x               =1






# if 1 > 0 :
#     print("hello!")
# else:
#     print("why")

# print("exit")


# a = 'a'
# print(f'a is {a}')
 
# x, y, z = 1, 2, 3
# print(f'a is {x}, {y}, {z}')
# print(f'a is {z}, {y}, {x}')
 
# name = 'Jun'
# family = 'Sakai'
# print(f'My name is {name} {family}. Watashi ha {family} {name}')



name = 'jun'
family = 'kob'
print(f'My name is {name}, {family}!hello!!')