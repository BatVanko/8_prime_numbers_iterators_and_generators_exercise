def get_primes(*args):
    for num in args:
        for el in num:
            flag = True
            if el > 1:
                for i in range(2, el):
                    if el % i == 0:
                        flag = False
                        break
                if flag:
                    yield el


prime_num = get_primes([-2, 0, 0, 1, 1, 0])
print(list(prime_num))
