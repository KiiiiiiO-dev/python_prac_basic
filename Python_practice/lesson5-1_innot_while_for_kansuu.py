
from typing import DefaultDict






print('''
      #################### TODO:###### 比較演算子　論理演算し ##########################
      　==, !=, <, >, <=, >=, and, or
      ''')

    #    🟡 Trueとみなすもの：True, 0以外の数字, 文字列が入っている
    #           📌Listの中身があるときもTrue！！
    #    🟡 Falseとみなすもの：False, 0, ''(空文字)
    #           📌Listの中身が ”空” なら、False！！

x_friends = ['a', 'b', 'c', 'd', 'e']
# x_friends = []

if x_friends:
    print('-----OK')
else:
    print('----NOOO')






print('''
      #################### TODO:###### 「in」「not」 ##########################
      in ➡ 含まれているか？
      not　➡　～じゃない
      ''')

#   ✅Boolean型で否定したいとき
#     is_ok = False
#     if not is_ok:
#      ~何らかの処理~

x_list = [1, 3, 5, 6]
y = 60

if y in x_list:
    print('yes!')

if y not in x_list:
    print('no!')

is_ok = False
if not is_ok:
     print('Nooooo')






print('''
      ################### TODO:####### 「is」と「Noneチェック」 ##########################
       ➡「is」：同じオブジェクト（クラス）か
       ➡「None」：何もない
       ➡ リストなどの空判定は、前述の「if リスト名:」でOK
      ''')

is_empty = None

# 🛑 None判定するときは、isを使う！
if is_empty is not None:
    print('空じゃない')

if is_empty is None:
    print('空エラー')






print('''
    #################### TODO:###### 「While」 ##########################
    ✅使いどころ：ある条件に合致するまでループしたいとき
    ''')
# 🛑変数の箱と、カウンターを設定する必要がある

counter = 0
while counter < 5:
    if counter == 1:
        # 🛑 While文自体を抜ける＝Elseも通らない
        break
    print(counter)
    # 🛑 ↓ 忘れないように
    counter += 1
else:
    print('Done!')






print('''
    ##################### TODO:##### 「Input関数」 ##########################
    ✅コンソール上で入力受付したいとき
    ''')
# # 実行がInoutでとまるため、コメントアウト
# while True:
#     # 金持ちに35歳までになる人？ >>
#     word = input('金持ちに35歳までになる人？ >>')
#     if word == 'yes':
#         break
#     print('next!!')







print('''
    ##################### TODO:##### 「for/ break / continue」 ##########################
    🟡break : for文自体から抜ける
    🟡continue：そのループを抜け、次のループへ
    ''')
job_friends = ['A', 'B', 'C', 'D', 'X']

for friend in job_friends:
    print(friend)


for friend in job_friends:
    # if friend == 'D':
    if friend == 'None!':
        print('Stop!!')
        # 🟡 break: for文から抜ける
        break
# 🟡 break されなければ到達
else:
    print('All Come on!!')






print('''
    ###################### TODO:#### 「range関数」 ##########################
        ➡数字の入ったリストのようなもの？
        　➡3~5、0~8
        ➡何回まわすか指定したいときに使用
    ''')


# 🟡 10回回したい
# 0 hello!
# 1 hello!
# 2 hello!
# 3 hello!

for i in range(10):
    print(i, 'hello!')

# 🟡for文内で、変数を利用しない時は、「_」で省略できる
for _ in range(10):
    print('hello!')

# 🟡🟡🟡 Listの要素分クルクル
job_friends = ['A', 'B', 'C', 'D', 'X']
for friend in range(len(job_friends)):
    print('------', friend)

# 🟡range(スタート数字、〇まで、何個飛ばし？)
for i in range(3, 11, 2):
    print(i)





print('''
    ##################### TODO:##### 「enumerate（イナムレート）関数」 ##########################
        ➡for内の変数を複数利用したい場合に利用
    ''')

#🟡出力結果
# 0 A
# 1 B
# 2 C
# 3 D
# 4 X
for i, friend in enumerate(job_friends):
    print(i, friend)

about_list = ['K', 'L', 'G', 'X']
for i, about in enumerate(about_list):
    print("\n",i, about)





print('''
    ##################### TODO:##### 「Zip関数」 ##########################
        ➡複数のリストを、同時にぐるぐる展開していきたい時に使う
    ''')

days = ['mon', 'tue', 'wed', 'thr']
foods = ['meat', 'fish', 'rice', 'apple']
drinks = ['cola', 'tea', 'coffee', 'milktea']

#🟡出力結果
# mon meat cola
# tue fish tea
# wed rice coffee
# thr apple milktea
for day, food, drink in zip(days, foods, drinks):
    print(day, food, drink)






print('''
      🟡🟡🟡  良く利用される🟡🟡🟡
    ###################### TODO:#### 「辞書（map/dct）」をfor文で取り出す ##########################
    ''')

food_dct = {'apple': 2, 'banana': 8, 'grape': 12}

#　🛑　○○.items()を利用することで、中身のKeyとValueを取り出せる
for k, v in food_dct.items():
    print(k, v)






print('''
    ###################### TODO:#### 　関数　 ##########################
    ''')

# 🛑　引数の型は、Pg向けメモのようなもん
# 🛑🛑　間違った型が入っても、エラーを吐かない
def someting(name: str, age: int) :
    return (name + '天才！', age + 100)

# 🟡関数は変数に入れることができる
f = someting
print(f('bob', 27))
print(f('gaga', 32))

# 🟡🟡引数のミスを減らす方法（これだと、型チェックができるみたい）
print(someting(name='kii', age=33))


def sayHi():
    return 'Say Hi !!'

print(sayHi())





print('''
    ##################### TODO:##### 　デフォルト値のある関数　 ##########################
    ''')

# 🟡引数が未入力の場合に、デフォルト値を適用する
def defult_someting(name='名無しさん', age=0, girlfriend=True):
    print(name, age, girlfriend)
# 🛑デフォルト値がない場合：必須の引数をいれないとエラー
# 🛑デフォルト値がある場合、引数を渡すと、引数で「上書き」される
defult_someting('hello')


# 🛑🛑🛑引数にリスト系（というか参照渡しのもの）は渡すな！、リストは関数内で、その都度つくれ！
def bad_sample(num, item_list=[]):
    item_list.append(num)
    return item_list

print(bad_sample(100))
# 🛑【バグの温床】🛑関数のデフォルトリストが参照渡しされる➡その一つのリストに、関数実行のたびに追加されてしまう…
# [100]
# [100, 999]
print(bad_sample(999))

# ⭕解決策⭕　参照渡し系の型は、デフォルト「None」
#もし、何かかしらのリストなどあれば、引数に渡す。それ以外は引数に渡さずデフォルト値を使う
def good_sample(num, item_list=None):
    #🟡 Noneの「型チェック」は「is」
    if item_list is None:
        item_list = []
    item_list.append(num)
    return item_list

print(good_sample(8))
# 🛑この解決方法なら、他人のリストにItemが追加されることがない
print(good_sample(100))




print('''
    ##################### TODO:##### 　「個数不明な引数を受け取る」関数　 ##########################
    受け取った「*args（引数）」は、タプル化される
    ''')

# 🟡たとえば、複数選択の時に利用できる？
def dont_know_args(user_id, *args):
    print('user_name = ',user_id)
    for arg in args:
        print(arg)

# 🟡出力結果
# 2 ('a', 'b', 'C')
dont_know_args(2, 'a', 'b', 'C')

# 🟡（あまり使わない）🛑引数には、タプルで渡すこともできる
t = ('aaa', 'bbb', 'xxx')
# ❌「*」をつけないと、タプルのまま引数となる
dont_know_args(888, t)
# ⭕ 「*」をつけることで、展開してくれる
dont_know_args(888, *t)





print('''
    #################### TODO:###### 　「キーワード引数の辞書化」関数　 ##########################
    🟡🟡🟡🟡🟡よく使われる🟡🟡🟡🟡🟡
    ''')

def menu(**kwargs):
    print(kwargs)
    # 🛑「.items()」をつけ忘れないように！
    for k, v in kwargs.items():
        print(k, v)

# 1つ目の方法：🛑キーワード引数として渡す（ k=v ）
menu(name='bob', age=28, msg='hello!')


# 2つ目の方法：🛑カンマをつけ忘れない
someting_dct = {
    'name': 'bob',
    'age': 24,
    'friend_count': 15
}
# 🛑「**」を入れないとエラーになる
menu(**someting_dct)


def sometion_args(**kwargs):
    for k, v in kwargs.items():
        print(k,v)

d = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

sometion_args(**d)



print('''
    #################### TODO:###### 　「通常」「*args」「**kwargs」を全て引数とする　 ##########################
    🟡🟡🟡使われる？🟡🟡🟡
    ''')

# 🛑 「*」の数が少ない方を、先に書かないとエラー
def arg_someting(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

# ✅出力結果
# jhon
# ('banana', 'apple', 'grape')
# {'user_id': 1, 'user_name': 'JN'}
arg_someting('jhon',
             'banana', 'apple', 'grape',
             user_id=1, user_name='JN')


print('''
    ##################### TODO:##### 　「Doc」の書き方 ##########################
    ''')
'''
✅関数の上ではなく、関数内の1行目にに書く
✅書き方

　"""ここに関数の機能概要
    Args:
        param1 (int):~~~
        param2 (str):~~~

    Returns:
        bool:~~~~~
  """
  
  ✅Docの読み込み方法
  help(関数名)
  もしくは。「関数名.__doc__」

'''