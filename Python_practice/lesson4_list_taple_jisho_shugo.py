print('''
      
      ################### TODO:####### list ##########################
      
      ''')
# ✅リストの使いどころ✅
# ・バスの乗車の乗り降り（AI運行バスなど）
#   ※最小座席0席～上限座席6席とする
# 　　ー乗客Aが乗った[A]：リスト.append(A)
#   　ー最小座席以上 ＆ 上限座席以内 か判定
#    ーTrueなら、乗客受付
#    ーFalseなら、乗客拒否
#    ー乗客B、Cが乗車：リスト.append(B),リスト.append(C)
#    ー乗客Aが下車：リスト.pop(A)

from typing import Tuple


r = [1, 4, 5, 6, 2, 5, 6, 7, 7, 1]

#ただの逆順
r.reverse() 
print(r)

#小さい順 [1, 1, 2, 4, 5, 5, 6, 6, 7, 7]
r.sort()
print(r)

#整えて逆順
r.sort(reverse=True)
print(r)

# リスト内に7はいくつあるか
print(r.count(7))

# rのリスト内に5があるか
if 5 in r:
    print('yes')
else:
    print('no')
    
# 〇.split(ココ)←に入った値ごとに、区切ってリスト化する
# ['My', 'name', 'Kii', 'Kob!!']
str1 = 'My name Kii Kob!!'
to_split = str1.split(' ')
print(to_split)

# 上のリストを「"何で区切るか".join(変更したいリスト)」で元の文章に戻す
# My name Kii Kob!!
str2 = " ".join(to_split)
print(str2)

print('''
      
      ##################### TODO:##### list コピー ##########################
      
      ''')

#リストのコピー
#TODO:※重要※一般的な代入は、参照渡し（アドレスだけ渡す）、値渡し（実値を渡す）わけではない

#通常変数は「値渡し」
x = 2
y = x
y += 3
print(f'x={x}, y={y}')

#リストは「参照渡し」
r2 = [1, 10, 100, 1000]
rc21 = r2.copy()
# 👆について：「rc21 = r2[:]」とも書けるが可読性が低いため、上を利用するようにする
rc22 = r2 #★ r2にも影響する


rc21.append(888)
print(f'rc21 ( copy() 値渡し )  = {rc21}')
print(f'r2   = {r2}')

rc22.append(99)
print(f'rc22 ( = 参照渡し )　　  = {rc22}')
print(f'r2   = {r2}')



# ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
# ◆◆◆　Tuple　◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆

print('''
      
      #################### TODO:###### tuple ##########################
      
      ''')

# ✅Tupleとは？　使いどころは？✅
#　📌「Tuple」とは、リストの要素変更できないバージョン
# ・ある選択肢（これをTuple）の中から、複数選択する
#  　ー理由：選択肢を変更されたくない
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('B')

print(chose_from_two)
print(answer)
print('''
      
      ###########################################
      
      ''')





# 🟡　Tuple中のリストは、変更することができる
t = ([1, 2, 3], [3, 5, 6])
t[0][1] = 100
print(t)

# 🟡省略したTupleの書き方
t = 1, #カンマを入れると、自動でTupleになる。
t = 1, 2, 3
t = () # これもタプルになる

# 🟡Tapleに追加するには、「結合：＋」を使う　(1, 2, 3, 11, 12, 13)
t = (1, 2, 3) + (11, 12, 13)
print(t)

print('''
      
      ### TODO:##### バグの温床：tuple #######
      
      ''')
# 🛑バグの温床🛑Tupleの注意点
# Tuple以下のように書いても、Tupleにならない。（ ）内の属性になる
tx = (1) # int
tx2 = ('タプルじゃない！Str！')
print(type(tx2))

# 🟡　要素の入れ替えをする
a = 100
b = 200

print(f'RowData: a = {a}, b = {b}')

a, b = b, a
print(f'変更後: a = {a}, b = {b}')


print('''
      
      #################### TODO:###### 辞書 ##########################
      🛑参照渡し
      ''')

# 🟡　辞書の作り方 2 種類
d1 = {'mike' : 18, 'jane' : 36, 'dan' : 30}
d1['bob'] = 26
d1['kii'] = 33
d1['kob'] = 28
print(d1)

d2 = dict(taro = 10, jun = 20, gaga = 30)
print(d2)


d1 = dict(x=100, y=200, z=300)
d2 = dict(x=100, y=200, xx=999)
print(d1)
print(d2)

# 🟡　ダブりなしのものだけ追加
d1.update(d2)
print(d1)

#　🛑（使用注意）辞書自体を削除
# del d1
# print(d1) #エラーになる「 NameError: name 'd1' is not defined 」

# 🟡中身を削除
d2.clear()
print(d2)


# 🟡🟡🟡辞書内に要素が存在するかチェックする方法
print("x" in d1) #True

print('''
      
      #################### TODO:###### 集合 ##########################
      　➡重複した値が自動で省かれる
      　➡ 辞書のKeyがないリストのようなもの
       ➡リストと違い、Indexがない（エラーになる）
       
       ✅使いどころ
      　　・共通の友人一覧を表示したいとき
        　　Aさんと共通の友人：「Zさん」「Yさん」
          A_friends = {1, 2, 2, 5, 6, 6}
      　　B_friends = {Z, 3, 4, Y, 7, 8}
          print(a & b)
       
      ''')

a = {1, 2, 2, 5, 6, 6}
print(a)

b = {2, 3, 4, 5, 6, 7}

# 「a」だけにあるものが出る; {1}
print(a - b)
# 「b」だけにあるものが出る：{3, 4, 7}
print(b - a)

# 「a」「b」に共通しているもの：{2, 5, 6}
print(a & b)
# 「a」「b」にそれぞれあるものを重複なく表示：{1, 2, 3, 4, 5, 6, 7}
print(a | b)
# 「a」「b」で、重複していないもの
print(a ^ b)

# 🛑足し算はできない
# print(a + b)

# 🟡リストからの型変換使うこともある（例：どの種類を購入したかなど）
f = ['apple', 'banana', 'apple', 'banana']
# リストから集合型に変換したいとき
kind = set(f)
print(kind)



