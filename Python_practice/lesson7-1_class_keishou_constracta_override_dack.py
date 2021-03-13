

print('''
    ########### TODO: ### 　クラスの書き方　 ##########################
    🟡クラス内のルール
        💎クラス名：キャメルケース、大文字開始、（）内に「object」
        💎def __init__(self)関数を創る
        💎インスタンス化したいクラス内で
        　　　ー保持したい変数：　self.変数名とする
           　ー利用したいメソッド：　引数として(self)を入れる
                                　クラス内の他関数内で呼び出す場合、self.関数名()とする
                                   　➡呼び出したときに、selfは引数にぶち込まなくてOK

    ''')
# 🛑()内の「object」は、Python2では必須で、Python3では、なくてもOKに。
# 　　➡ ただ、継承の観点から、コードスタイル上、（）内の｛object｝は記載する方が良しとされている
# 🛑中には、書かない人もいるが、驚くな.

class Person(object):
    # 🟡コンストラクタ
    #   💎インスタンス化されたときに、まず最初に呼び出される関数
    #       🛑「self」
    # 　　          ➡引数でわたってきた値を保持する
    #           関数内で、インスタンス化されたときに渡された値を使いたいのなら、
    #           その関数にも、「self」を引数に渡すようにする
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.someting_say()
        self.say('天才')

    def say(self, word):
        print(self.name, 'の車か～', word, "!")

    def someting_say(self):
        print("hello")

    # 🟡デストラクタ
    #       💎インスタンスが消滅するときに、自動実行される関数.
    #       🛑予測変換で出てこない…自分で覚えてつくる
    #   💡インスタンスが利用されなくなってプラグラムが終了するときか、
    # 　　　　ex ：チャットに応答がなく、制限時間を迎えたとき
    # 　　明示的に、「del インスタンス名」を呼び出したときに発火.
    def __del__(self):
        print('bey')



#🟡 インスタンス化（java の new）
person = Person('Make')
person.someting_say()

print('########################')
# del person





print('''
    ########### TODO: ### 　クラスの継承 / オーバーライド ##########################
    🟡継承の使いどころ
        💎似た機能を持つ関数が複数クラスで存在しそうなとき
        　　➡親クラス（継承元）を作ることで、子クラスで同じコードを書かなくて済む

    🟡クラス継承のルール
        💎クラス名後の（）に継承したいクラス名を入れる
        💎継承元関数を暗黙的に持ってる
        💎継承元になく、このクラスのみの関数のみ記載
        💎関数の引数には、「self」を入れる
    ''')
# 上位クラスが「Object」のため、継承しているような雰囲気で、(object)なのかも？知らんけど
class Car(object):
    def __init__(self, model=None) -> None:
        super().__init__()
        self.model = model
    # 🛑selfをわすれないように！エラーになる
    def run(self):
        print('run')

# 🟡継承したいクラス名を()中に入れる
# 🟡Carクラスのメソッドも暗黙的に持っている
# 🟡ココには、TesraCarにしかない、関数のみを書く.
class TesraCar(Car):
    def __init__(self, model, enable_auto_run=False) -> None:
        super().__init__(model=model)
        self.enable_auto_run = enable_auto_run

    def run(self):
        print(self.model, self.enable_auto_run, 'super run!!')

    # 🛑selfをわすれないように！エラーになる
    def autorun(self):
        print('autorun')


car = Car()
car.run()

tesra = TesraCar(model='tesra', enable_auto_run=True)
tesra.autorun()
tesra.run()


# ###################　練習　##################
class Robot(object):
    def __init__(self, name='名無し号', hp=0) -> None:
        super().__init__()
        self.name = name
        self.hp = hp
        self.start()

    def start(self):
        print(self.name, 'は起動しました。', self.hp, 'のHPがあります。')

    def attack(self):
        print('No Attack')


class SuperRobot(Robot):
    def __init__(self, name, hp, is_battle=False) -> None:
        # 🟡init関数を書いているため、親のInit関数を上書きしてしまう
        #      💎 super()で親を呼び出すこと➡「親の要請」という.
        # 　　　💎　↓のように、親のInitをSuperを呼び出し、使いまわせるところは使い、コードの重複を防ぐ
        super().__init__(name=name, hp=hp)
        self.is_battle = is_battle

    def attack(self):
        if self.is_battle:
            print(self.name, 'は、攻撃しました')
        else:
            print('やだよ！！')


robot = Robot(name='Robot_1', hp=50)
super_robot = SuperRobot(name='Robot_2', hp=100, is_battle=True)
sp_robot_2 = SuperRobot(name='NotAttackRobo', hp=20, is_battle=False)

robot.attack()
super_robot.attack()
sp_robot_2.attack()



print('''
    ########### TODO: ### 　プロパティを使った属性設定　 ##########################

    ー🛑🛑🛑 プライベート変数に、外部ファイルから代入すると、上書きではなく新たに変数を再定義して代入となる


    💎「なにもなし」:
            ー 自由に書き換え可能（public変数）

    💎「_ + 変数名」:
            ー 条件付きの Private 変数 のようなもの
            ー getter（@property）のみ作成すれば、閲覧のみOK
            ー gettter　/ setterを作成し、[_]なしでアクセスすると読み書きできる
            ー ゲッターとして「🟡@property」使用
            ー セッターとして「🟡@変数名.seter」使用

    💎「__ + 変数名」:
            ー Private 変数
            ー getter（デコレーター：@property）のみ作成すれば、閲覧のみOK
            ー gettter　/ setter（@変数名.setter）を作成し、[__]なしでアクセスすると読み書きできる
            ー 定義したクラス内でのみ、直接アクセス可能。
            ー ゲッターとして「🟡@property」使用
            ー セッターとして「🟡@変数名.seter」使用
    ''')


class ParameterLesson(object):

    def __init__(self,
                 age,
                 userId,
                 passwd=123,
                 name='名無しさん') -> None:
        super().__init__()
        # 🛑変数は、コンストラクタ（init関数）の中で定義する（Javaのように、箱だけ作らない）
        self.__age = age # ❌ Privete変数
        self._userId = userId# 🟡 ある条件のもと書き換え可能（原則不可）
        self._passwd = passwd # 🟡 ある条件のもと書き換え可能（原則不可）
        self.name = name     # ⭕ 自由に書き換え可能

    @property
    def age(self):
        return self.__age
    @property
    def userId(self):
        return self._userId

    @age.setter
    def age(self, age):
        self.__age = age


    # 🟡setter（ある条件のもと書き換え可能にする時に使用）
    #   ※「getter名.setter」とする
    # 　　🛑あくまで例で、パスワードチェックの方法はもっと厳重（ハッシュやAES,shなど）🛑.
    @userId.setter
    def userId(self, userId):
        if self._passwd == 123:
            self._userId = userId
        else:
            raise ValueError

pp = ParameterLesson(age=28, userId='aaa', passwd=123)
# 🟡プライベート変数のため、アクセスできない
# print(pp.__age)

# 🛑🛑バグの温床🛑🛑ただし、以下のように書くと、クラス内の変数を上書きしているのではなく、新しく再定義していることになる
pp.__age = 10
# 🛑🛑🛑こうなると、見た目上（中身も？）上書きしているようにみえてしまう。
print(pp.__age)

################################　練習　###############################

class SuperMan(object):

    def __init__(self, name,
                 age,
                 can_fly=False) -> None:
        super().__init__()
        self.__name = name
        self.__age = age
        self.__can_fly = can_fly

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name



man = SuperMan(name='bob', age=30, can_fly=True)

# 🛑🛑🛑クラスSuperMan内の、「__name」と、↓の「name」は、別物
#   新しく、nameという変数を定義して、格納した感じ
# 　たとえば、SuperManクラスに一切出てこない、「tensai」も定義できてしまう
# ❓❓❓　となると、setterの意味って。。❓❓❓.
man.name = 'Hello'
man.tensai = 789

print(man.tensai)
print(man.name)

# 🛑以下のように、直接「__」付きのプロパティにアクセスすると、次のようなエラーが出る
# AttributeError: 'SuperMan' object has no attribute '__name'
# 🛑プライベート変数は、getter/setter（__なし）を返してしか、アクセスできない
# print(man.__name)




print('''
    ########### TODO: ### 　ダックタイピング　 ##########################
    ポリモーフィズムは子クラスが親クラスのメソッドをオーバーライドできること。
        例：クラスAnimalはメソッドtalk()を持つことができ、サブクラスDogとCatのAnimalはメソッドtalk()異なる音を出します。

    ダックタイピングは、特定のメソッドを持つ、"すべてのオブジェクト"を受け入れること。
        animal.quack()。
        指定されたオブジェクトanimalに、呼び出したいメソッドがある場合はOK。
        animalが実際にDuckであるか、別の動物であるかどうかは関係ありません。
        たとえば、quack()というメソッドがある場合、そのオブジェクトがアヒルであるかのように動作できます）。
    ''')

class Person(object):
    def __init__(self, age=1) -> None:
        super().__init__()
        self.age = age

    def drive(self):
        if self.age < 18:
            raise Exception('Noooo!! drive!!')
        print('ride ok!!')

# 🟡継承しているため、drive()は持っている鄭になっている
class Adult(Person):
    def __init__(self, age=18) -> None:
        if age < 18:
            raise ValueError
        super().__init__(age=age)

# 🟡継承しているため、drive()は持っている鄭になっている
class Baby(Person):
    def __init__(self, age=1) -> None:
        if age >= 18:
            raise ValueError
        super().__init__(age=age)
    # 🟡オーバーライドもできる
    def drive(self):
        print('yeah!!!!!!!!!!!')

# 🟡🛑Personを継承していないため、drive()はもっていない
class Someting(object):
    def __init__(self) -> None:
        super().__init__()



class Car(object):
    def __init__(self) -> None:
        super().__init__()

    def ride(self, person):
        # 🟡💎personが具体的にどの型で、
        #     本当にdrive()を持っているかわからないが、"実装しているとみなせる”
        person.drive()



adult = Adult()
baby = Baby()
# 🛑以下のクラスは、driveを持っていない（car.drive()に入れるとエラーになる）
st = Someting()
car = Car()

car.ride(baby)




print('''
    ########### TODO: ### 　抽象クラスについて　 ##########################
    💎🛑基本的には、利用しないほうがいい。
    　➡ python には、元々抽象クラスの概念がなく、後付け的にできた。
      ➡故にちょっと分かりにくいかも？
      ➡そもそも、ダックタイピングを使えば利用できてしまうし、オーバーライドもできる
      ➡コードスタイルでも、推奨されていない
    ''')

# 🟡抽象クラスの書き方
import abc

class Sample(metaclass = abc.ABCMeta):
    def __init__(self, age=1) -> None:
        self.age = age

    @abc.abstractmethod
    def eat(self):
        pass



print('''
    ########### TODO: ### 　多重継承　 ##########################
    💎🛑なるべく、Pythonでは、利用しないような設計にすべき
            ➡ 多重継承の優先度を知らないことでバグに繋がることがある
            ex：
                class PersonCar(Person, Car)の時、
                親クラスのPersonと、Carの両方に、run()が存在していた場合、
                person_car = PersonCar()
                person_car.run() ←🛑ここで実行されるのは、Personクラスのrun()となる

            ※この優先度を知らないで実装し、期待通りの動作にならないこともあることに注意
    ''')






print('''
    ########### TODO: ### 　クラス変数　 ##########################
    💎違うインスタンス間で共有される変数のこと。
    たとえば、体力のHPという変数をクラス変数にすると、勇者Aと勇者Bで、HPが共有されてしまう。
    　（勇者AのHPが100→30になった、勇者Bは何もしていないのに30になってる！）

     # 💡💎数を共有したくないとき💎💡
     # 　Init関数内だけの定義にする

     ★定数クラス的につかうのはあり、

    ''')

class T(object):
    # 🟡クラス変数
    words = []

    def __init__(self) -> None:
        super().__init__()

    def add_word(self, word):
        # 🟡[self]をつけてアクセス可能
        self.words.append(word)

t = T()
t1 = T()
t.add_word(1)
t1.add_word(2)

# リストは共有されて、以下のような出力結果となる
# [1, 2]
# [1, 2]」
print(t.words)
print(t1.words)





print('''
    ########### TODO: ### 　クラスメソッド と スタティックメソッド　 ##########################
    💎インスタンス化することなく、メソッドを利用できるようになる
    ''')
# 🛑あまり使わない：Staticメソッド(どこからでも、メソッド名だけでアクセスできる)
def about(yaer):
    print('static!!!')

class SometingUtils(object):

    class_prop = 'クラス変数！'

    def __init__(self) -> None:
        super().__init__()

    # 🟡デコレーターをつけ、引数にクラスを表す「cls」を入れる
    @classmethod
    def call_me(cls):
        # 🟡インスタンス作成しなくても、クラス変数にアクセスできるようになる
        return cls.class_prop

# 🟡インスタンス化することなく、メソッドを利用できるようになる
print(SometingUtils.call_me())
about(2180)



print('''
    ########### TODO: ### 　　 ##########################
    ''')