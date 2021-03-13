
# 🛑どんなスクリプトでも、ファイルが他から呼び出されないように、このように書く。
#     ファイルに、いきなり生でコードを書かない
    #   💎main()を定義して、if文で、このファイルがmain実行されているときのみ、main()を実行するとする
        # Python では、これが安全で良しとされている


def main():
    # 🟡ここに本来処理したい内容を書くようにする
    print()


if __name__ == '__main__':
    main()