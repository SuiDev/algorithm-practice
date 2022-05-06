"""
Question:
    20の階乗を出力するプログラム

Note:
    ライブラリを使わず、再帰関数で実装する
"""
def factorial(number):
    if number:
        return number * factorial(number - 1)
    else:
        return 1

print(factorial(20))
    