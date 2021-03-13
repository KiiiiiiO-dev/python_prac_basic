print('''
    ########### TODO: ### 　リスト内包表記　 ##########################
    ネストしたfor-if, for-forであるリストをクルクルし、最終的に何らかの処理を加えた結果を、リストに詰める場合に利用
    ただし、ネストの階層が3つ以上になるような、可読性が下がる場合には、通常の書き方が〇
    ※あえて使いまくることも、また微妙
    ''')


t = (1, 3, 4, 5, 6, 7, 10)
t2 = (2, 12, 15, 16, 18, 19, 21)

r = [i for i in t if i % 2 == 0]
print(r)

r =  [i *j for i in t for j in t2]
print(r)






print('''
    ########### TODO: ### 　辞書内包表記　 ##########################
    ''')

t = ('a', 'b', "c", "d", "e", "f", "g")
t2 = (2, 12, 15, 16, 18, 19, 21)

r = {x: y for x, y in zip(t, t2)}
print(r)





print('''
    ########### TODO: ### 　集合内包表記　 ##########################
    ''')
s = set()

for i in range(10):
    s.add(i)

print('1---', s)

s = {i for i in range(10)}
print('2---',s)

s = {i for i in range(10) if i % 2 == 0}
print('3---',s)




print('''
    ########### TODO: ### 　ジェネレーター内包　 ##########################
    内容で囲うときは、「( )」を使う：yield は書かない
    Tupleにしたいときは、tuple(i for i in range(10))
    　　★頭にtupleと記載するのがポイント
    ''')
# 通常の書き方
def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print("other function...")
print(next(g))
print(next(g))
print(next(g))
print("other function...")
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 内包的な書き方 🛑() = でジェネレーター（yeild）という意味
g1 = (i for i in range(3))

print("------------",type(g1))
print(next(g1))
print(next(g1))
print("other function...")
print(next(g1))



print('''
    ########### TODO: ### 　名前空間とスコープ　 ##########################
    ''')

print("---", locals(), "\n\n")
print(globals())

# global()で出てくる、「関数名.__name__」「関数名.__doc__」として利用する、Python側が用意したもの



print('''
    ########### TODO: ### 　例外　 ##########################
    💎エラーの種類について確認

    💎書き方
    try:
        ～やりたい処理～
    except エラー名 as ex
        ～エラー時にしたい処理～
        print(ex)　←🟡エラー文の表示（ここに独自エラー文を記載してもOK）
    final:
        ～成功しても、エラーになっても実施したい処理～

    ''')

l = [1, 2, 3]
i = 1

# del l

try:
    # l[4] = i
    # l + i
    print('Try処理成功？')
# index out of range
except IndexError as ex:
    print("index-err_____", ex)
# name 'l' is not defined
except NameError as ex:
    print("name-err_____",ex)
# can only concatenate list (not "int") to list
except TypeError as ex:
    print("type-err____", ex)
except Exception as ex:
    print("🛑 このキャッチの仕方はNG！！悪事の丸め込み")
else:
    print("🟡Tryの処理が成功（エラーなし）したら実行される。この後にFinallyが実行")
finally:
    print("finally!!!!")






print('''
    ########### TODO: ### 　独自例外クラスの作成方法　 ##########################
    ''')
# １：Exceptionを継承して、独自の例外クラス名（～～Exception）とする
# ２：中身は「pass」とだけ記載　　～end～
class UppercaseMyException(Exception):
    # 🟡なにもしないという意味
    pass

# 独自例外を使用したい場合
def check():
    fruits = ["BANANA", "appple", "grape"]
    for fruit in fruits:
        if fruit.isupper():
            # 🟡「raise(レイズ)」は、強制的にエラーを発動する命令
            raise UppercaseMyException(fruit, '：：これは独自エラーです')


try:
    check()
except UppercaseMyException as ex:
    print('エラーコード999：', ex)
else:
    print('処理は成功しました！')
finally:
    print('function is exit.')






