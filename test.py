import random
import timeit

from sort import bubble_sort, selection_sort, insert_sort, shell_sort

def generate_num(n):
    return [random.randint(0,1000000) for _ in range(n)]

def shell_list(n):
    hibbard = []
    normal = [n // 2]
    sedg = []
    a = n // 2
    while a > 1:
        a = a // 2
        normal.append(a)
    for i in range(n):
        gap = 2 ** (i+1) - 1
        if gap < n:
            hibbard.append(gap)
        s1 = 9 * (4 ** i - 2 ** i) + 1
        if s1 < n:
            sedg.append(s1)
        s2 = 4 ** i - 3 * 2 ** i + 1
        if s2 < n and s2 > 0:
            sedg.append(s2)
    hibbard.reverse()
    sedg.sort(reverse=True)
    return {'hibbard': hibbard,
            'normal': normal,
            'sedg': sedg}

# 装饰器统计递归次数
def recursion_count(func):
    num = 0
    def call_func(*args, **kwargs):
        result = func(*args, **kwargs)
        nonlocal num
        num += 1
        print(f'递归执行次数: {num}.')
        return result
    return call_func

@recursion_count
def fab(n):
    if n == 1: return 1
    if n == 2: return 1
    return fab(n-2) + fab(n-1)

def fabs(n):
    result = []
    for i in range(n):
        result.append(fab(i+1))
    return result

if __name__ == '__main__':
    #n1 = 1000
    #n2 = 1000
    #num = generate_num(n1)
    #t0 = timeit.timeit("bubble_sort(*num)", setup="from __main__ import bubble_sort, num", number=n2)
    #t1 = timeit.timeit("selection_sort(*num)", setup="from __main__ import selection_sort, num", number=n2)
    #t2 = timeit.timeit("insert_sort(*num)", setup="from __main__ import insert_sort, num", number=n2)
    #t3 = timeit.timeit("shell_sort(*num, quence='hibbard')", setup="from __main__ import shell_sort, num", number=n2)
    #t4 = timeit.timeit("shell_sort(*num, quence='sedg')", setup="from __main__ import shell_sort, num", number=n2)
    #t5 = timeit.timeit("shell_sort(*num, quence='normal')", setup="from __main__ import shell_sort, num", number=n2)
    #print(f'{n1}个随机数排序重复{n2}次，\n冒泡{t0}，\n选择{t1}，\n插入{t2}，\n希尔-Hibbard{t3}，\n希尔-Sedg{t4}，\n希尔-二分{t5}')
    print(fabs(10))
