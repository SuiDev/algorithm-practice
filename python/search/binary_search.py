"""
Question:
    ソート済みのリストの中から目的の値の場所を出力するプログラム

Note:
    二分探索
"""
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
objective_value = 1

min = 0
max = len(sorted_list) - 1

while min <= max:
    middle = (min + max) // 2
    if sorted_list[middle] == objective_value:
        print(middle)
        break
    elif sorted_list[middle] < objective_value:
        min = middle + 1
    else:
        max = middle - 1
