"""
Question:
    2から100までの整数が素数かどうか調べ、素数であればその数を出力するプログラム

Note:
    nが素数であるかどうかは、√nまでの素数で割れるかを確かめれば良い
"""
import math

for i in range(2, 101):
    output_flag = True
    # √nを求め、小数点以下を切り上げ
    sqrt = math.ceil(math.sqrt(i))

    for j in range(2, sqrt + 1):
        if not i % j:
            output_flag = False
            break

    if output_flag:
        print(i, end=", ")
