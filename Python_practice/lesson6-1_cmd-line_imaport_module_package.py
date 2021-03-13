# 🛑# 🛑# 🛑# 🛑# 🛑# 🛑
# import したファイル内に、「__○○__」や「○○()」などの関数が書かれていた場合、
# import文を読み込む際に、実行されてしまう。
# それを防ぐには、main以外のファイルで、以下のように記述するべし！
#
# if __name__ == '__main__':
    #そのファイル自体の動作確認したいときに、テスト感覚で残しておきたい関数を、このif文に閉じ込める
    # print(eat())
# 。
# プロジェクトの実行は、mainファイルの、main()からすべてが始まるようにする
# 🛑# 🛑# 🛑# 🛑# 🛑# 🛑





# import lesson_basic.lesson_package.utils
# 🛑「..○○」で、1階層上へ戻ることができる（相対パス）
#       👆ただし、今どこの階層か探す手間があるため、非推奨。基本は以下書き方。
# 🛑呼び出し時に、絶対パスですべて書くか、モジュール名から書く（util.talk()）かは、現場のルール次第
from lesson_package.talk import animal, human
# 🛑主にファイルで[imporet *」で、どれを読み込んでもらうか、を定義するために以下のように書く
        # 👆ただし、推奨された書き方ではない。ファイルで「*」だと、具体的にどのファイルから呼ばれたかわからないため。
# from lesson_package.talk import *
from lesson_package import utils



print('''
    ########### TODO: ### 　コマンドライン　 ##########################
    ''')






print('''
    ######:##### TODO: ### 　パッケージの使い方　 ##########################
    1: 新規フォルダー作成で、Packageを作成する
    2: 1のフォルダーの中に、「__init__.py」、「その他モジュール（ex：utils.py）」などを作成
    　　➡「__init__.py」がないと、Python上でPackageとして認識されない＝必須
      　➡
    ''')

# 🟡ファイル上部のimport文を見ながら、復習すること

# print(lesson_basic.lesson_package.utils.say_twice('hello'))
print(utils.say_twice('hello'))
# 🟡インポートするときは、もじゅるー名から呼び出すようにする（どこから呼ばれているかを明確化するため）
        # from lesson_package.talk import animal, human
human.talk()
human.eat()
# 🟡インポートにアスタリスクをつければ、Talkパッケージ内の全てのファイルを利用できるようになる
        # from lesson_package.talk import *
animal.eat()
animal.talk()





print('''
    ########### TODO: ### 　importエラーの回避方法（エラーハンドリング）　 ##########################
    古いパッケージと新しいパッケージで、呼び出したいモジュールの階層が異なるときに役立つ
    ''')

# 🟡ファイル上部で行う
try:
    # 例えば、古いパッケージの場合はコッチ
    from lesson_package.talk import animal, human
except:
    #  古いパッケージのアクセスができなくなっていれば、新しいパッケージを呼び出すようにする
    from lesson_package import animal, human






print('''
    ######:##### TODO: ### 　setup.py（パッケージ化して配布）　 ##########################
    ''')






print('''
    ########### TODO: ### 　sorted() , 組み込み関数　 ##########################
    モジュールをimportしなくても、使える関数のこと
        ex: print(), input(), global(), local(), sorted()とか
    ''')

# 特にりようされるSortedの使い方も観てみる
ranking = {
    'A': 75,
    'B': 100,
    'C': 98
}
# 🟡「ranking辞書」が、「点数」が「高い順」にソートされた
print(sorted(ranking, key=ranking.get, reverse=True))






print('''
    ######:##### TODO: ### 　標準ライブラリ　 ##########################
     💎# DOC: https://docs.python.org/ja/3/library/index.html
    はじめから組み込まれているものではない。➡自分で読み込む必要がある。
    ※標準ライブラリで良く利用される、コレクションを使ってみる
    ''')

# 文字列の中に、該当する文字が何個あるを数える
# 結果は、辞書型が好ましい「〇：10」
s = 'tyuiohjruirtnfjdkahfdbggfdf'

# 通常の書き方
d = {}
for i in s:
    if i not in d:
        d[i] = 0
    d[i] += 1
print(d)



# 少し良い感じの書き方
d = {}
for i in s:
    if i not in d:
        # i(まだ文字)が追加されていなければ、「新追加文字：個数」の要素を辞書に追加する
        d.setdefault(i, 0)
    d[i] += 1
print(d)


# 良い感じの書き方
from collections import defaultdict
# 🟡🟡🟡もし、Keyに対してのバリューに指定がない時は、Integerのデフォルト「0」が入るようになる
d = defaultdict(int)

for i in s:
    d[i] += 1

print(d)





print('''
    ########### TODO: ### 　外部サードパーティのライブラリのインストール　 ##########################
    ターミナルで、
        １：インストールしたい仮想環境を向いてることを確認
        ２：pip install ライブラリ名
        ３：Enterで実行
        ４：該当ライブラリをimport
        ５：呼び出して利用
    ''')
from termcolor import colored
print(colored('text', 'red'))




print('''
    ######:## TODO: ### 　importの記法（ルール)　 ##########################
    ・1行1ライブラリ」として書く
    ・アルファベット順にならべる（A→Z）
    ・標準ライブラリ と サードパーティ の間に1行入れて書く
    ''')
#  🟡各種パッケージの保存場所
#     ・標準ライブラリ： anaconda3 の python3.x/ 配下
#     ・サードパーティ製ライブラリ：anaconda3 の python3.x/site-package/ 配下
#     ・自身のパッケージ：ローカルのプロジェクトフォルダー内
#     ・ローカルパッケージ：ローカルのプロジェクトフォルダー内

# 🟡パッケージの保存場所を探したい
#   １；パッケージ名にカーソル合わる
#   ２：「F12」で定義先を開く
#   ３：上部のパスを見ればわかる
#  ◆その他の方法◆
#       コードで、「print(ライブラリ名.__file__)」と書き実行 → ターミナルに表示される

#  🟡パッケージが読み込まれる階層を調べる
# 　　→　コードで「print(sys.path)」と書き実行
# 　　→　表示された階層内なら読み込まれる
# 　　　　※それ以外に、ライブラリを配置しても読み込まれない
#
# 　　→　🛑ライブラリの読み込み優先は、表示結果の上から
# 　　　　　ローカル優先で、
#               例えば、標準ライブラリと同一名をローカルに作ってしまったら、
# 　　　　　　　　　　　　　本家ではなくローカルの自作ライブラリがよびだされてしまうので注意！


# # 💎標準ライブラリ（A→Z）
# import collections
# import os
# import sys

# # 💎外部サードパーティー（A→Z）
# import termcolor

# # 💎自分たちのパッケージ（A→Z）
# from lesson_package import utils
# from lesson_package.talk import animal, human

# # 💎ローカルファイル（A→Z）
# import config（今のところない）



