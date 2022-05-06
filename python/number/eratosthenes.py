"""
Question:
    2から100までの整数が素数かどうか調べ、素数であればその数を出力するプログラム

Note:
    エラトステネスのふるい
    リストの変更を最低限にする
"""
limit = 100
prime_number_list = []
is_prime_list = [True] * (limit + 1)
is_prime_list[0] = False
is_prime_list[1] = False

for p in range(0, limit + 1):
    if not is_prime_list[p]:
        continue

    prime_number_list.append(p)

    for i in range(p * p, limit + 1, p):
        is_prime_list[i] = False

print(prime_number_list)
