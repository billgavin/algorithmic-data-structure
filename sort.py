import fire
import sys
# 设置最大递归深度
sys.setrecursionlimit(100000)

# 冒泡排序
def bubble_sort(*num, reverse=False):
    num = list(num)
    n = len(num)
    change = 0
    cycle = 0
    for i in range(n):
        # 设定一个标记，若为true，则表示此次循环没有进行交换，也就是待排序列已经有序，排序已经完成。
        flag = True
        for j in range(n-i-1): # 从上一轮交换位置开始比较
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                flag = False
                change += 1
            cycle += 1
        if flag: # 没有交换时，已为有序，跳出循环
            break
        for j in range(-1, i-n, -1):
            if num[j] < num[j-1]:
                num[j], num[j-1] = num[j-1], num[j]
                flag = False
                change += 1
            cycle += 1
        if flag: # 没有交换时，已为有序，跳出循环
            break
    print(f'冒泡排序共循环{cycle}次，交换{change}次。')
    if reverse:
        num.reverse()
    return num

# 选择排序
def selection_sort(*num, reverse=False):
    num = list(num)
    n = len(num)
    change = 0
    cycle = 0
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if num[j] < num[mini]:
                mini = j
                change += 1
            cycle += 1
        if i != mini:
            num[i], num[mini] = num[mini], num[i]
    print(f'选择排序共循环{cycle}次，交换{change}次。')
    if reverse:
        num.reverse()
    return num
    
# 插入排序
# 适配希尔排序，增加gap参数
def insert_sort(*num, gap=1, reverse=False):
    num = list(num)
    n = len(num)
    change = 0
    cycle = 0
    for i in range(gap, n):
        tmp = num[i]
        j = i
        index = i % gap
        while j > index and tmp < num[j-gap]:
            num[j] = num[j-gap]
            j -= gap
            change += 1
            cycle += 1
        else:
            num[j] = tmp
            change += 1
    print(f'插入排序共循环{cycle}次，交换{change}次。')
    if reverse:
        num.reverse()
    return num

# 生成希尔序列
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

# 希尔排序
def shell_sort(*num, quence='normal', reverse=False):
    num = list(num)
    n = len(num)
    gaps = shell_list(n)[quence]
    print(f'希尔序列为：{quence}', gaps)
    for gap in gaps:
        result = insert_sort(*num, gap=gap, reverse=reverse)
        print(f'当前增量为{gap}', result)
        

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

# 归并排序
@recursion_count
def merge_sort(*num, reverse=False):
    num = list(num)
    if len(num) == 1:
        return num
    # 取拆分的中间位置
    mid = len(num) // 2
    # 拆分过后左右两侧子串
    left = num[:mid]
    right = num[mid:]
    # 递归调用自己，一直到拆分成单个元素
    lnum = merge_sort(*left)
    rnum = merge_sort(*right)
    return merge(lnum, rnum, reverse)

def merge(left, right, reverse):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
    result = []
    while len(left) > 0 and len(right) > 0:
        #为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    #while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += left
    result += right
    if reverse:
        result.reverse()
    return result
    
def get_mid(n, start=0):
    return (n + start) // 2

def get_pivot(n, *arr):
    arr = list(arr)
    n = len(arr)
    mid = get_mid(n)
    result = [arr[0], arr[mid], arr[-1]]
    if n > 3:
        lmid = get_mid(mid)
        rmid = get_mid()
        

# 快速排序
def quick_sort(*num, reserve=False):
    num = list(num)
    n = len(num)
    

if __name__ == '__main__':
    fire.Fire()
