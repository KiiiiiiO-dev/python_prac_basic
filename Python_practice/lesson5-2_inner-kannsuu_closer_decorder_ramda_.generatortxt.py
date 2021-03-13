print('''
    #################### TODO:###### 　インナー関数　##########################
    関数の中で、ある処理を繰り返したい場合に利用。
    ''')

def outer(num1, num2):
    def calc(num3, num4):
        return (num3 + 10) - num4
    # 🟡ここで処理を繰り返したい
    r1 = calc(num1, num2)
    r2 = calc(num2, num1)

    return r1 + r2

print(outer(3, 5))





print('''
    #################### TODO:###### 　インナー関数を直接実行　##########################
    ''')
def sample():
    def b():
        print('hello')
    return b

sample()()





print('''
    #################### TODO:###### 　クロージャ―　 ##########################
    📌インナー関数（処理機能）をReturnで返す関数
    　　計算式が同じで、ある値だけ変えて、状況に合わせて計算したいときに使用。

    ◆例：
    円の面積を求めるとき、円周率πを、「3」とするか、「3.14」とするか、「3.141592」と詳しく計算するか
    状況に合わせて計算したい。

    ✅使い方
        １：外側の関数に引数（状況によって変わる値：円周率など）を入れて、完成したインナー関数をReturnで受け取り変数へ。
        ２：処理入りの変数に（）をつけ、該当の引数を入れ、欲しい値を取得
    ''')

#指定したπの入った処理を返す
def circle_area_func(pi):
    #指定されたπで、円の面積を求め、値を返す
    # ある値を入れたら完成する、本当に求めたい式
    def circle_area(radius):
        return radius * radius * pi
    return circle_area

c_easy = circle_area_func(3)
c_normal = circle_area_func(3.14)
c_detail = circle_area_func(3.141592)

print('簡単計算：', c_easy(10))
print('通常計算：', c_normal(10))
print('詳細計算：', c_detail(10))


#####################　練習　#######################
def circle_area_func(pi):
    def circle_area(radius):
        return radius * radius * pi
    return circle_area

c_easy = circle_area_func(3)
c_normal = circle_area_func(3.14)
c_detail = circle_area_func(3.141592)

print('easy', c_easy(10))
print('normal', c_normal(10))
print('detail', c_detail(10))







print('''
    #################### TODO:###### 　デコーダー　 ##########################
    📌デコレータとは、対象の関数に対して、別処理を付け加える関数のこと（関数の中身を書き換えずに関数を修飾）。

    ライブラリ内の関数の機能を変更したいときなどに役立ちます。
     また、自身でクラスメソッドやスタティックメソッドを定義する際には
     @classmethodや@staticmethodと記述するのがPythonでは一般的

     💎とにかく、元の処理の前後に、何らかの処理を付け加えたいときに使う
     💎元処理に計算を加えたい場合は、resultで返してあげると良いカモ
    ''')

def arrenge_func(func):
    #関数そのものを返す
    def wrapper(*args,  **kwargs):
        print('Start！')
        # 実際の処理に文章を足した
        result = f'「{func(*args, **kwargs)}」が答えだそうですよ？'
        print('答えは・・・')
        # 後で結果を受け取って、別の処理をしたい
        return result
    return wrapper


def arrenge_func_2(func):
    #関数そのものを返す
    def wrapper(*args,  **kwargs):
        print('Second Start！')
        # 実際の処理に文章を足した
        result = f'「{func(*args, **kwargs)}」これは func_2 ですよ？'
        print('2回目の答え')
        # 後で結果を受け取って、別の処理をしたい
        return result
    return wrapper

# 🟡アテンション名の処理に、以下の関数をぶち込む
@arrenge_func
@arrenge_func_2#🛑順番注意🛑 コッチが内包される　💎arrenge_func(arrenge_func_2(add_num(10,30)))といった感じ
def add_num(num1, num2):
    return num1 * num2

#ここで「result」の文章を表示している
print(add_num(10,30))




print('''
    ################### TODO:####### 　ラムダ　 ##########################
    2行目でreturnを書くような単純な関数を、一行で書けるもの
    ''')
# 通常通り書いた場合
def sample(word: str):
    return word.capitalize()

# 🟡ラムダで書いた場合
sample_func = lambda word: word.capitalize()

# 🟡🟡🟡引数に直接入れることもできる
def word_capitalize(word, func):
    print(func(word))

word_capitalize('aaa', lambda word: word.capitalize())




print('''
    #################### TODO:###### 　ジェネレーター　 ##########################
    重い処理を必要箇所に分割して、実行したい場合に利用
    ''')